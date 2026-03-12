#!/bin/bash

# 1. Verifica se o parâmetro foi passado
if [ -z "$1" ]; then
    echo "Erro: Nenhum parâmetro fornecido."
    exit 1
fi

# 2. Verifica se o parâmetro é um número (usa expressão regular)
if [[ ! "$1" =~ ^[0-9]+$ ]]; then
    echo "Erro: O parâmetro '$1' não é um número válido."
    exit 1
fi

NUM=$1

# 3. Verifica se está no intervalo de 1 a 10 inclusive
if [ "$NUM" -ge 1 ] && [ "$NUM" -le 10 ]; then
    echo "O número $NUM está no intervalo de 1 a 10."
    
    # 4. Testa se é maior, menor ou igual a 5
    if [ "$NUM" -gt 5 ]; then
        echo "Resultado: $NUM é maior que 5."
    elif [ "$NUM" -lt 5 ]; then
        echo "Resultado: $NUM é menor que 5."
    else
        echo "Resultado: $NUM é igual a 5."
    fi
else
    echo "O número $NUM está fora do intervalo de 1 a 10."
fi