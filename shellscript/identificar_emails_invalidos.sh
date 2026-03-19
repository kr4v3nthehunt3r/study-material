#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: identificar_emails_invalidos.sh
# Descrição do módulo:
#   Lê um arquivo texto contendo um e-mail por linha e grava em outro arquivo
#   apenas os endereços que não seguem um padrão básico de validação.
#
# Uso:
#   ./identificar_emails_invalidos.sh [arquivo_entrada] [arquivo_saida]
# ==============================================================================

set -o nounset
set -o pipefail

REGEX_EMAIL='^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

# ------------------------------------------------------------------------------
# Função: definir_arquivos
# Descrição:
#   Define os arquivos de entrada e saída, usando valores padrão quando
#   necessário.
# Parâmetros:
#   $1 -> Arquivo de entrada.
#   $2 -> Arquivo de saída.
# ------------------------------------------------------------------------------
definir_arquivos() {
    local entrada="${1:-emails.txt}"
    local saida="${2:-emails_invalidos.txt}"

    echo "$entrada;$saida"
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo_entrada
# Descrição:
#   Garante que o arquivo de entrada exista e possa ser lido.
# Parâmetros:
#   $1 -> Caminho do arquivo de entrada.
# ------------------------------------------------------------------------------
validar_arquivo_entrada() {
    local arquivo_entrada="$1"

    if [[ ! -f "$arquivo_entrada" ]]; then
        echo "Erro: o arquivo '$arquivo_entrada' não foi encontrado."
        exit 1
    fi

    if [[ ! -r "$arquivo_entrada" ]]; then
        echo "Erro: sem permissão de leitura em '$arquivo_entrada'."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: filtrar_invalidos
# Descrição:
#   Percorre o arquivo de entrada e grava apenas os e-mails inválidos no arquivo
#   de saída.
# Parâmetros:
#   $1 -> Arquivo de entrada.
#   $2 -> Arquivo de saída.
# ------------------------------------------------------------------------------
filtrar_invalidos() {
    local arquivo_entrada="$1"
    local arquivo_saida="$2"

    : > "$arquivo_saida"

    while IFS= read -r email || [[ -n "$email" ]]; do
        [[ -z "$email" ]] && continue

        if [[ ! "$email" =~ $REGEX_EMAIL ]]; then
            echo "$email" >> "$arquivo_saida"
        fi
    done < "$arquivo_entrada"

    echo "E-mails inválidos salvos em: $arquivo_saida"
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
    filtrar_invalidos "$arquivo_entrada" "$arquivo_saida"
}

main "${1:-}" "${2:-}"
