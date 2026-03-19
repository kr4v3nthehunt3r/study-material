#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: extrair_cves_csv.sh
# Descrição do módulo:
#   Lê um arquivo CSV simples e exibe as primeiras linhas de dados em formato
#   resumido. O script foi pensado para exercícios em que o CSV não possui
#   vírgulas escapadas ou estruturas complexas.
#
# Uso:
#   ./extrair_cves_csv.sh <arquivo.csv> <quantidade>
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de uso do script.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <arquivo.csv> <quantidade>"
}

# ------------------------------------------------------------------------------
# Função: validar_parametros
# Descrição:
#   Valida arquivo e quantidade solicitada.
# Parâmetros:
#   $1 -> Caminho do CSV.
#   $2 -> Quantidade de linhas a exibir.
# ------------------------------------------------------------------------------
validar_parametros() {
    local arquivo_csv="$1"
    local quantidade="$2"

    if [[ -z "$arquivo_csv" || -z "$quantidade" ]]; then
        echo "Erro: informe arquivo CSV e quantidade."
        exibir_uso
        exit 1
    fi

    if [[ ! -f "$arquivo_csv" ]]; then
        echo "Erro: o arquivo '$arquivo_csv' não existe."
        exit 1
    fi

    if [[ ! "$quantidade" =~ ^[0-9]+$ ]] || (( quantidade <= 0 )); then
        echo "Erro: a quantidade deve ser um inteiro maior que zero."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: exibir_registros
# Descrição:
#   Exibe até N registros do CSV, ignorando o cabeçalho. Esta rotina considera
#   um CSV simples separado por vírgula.
# Parâmetros:
#   $1 -> Caminho do CSV.
#   $2 -> Quantidade de linhas a exibir.
# ------------------------------------------------------------------------------
exibir_registros() {
    local arquivo_csv="$1"
    local quantidade="$2"
    local contador=0

    tail -n +2 "$arquivo_csv" | while IFS=',' read -r coluna1 nome severidade coluna4 coluna5 patch versao coluna8; do
        ((contador++))
        echo "[$contador] Nome: ${nome:-N/D} | Severidade: ${severidade:-N/D} | Patch: ${patch:-N/D} | Versão: ${versao:-N/D}"

        if (( contador >= quantidade )); then
            break
        fi
    done
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Controla o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local arquivo_csv="${1:-}"
    local quantidade="${2:-}"

    validar_parametros "$arquivo_csv" "$quantidade"
    exibir_registros "$arquivo_csv" "$quantidade"
}

main "${1:-}" "${2:-}"
