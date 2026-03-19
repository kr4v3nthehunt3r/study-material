#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: analisar_logs.sh
# Descrição do módulo:
#   Analisa um arquivo de log de texto para identificar IPs mais frequentes,
#   contar ocorrências de falha e separar registros ocorridos durante a
#   madrugada em um arquivo dedicado.
#
# Uso:
#   ./analisar_logs.sh <arquivo_log>
# ==============================================================================

set -o nounset
set -o pipefail

ARQUIVO_MADRUGADA="registros_madrugada.log"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de uso do script.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <arquivo_log>"
}

# ------------------------------------------------------------------------------
# Função: validar_entrada
# Descrição:
#   Verifica se o arquivo informado existe e possui permissão de leitura.
# Parâmetros:
#   $1 -> Caminho do arquivo de log.
# ------------------------------------------------------------------------------
validar_entrada() {
    local arquivo_log="$1"

    if [[ -z "$arquivo_log" ]]; then
        echo "Erro: informe o caminho de um arquivo de log."
        exibir_uso
        exit 1
    fi

    if [[ ! -f "$arquivo_log" ]]; then
        echo "Erro: o arquivo '$arquivo_log' não existe."
        exit 1
    fi

    if [[ ! -r "$arquivo_log" ]]; then
        echo "Erro: sem permissão de leitura no arquivo '$arquivo_log'."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: mostrar_top_ips
# Descrição:
#   Exibe os 5 IPs mais frequentes com base na primeira coluna do log.
# Parâmetros:
#   $1 -> Caminho do arquivo de log.
# ------------------------------------------------------------------------------
mostrar_top_ips() {
    local arquivo_log="$1"

    echo "Top 5 IPs mais frequentes:"
    awk '{print $1}' "$arquivo_log" \
        | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$' \
        | sort \
        | uniq -c \
        | sort -nr \
        | head -n 5
}

# ------------------------------------------------------------------------------
# Função: contar_falhas
# Descrição:
#   Conta quantas linhas possuem a palavra "falha", ignorando maiúsculas
#   e minúsculas.
# Parâmetros:
#   $1 -> Caminho do arquivo de log.
# ------------------------------------------------------------------------------
contar_falhas() {
    local arquivo_log="$1"
    local total_falhas

    total_falhas=$(grep -Eic 'falha' "$arquivo_log")
    echo "Quantidade de falhas encontradas: $total_falhas"
}

# ------------------------------------------------------------------------------
# Função: extrair_madrugada
# Descrição:
#   Salva em arquivo separado as linhas que contenham horário entre 00:00:00 e
#   03:59:59. A detecção depende de o horário estar presente na linha.
# Parâmetros:
#   $1 -> Caminho do arquivo de log.
# ------------------------------------------------------------------------------
extrair_madrugada() {
    local arquivo_log="$1"

    if grep -En '(^|[^0-9])(0[0-3]):[0-5][0-9](:[0-5][0-9])?([^0-9]|$)' "$arquivo_log" > "$ARQUIVO_MADRUGADA"; then
        echo "Registros de madrugada salvos em: $ARQUIVO_MADRUGADA"
    else
        : > "$ARQUIVO_MADRUGADA"
        echo "Nenhum registro de madrugada foi encontrado."
    fi
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local arquivo_log="${1:-}"

    validar_entrada "$arquivo_log"
    mostrar_top_ips "$arquivo_log"
    contar_falhas "$arquivo_log"
    extrair_madrugada "$arquivo_log"
}

main "${1:-}"
