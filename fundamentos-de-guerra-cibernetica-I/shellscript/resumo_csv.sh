#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: resumo_csv.sh
# Descrição do módulo:
#   Analisa um arquivo CSV contendo, nas três primeiras colunas, informações
#   como IP, método HTTP e URL. O script ignora o cabeçalho, agrupa linhas
#   repetidas e apresenta um resumo ordenado pela frequência.
#
# Objetivos do módulo:
#   - Validar o arquivo CSV de entrada;
#   - Remover cabeçalho e normalizar quebras de linha;
#   - Agrupar combinações repetidas das três primeiras colunas;
#   - Exibir um resumo ordenado por recorrência.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

ARQUIVO_CSV="${1:-}"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe o modo correto de utilização do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <arquivo_csv>"
    echo "Exemplo: $0 acessos.csv"
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo_csv
# Descrição:
#   Verifica se o arquivo CSV foi informado, existe e pode ser lido.
# Parâmetros:
#   $1 -> Caminho do arquivo CSV.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_arquivo_csv() {
    local arquivo_csv="$1"

    if [[ -z "$arquivo_csv" ]]; then
        exibir_uso >&2
        exit 1
    fi

    if [[ ! -f "$arquivo_csv" ]]; then
        echo "[ERRO] Arquivo não encontrado: $arquivo_csv" >&2
        exit 1
    fi

    if [[ ! -r "$arquivo_csv" ]]; then
        echo "[ERRO] Sem permissão de leitura em: $arquivo_csv" >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: gerar_resumo_csv
# Descrição:
#   Processa o CSV removendo o cabeçalho, mantendo apenas as três primeiras
#   colunas e agrupando entradas repetidas.
# Parâmetros:
#   $1 -> Caminho do arquivo CSV.
# Retorno:
#   Imprime o resumo na saída padrão.
# ------------------------------------------------------------------------------
gerar_resumo_csv() {
    local arquivo_csv="$1"

    tail -n +2 "$arquivo_csv" \
        | tr -d '\r' \
        | awk -F',' 'NF >= 3 {print $1 "," $2 "," $3}' \
        | sort \
        | uniq -c \
        | sort -nr
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Coordena a execução principal do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    validar_arquivo_csv "$ARQUIVO_CSV"
    gerar_resumo_csv "$ARQUIVO_CSV"
}

principal
