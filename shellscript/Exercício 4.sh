#!/bin/bash

# 1. Verifica se o parâmetro (site) foi passado
if [ -z "$1" ]; then
    echo "Erro: Forneça um endereço de site ou IP. Ex: ./monitor_host.sh www.google.com"
    exit 1
fi

SITE=$1

echo "Iniciando 5 pings para $SITE..."

# 2. Executa o ping e captura a saída em uma variável
# -c 5 (5 pacotes)
SAIDA_PING=$(ping -c 5 "$SITE" 2>/dev/null)

# 3. Verifica se o comando foi bem-sucedido (Exit Code 0)
if [ $? -ne 0 ]; then
    echo "Erro: Não foi possível alcançar o host '$SITE'. Verifique a conexão ou o endereço."
    exit 1
fi

# 4. Extração de informações usando manipulação de texto
# Extrai o IP (fica entre parênteses na primeira linha do ping)
IP_HOST=$(echo "$SAIDA_PING" | head -n 1 | grep -oE "\([0-9.]+\)" | tr -d '()')

# Extrai as estatísticas (min/avg/max) da última linha
# Exemplo de linha: rtt min/avg/max/mdev = 15.123/18.456/22.789/2.111 ms
STATS=$(echo "$SAIDA_PING" | tail -n 1 | cut -d '=' -f 2 | tr -d ' ms')

MIN_TIME=$(echo "$STATS" | cut -d '/' -f 1)
AVG_TIME=$(echo "$STATS" | cut -d '/' -f 2)
MAX_TIME=$(echo "$STATS" | cut -d '/' -f 3)

# 5. Impressão dos resultados conforme solicitado
echo "-------------------------------------------"
echo "Informações coletadas para: $SITE"
echo "Endereço IP: $IP_HOST"
echo "Menor tempo de resposta: ${MIN_TIME}ms"
echo "Média de tempo de resposta: ${AVG_TIME}ms"
echo "Maior tempo de resposta: ${MAX_TIME}ms"
echo "-------------------------------------------"