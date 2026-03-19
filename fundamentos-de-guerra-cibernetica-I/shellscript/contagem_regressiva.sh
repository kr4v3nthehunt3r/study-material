#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: contagem_regressiva.sh
# Descrição do módulo:
#   Realiza uma contagem regressiva a partir de um número inteiro não negativo
#   informado via argumento ou digitado pelo usuário.
#
# Uso:
#   ./contagem_regressiva.sh [numero]
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de uso do script.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 [numero_inteiro_nao_negativo]"
}

# ------------------------------------------------------------------------------
# Função: ler_numero
# Descrição:
#   Obtém o número a partir do argumento ou via entrada interativa.
# Parâmetros:
#   $1 -> Número informado como argumento.
# ------------------------------------------------------------------------------
ler_numero() {
    local numero="${1:-}"

    if [[ -z "$numero" ]]; then
        read -r -p "Informe o valor inicial da contagem: " numero
    fi

    echo "$numero"
}

# ------------------------------------------------------------------------------
# Função: validar_numero
# Descrição:
#   Garante que o valor informado seja um número inteiro não negativo.
# Parâmetros:
#   $1 -> Valor informado pelo usuário.
# ------------------------------------------------------------------------------
validar_numero() {
    local numero="$1"

    if [[ ! "$numero" =~ ^[0-9]+$ ]]; then
        echo "Erro: informe um número inteiro não negativo."
        exibir_uso
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: executar_contagem
# Descrição:
#   Exibe os valores da contagem regressiva até zero.
# Parâmetros:
#   $1 -> Número inicial da contagem.
# ------------------------------------------------------------------------------
executar_contagem() {
    local numero="$1"

    while (( numero >= 0 )); do
        echo "$numero"
        sleep 1
        ((numero--))
    done

    echo "FIM!"
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local numero

    numero="$(ler_numero "${1:-}")"
    validar_numero "$numero"
    executar_contagem "$numero"
}

main "${1:-}"
