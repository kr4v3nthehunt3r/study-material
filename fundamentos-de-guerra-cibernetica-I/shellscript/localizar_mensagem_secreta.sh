#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: localizar_mensagem_secreta.sh
# Descrição do módulo:
#   Procura uma expressão específica em arquivos de um diretório, exibindo o
#   nome do arquivo e a linha correspondente quando houver ocorrência.
#
# Uso:
#   ./localizar_mensagem_secreta.sh [diretorio] [padrao]
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Garante que o diretório informado exista.
# Parâmetros:
#   $1 -> Caminho do diretório a ser pesquisado.
# ------------------------------------------------------------------------------
validar_diretorio() {
    local diretorio="$1"

    if [[ ! -d "$diretorio" ]]; then
        echo "Erro: o diretório '$diretorio' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: buscar_mensagem
# Descrição:
#   Procura o padrão desejado recursivamente no diretório informado.
# Parâmetros:
#   $1 -> Diretório de busca.
#   $2 -> Padrão textual a ser procurado.
# ------------------------------------------------------------------------------
buscar_mensagem() {
    local diretorio="$1"
    local padrao="$2"

    echo "Busca por padrão: $padrao"

    if ! grep -RIn --binary-files=without-match -- "$padrao" "$diretorio"; then
        echo "Nenhuma ocorrência foi encontrada."
    fi
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-.}"
    local padrao="${2:-MENSAGEM SECRETA}"

    validar_diretorio "$diretorio"
    buscar_mensagem "$diretorio" "$padrao"
}

main "${1:-}" "${2:-}"
