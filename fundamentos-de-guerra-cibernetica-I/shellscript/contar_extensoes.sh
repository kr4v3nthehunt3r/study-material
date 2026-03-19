#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: contar_extensoes.sh
# Descrição do módulo:
#   Lista os arquivos de um diretório e contabiliza quantos arquivos existem por
#   extensão. Arquivos sem extensão são agrupados como "sem_ext".
#
# Uso:
#   ./contar_extensoes.sh <diretorio>
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
# Função: obter_extensao
# Descrição:
#   Retorna a extensão do arquivo informado.
# Parâmetros:
#   $1 -> Caminho do arquivo.
# ------------------------------------------------------------------------------
obter_extensao() {
    local arquivo="$1"
    local nome_base
    local extensao

    nome_base="$(basename "$arquivo")"

    if [[ "$nome_base" == *.* && "$nome_base" != .* ]]; then
        extensao="${nome_base##*.}"
        echo "$extensao"
    else
        echo "sem_ext"
    fi
}

# ------------------------------------------------------------------------------
# Função: contar_por_extensao
# Descrição:
#   Percorre os arquivos do diretório e soma a quantidade por extensão.
# Parâmetros:
#   $1 -> Caminho do diretório.
# ------------------------------------------------------------------------------
contar_por_extensao() {
    local diretorio="$1"
    local arquivo
    local extensao
    declare -A contadores=()

    while IFS= read -r -d '' arquivo; do
        extensao="$(obter_extensao "$arquivo")"
        ((contadores["$extensao"]++))
    done < <(find "$diretorio" -maxdepth 1 -type f -print0)

    for extensao in "${!contadores[@]}"; do
        echo "${extensao}: ${contadores[$extensao]} arquivo(s)"
    done | sort
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-}"

    validar_diretorio "$diretorio"
    contar_por_extensao "$diretorio"
}

main "${1:-}"
