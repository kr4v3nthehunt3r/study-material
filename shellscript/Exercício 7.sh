#!/bin/bash

# 1. Validação de parâmetros
if [ "$#" -ne 2 ]; then
    echo "Erro: Parâmetros insuficientes."
    echo "Utilização: $0 <wordlist.txt> <arquivo.jpg>"
    exit 1
fi

WORDLIST=$1
IMAGEM=$2

# 2. Definição da função de teste
# Recebe: $1 (arquivo) e $2 (senha)
teste_steg() {
    local ARQ=$1
    local PASS=$2

    # Tenta extrair. 
    # -sf: source file | -p: password | -f: force overwrite
    # Redirecionamos a saída para /dev/null para manter o terminal limpo
    steghide extract -sf "$ARQ" -p "$PASS" -f > /dev/null 2>&1
    
    # Retorna o status do comando steghide (0 se sucesso, != 0 se falha)
    return $?
}

# 3. Inicialização de variáveis
CONTADOR=0
SENHA_ENCONTRADA=""

echo "Iniciando Bruteforce em: $IMAGEM..."
echo "Utilizando a lista: $WORDLIST"
echo "------------------------------------------"

# 4. Laço de repetição para ler a wordlist
while read -r SENHA; do
    ((CONTADOR++))
    
    # Imprime o progresso na mesma linha (\r) para não poluir a tela
    printf "\rTentativa nº: %d [Testando: %s]          " "$CONTADOR" "$SENHA"

    # Chama a função e verifica o retorno
    if teste_steg "$IMAGEM" "$SENHA"; then
        SENHA_ENCONTRADA=$SENHA
        echo -e "\n\n[+] SUCESSO!"
        echo "A senha encontrada foi: $SENHA_ENCONTRADA"
        echo "Total de tentativas: $CONTADOR"
        break
    fi

done < "$WORDLIST"

# 5. Caso o laço termine sem encontrar a senha
if [ -z "$SENHA_ENCONTRADA" ]; then
    echo -e "\n\n[-] Falha: Nenhuma senha da wordlist funcionou."
fi