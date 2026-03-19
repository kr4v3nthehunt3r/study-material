#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: filtrar_emails_uol.sh
# Descrição do módulo:
#   Lê um arquivo contendo um e-mail por linha e salva somente os endereços
#   pertencentes ao domínio @uol.com.br.
#
# Uso:
#   ./filtrar_emails_uol.sh [arquivo_entrada] [arquivo_saida]
# ==============================================================================

set -o nounset
set -o pipefail

REGEX_UOL='^[A-Za-z0-9._%+-]+@uol\.com\.br$'

# ------------------------------------------------------------------------------
# Função: definir_arquivos
# Descrição:
#   Define os arquivos de entrada e saída, com valores padrão quando omitidos.
# Parâmetros:
#   $1 -> Arquivo de entrada.
#   $2 -> Arquivo de saída.
# ------------------------------------------------------------------------------
definir_arquivos() {
    local entrada="${1:-emails.txt}"
    local saida="${2:-emails_uol_validos.txt}"

    echo "$entrada;$saida"
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo_entrada
# Descrição:
#   Valida a existência do arquivo de entrada.
# Parâmetros:
#   $1 -> Caminho do arquivo de entrada.
# ------------------------------------------------------------------------------
validar_arquivo_entrada() {
    local arquivo_entrada="$1"

    if [[ ! -f "$arquivo_entrada" ]]; then
        echo "Erro: o arquivo '$arquivo_entrada' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: filtrar_emails
# Descrição:
#   Filtra e salva apenas os e-mails do domínio @uol.com.br.
# Parâmetros:
#   $1 -> Arquivo de entrada.
#   $2 -> Arquivo de saída.
# ------------------------------------------------------------------------------
filtrar_emails() {
    local arquivo_entrada="$1"
    local arquivo_saida="$2"

    : > "$arquivo_saida"

    while IFS= read -r email || [[ -n "$email" ]]; do
        [[ -z "$email" ]] && continue

        if [[ "$email" =~ $REGEX_UOL ]]; then
            echo "$email" >> "$arquivo_saida"
        fi
    done < "$arquivo_entrada"

    echo "E-mails válidos do domínio UOL salvos em: $arquivo_saida"
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local arquivos
    local arquivo_entrada
    local arquivo_saida

    arquivos="$(definir_arquivos "${1:-}" "${2:-}")"
    arquivo_entrada="${arquivos%;*}"
    arquivo_saida="${arquivos#*;}"

    validar_arquivo_entrada "$arquivo_entrada"
    filtrar_emails "$arquivo_entrada" "$arquivo_saida"
}

main "${1:-}" "${2:-}"
