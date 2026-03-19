#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: compara_5.sh
# Descrição do módulo:
#   Recebe um número inteiro entre 1 e 10 e informa se esse valor é maior,
#   menor ou igual a 5. O script também valida o formato da entrada.
#
# Objetivos do módulo:
#   - Validar o parâmetro recebido;
#   - Garantir que o valor esteja no intervalo esperado;
#   - Comparar o número com o valor 5;
#   - Exibir o resultado da comparação.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

NUMERO="${1:-}"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Informa ao usuário a sintaxe correta de utilização do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <numero>"
    echo "Exemplo: $0 7"
}

# ------------------------------------------------------------------------------
# Função: validar_numero
# Descrição:
#   Verifica se o valor recebido é um número inteiro.
# Parâmetros:
#   $1 -> Valor informado pelo usuário.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_numero() {
    local numero="$1"

    if [[ -z "$numero" ]]; then
        exibir_uso >&2
        exit 1
    fi

    if ! [[ "$numero" =~ ^-?[0-9]+$ ]]; then
        echo "[ERRO] Informe um número inteiro válido." >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: validar_intervalo
# Descrição:
#   Garante que o número informado esteja entre 1 e 10.
# Parâmetros:
#   $1 -> Número inteiro validado.
# Retorno:
#   0 se o número estiver no intervalo; 1 caso contrário.
# ------------------------------------------------------------------------------
validar_intervalo() {
    local numero="$1"

    if (( numero < 1 || numero > 10 )); then
        echo "Fora do intervalo permitido (1 a 10)."
        return 1
    fi

    return 0
}

# ------------------------------------------------------------------------------
# Função: comparar_com_cinco
# Descrição:
#   Compara o número informado com o valor 5 e imprime o resultado.
# Parâmetros:
#   $1 -> Número inteiro validado.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
comparar_com_cinco() {
    local numero="$1"

    if (( numero > 5 )); then
        echo "> 5"
    elif (( numero < 5 )); then
        echo "< 5"
    else
        echo "= 5"
    fi
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Conduz o fluxo principal do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    validar_numero "$NUMERO"

    if validar_intervalo "$NUMERO"; then
        comparar_com_cinco "$NUMERO"
    fi
}

principal
