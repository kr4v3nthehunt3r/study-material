#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: analisar_base64.sh
# Descrição do módulo:
#   Procura arquivos que aparentam conter conteúdo em Base64, tenta decodificá-los
#   e busca uma expressão textual específica no conteúdo decodificado.
#
# Uso:
#   ./analisar_base64.sh [diretorio] [padrao_textual]
# ==============================================================================

set -o nounset
set -o pipefail

REGEX_B64='^[A-Za-z0-9+/=[:space:]]+$'

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Garante que o diretório informado exista.
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
# Função: analisar_arquivo
# Descrição:
#   Tenta decodificar um arquivo e verifica se o padrão desejado está presente.
# Parâmetros:
#   $1 -> Caminho do arquivo.
#   $2 -> Padrão a ser pesquisado.
# ------------------------------------------------------------------------------
analisar_arquivo() {
    local arquivo="$1"
    local padrao="$2"
    local temporario

    temporario="$(mktemp)"

    if base64 -d "$arquivo" > "$temporario" 2>/dev/null; then
        if grep -q -- "$padrao" "$temporario"; then
            echo "Padrão localizado em: $arquivo"
            grep -- "$padrao" "$temporario"
        fi
    fi

    rm -f -- "$temporario"
}

# ------------------------------------------------------------------------------
# Função: percorrer_arquivos
# Descrição:
#   Varre os arquivos do diretório e seleciona candidatos que aparentam conter
#   apenas caracteres compatíveis com Base64.
# Parâmetros:
#   $1 -> Diretório de análise.
#   $2 -> Padrão a ser pesquisado após a decodificação.
# ------------------------------------------------------------------------------
percorrer_arquivos() {
    local diretorio="$1"
    local padrao="$2"
    local arquivo

    while IFS= read -r -d '' arquivo; do
        [[ ! -r "$arquivo" ]] && continue

        if head -n 20 "$arquivo" | tr -d '\n' | grep -Eq "$REGEX_B64"; then
            analisar_arquivo "$arquivo" "$padrao"
        fi
    done < <(find "$diretorio" -maxdepth 1 -type f -print0)
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-.}"
    local padrao="${2:-ALVO PRIORITÁRIO}"

    validar_diretorio "$diretorio"
    percorrer_arquivos "$diretorio" "$padrao"
}

main "${1:-}" "${2:-}"
