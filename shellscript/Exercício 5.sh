#!/bin/bash

# 1. Validação de parâmetros (deve ser exatamente 1)
if [ "$#" -ne 1 ]; then
    echo "Erro: Uso incorreto."
    echo "Utilização: $0 <endereço_ip>"
    exit 1
fi

IP_ENTRADA=$1

# 2. Extração do endereço de rede /24
# Pega os 3 primeiros octetos e define a REDE (.0) e o PREFIXO para o loop
REDE=$(echo "$IP_ENTRADA" | cut -d '.' -f 1-3).0
PREFIXO=$(echo "$IP_ENTRADA" | cut -d '.' -f 1-3)

echo "Iniciando varredura na rede $REDE/24..."

# Limpa/Cria o arquivo de relatório e a lista temporária
> relatorio_scanner.txt
> hosts_up.tmp

# 3. Laço FOR para testar quais hosts estão UP (Varredura ICMP)
echo "Localizando hosts ativos..."
for i in {1..254}; do
    HOST="$PREFIXO.$i"
    # O ping envia 1 pacote com tempo de espera de 1 segundo
    if ping -c 1 -W 1 "$HOST" > /dev/null 2>&1; then
        echo "$HOST" >> hosts_up.tmp
    fi
done

# 4. Estrutura WHILE READ para iterar sobre a lista de hosts UP
echo "Analisando portas 22, 80 e 443 nos hosts localizados..."
while read IP_ATIVO; do
    # Executa o nmap nas portas específicas
    # O grep busca a linha da porta e o awk extrai o status (open/closed/filtered)
    STATUS_22=$(nmap -p 22 "$IP_ATIVO" | grep "22/tcp" | awk '{print $2}')
    STATUS_80=$(nmap -p 80 "$IP_ATIVO" | grep "80/tcp" | awk '{print $2}')
    STATUS_443=$(nmap -p 443 "$IP_ATIVO" | grep "443/tcp" | awk '{print $2}')

    # Caso o nmap não retorne a linha (porta filtrada ou erro), define como 'unknown'
    STATUS_22=${STATUS_22:-unknown}
    STATUS_80=${STATUS_80:-unknown}
    STATUS_443=${STATUS_443:-unknown}

    # Grava no relatório conforme solicitado
    echo "IP: $IP_ATIVO | Porta 22: $STATUS_22 | Porta 80: $STATUS_80 | Porta 443: $STATUS_443" >> relatorio_scanner.txt

done < hosts_up.tmp

# 5. Limpeza e Finalização
rm hosts_up.tmp
echo "O scanner da rede $REDE foi concluído, o resultado foi gravado no arquivo relatorio_scanner.txt"