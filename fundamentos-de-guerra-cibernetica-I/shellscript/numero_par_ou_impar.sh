#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: numero_par_ou_impar.sh
# Descrição do módulo:
#   Verifica se um número inteiro informado é par ou ímpar.
#
# Uso:
#   ./numero_par_ou_impar.sh [numero]
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: obter_numero
# Descrição:
#   Lê o número via argumento ou via entrada interativa.
# Parâmetros:
#   $1 -> Número informado como argumento.
# ------------------------------------------------------------------------------
obter_numero() {
    local numero="${1:-}"

    if [[ -z "$numero" ]]; then
        read -r -p "Informe um número inteiro: " numero
    fi

    echo "$numero"
}

# ------------------------------------------------------------------------------
# Função: validar_numero
# Descrição:
#   Garante que o valor informado seja um número inteiro.
# Parâmetros:
#   $1 -> Valor a ser validado.
# ------------------------------------------------------------------------------
validar_numero() {
    local numero="$1"

    if [[ ! "$numero" =~ ^-?[0-9]+$ ]]; then
        echo "Erro: informe um número inteiro válido."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: classificar_numero
# Descrição:
#   Exibe se o número é par ou ímpar.
# Parâmetros:
#   $1 -> Número inteiro.
# ------------------------------------------------------------------------------
classificar_numero() {
    local numero="$1"

    if (( numero % 2 == 0 )); then
        echo "PAR"
    else
        echo "ÍMPAR"
    fi
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local numero

    numero="$(obter_numero "${1:-}")"
    validar_numero "$numero"
    classificar_numero "$numero"
}

main "${1:-}"
