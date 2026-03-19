#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: listar_maiores_arquivos.sh
# Descrição do módulo:
#   Lista os 10 maiores arquivos de um diretório, sem recursão, exibindo o nome
#   e o tamanho em formato legível.
#
# Uso:
#   ./listar_maiores_arquivos.sh <diretorio>
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de uso do script.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <diretorio>"
}

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Garante que o diretório informado exista.
# Parâmetros:
#   $1 -> Caminho do diretório.
# ------------------------------------------------------------------------------
validar_diretorio() {
    local diretorio="$1"

    if [[ -z "$diretorio" ]]; then
        echo "Erro: informe um diretório."
        exibir_uso
        exit 1
    fi

    if [[ ! -d "$diretorio" ]]; then
        echo "Erro: o diretório '$diretorio' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: formatar_tamanho
# Descrição:
#   Converte bytes em formato legível, desde que o utilitário numfmt exista.
# Parâmetros:
#   $1 -> Quantidade em bytes.
# ------------------------------------------------------------------------------
formatar_tamanho() {
    local bytes="$1"

    if command -v numfmt >/dev/null 2>&1; then
        numfmt --to=iec --suffix=B "$bytes"
    else
        echo "${bytes}B"
    fi
}

# ------------------------------------------------------------------------------
# Função: listar_top_arquivos
# Descrição:
#   Lista os 10 maiores arquivos do diretório informado.
# Parâmetros:
#   $1 -> Caminho do diretório.
# ------------------------------------------------------------------------------
listar_top_arquivos() {
    local diretorio="$1"

    echo "10 maiores arquivos em: $diretorio"

    find "$diretorio" -maxdepth 1 -type f -printf '%s\t%f\n' \
        | sort -nr \
        | head -n 10 \
        | while IFS=$'\t' read -r tamanho nome; do
            echo "$nome - $(formatar_tamanho "$tamanho")"
        done
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-}"

    validar_diretorio "$diretorio"
    listar_top_arquivos "$diretorio"
}

main "${1:-}"
