#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: buscar_palavras_chave.sh
# Descrição do módulo:
#   Procura palavras-chave em arquivos .txt de um diretório. O objetivo é apoiar
#   triagens simples de conteúdo textual em ambiente controlado.
#
# Uso:
#   ./buscar_palavras_chave.sh [diretorio] [padrao_regex]
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Verifica se o diretório informado existe.
# Parâmetros:
#   $1 -> Caminho do diretório.
# ------------------------------------------------------------------------------
validar_diretorio() {
    local diretorio="$1"

    if [[ ! -d "$diretorio" ]]; then
        echo "Erro: o diretório '$diretorio' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: buscar_ocorrencias
# Descrição:
#   Procura o padrão informado nos arquivos .txt do diretório.
# Parâmetros:
#   $1 -> Diretório de busca.
#   $2 -> Expressão regular a ser pesquisada.
# ------------------------------------------------------------------------------
buscar_ocorrencias() {
    local diretorio="$1"
    local padrao="$2"

    if ! grep -EiH -- "$padrao" "$diretorio"/*.txt 2>/dev/null; then
        echo "Nenhuma ocorrência encontrada para o padrão informado."
    fi
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-.}"
    local padrao="${2:-ataque|defesa|infiltracao}"

    validar_diretorio "$diretorio"
    buscar_ocorrencias "$diretorio" "$padrao"
}

main "${1:-}" "${2:-}"
