#!/bin/bash

# 1. Validação: Verifica se o parâmetro existe
if [ -z "$1" ]; then
    echo "Erro: Forneça um número como parâmetro."
    exit 1
fi

# 2. Validação: Verifica se é um número inteiro (Regex)
if [[ ! "$1" =~ ^[0-9]+$ ]]; then
    echo "Erro: O valor '$1' não é um número inteiro válido."
    exit 1
fi

# 3. Lógica de Paridade
# Usamos $(( ... )) para expansão aritmética
NUM=$1

if [ $((NUM % 2)) -eq 0 ]; then
    echo "O número $NUM é PAR."
else
    echo "O número $NUM é ÍMPAR."
fi