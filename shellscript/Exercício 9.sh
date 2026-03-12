#!/bin/bash

# Função para validar se a entrada é um número inteiro positivo maior que zero
validar_numero() {
    # Loop infinito que só para quando o usuário digitar um número válido
    while true; do
        read -p "Digite um número inteiro positivo maior que zero: " NUM
        
        # Verifica se é numérico e se é maior que zero
        if [[ "$NUM" =~ ^[0-9]+$ ]] && [ "$NUM" -gt 0 ]; then
            break # Sai do loop de solicitação
        else
            echo "Erro: Entrada inválida. Por favor, tente novamente."
        fi
    done
}

# 1. Solicita e valida o número
validar_numero

echo "Iniciando contagem regressiva..."

# 2. Laço de repetição para contagem regressiva (usando WHILE)
# Enquanto o número for maior ou igual a zero, o laço continua
while [ "$NUM" -ge 0 ]; do
    echo "$NUM"
    
    # 3. Atraso de 1 segundo entre cada número
    sleep 1
    
    # Decrementa o valor de NUM
    NUM=$((NUM - 1))
done

# 4. Mensagem final
echo "FIM!"