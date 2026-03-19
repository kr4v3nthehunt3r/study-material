#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: localizar_ips_em_arquivos.sh
# Descrição do módulo:
#   Procura padrões de endereços IPv4 em arquivos de um diretório, exibindo
#   quantos IPs foram encontrados por arquivo.
#
# Uso:
#   ./localizar_ips_em_arquivos.sh [diretorio]
# ==============================================================================

set -o nounset
set -o pipefail

REGEX_IP='([0-9]{1,3}\.){3}[0-9]{1,3}'

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
# Função: contar_ips_por_arquivo
# Descrição:
#   Varre recursivamente os arquivos legíveis do diretório e informa quantos
#   padrões IPv4 foram encontrados em cada um.
# Parâmetros:
#   $1 -> Caminho do diretório.
# ------------------------------------------------------------------------------
contar_ips_por_arquivo() {
    local diretorio="$1"
    local arquivo
    local quantidade

    while IFS= read -r -d '' arquivo; do
        [[ ! -r "$arquivo" ]] && continue

        quantidade=$(grep -Eo "$REGEX_IP" "$arquivo" 2>/dev/null | wc -l)

        if (( quantidade > 0 )); then
            echo "$arquivo ($quantidade IP(s))"
        fi
    done < <(find "$diretorio" -type f -print0)
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-.}"

    validar_diretorio "$diretorio"
    contar_ips_por_arquivo "$diretorio"
}

main "${1:-}"
