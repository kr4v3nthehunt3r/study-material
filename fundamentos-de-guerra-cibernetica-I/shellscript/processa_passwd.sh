#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: processa_passwd.sh
# Descrição do módulo:
#   Processa um arquivo no formato semelhante ao /etc/passwd. O script identifica
#   linhas contendo a palavra "false", lista os nomes de usuário e calcula a
#   soma dos UIDs presentes na terceira coluna.
#
# Objetivos do módulo:
#   - Validar o arquivo de entrada;
#   - Exibir linhas com a palavra "false";
#   - Listar usuários da primeira coluna;
#   - Somar os UIDs numéricos da terceira coluna.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

ARQUIVO="${1:-exercicio8.txt}"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Mostra ao usuário como executar o script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 [arquivo]"
    echo "Exemplo: $0 exercicio8.txt"
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo
# Descrição:
#   Verifica se o arquivo informado existe e pode ser lido.
# Parâmetros:
#   $1 -> Caminho do arquivo.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_arquivo() {
    local arquivo="$1"

    if [[ ! -f "$arquivo" ]]; then
        echo "[ERRO] Arquivo não encontrado: $arquivo" >&2
        exit 1
    fi

    if [[ ! -r "$arquivo" ]]; then
        echo "[ERRO] Sem permissão de leitura no arquivo: $arquivo" >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: exibir_linhas_false
# Descrição:
#   Mostra as linhas do arquivo que contêm a palavra "false".
# Parâmetros:
#   $1 -> Caminho do arquivo.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_linhas_false() {
    local arquivo="$1"

    echo "[1] Linhas contendo a palavra 'false':"
    grep -n "false" "$arquivo" || echo "Nenhuma linha encontrada."
    echo
}

# ------------------------------------------------------------------------------
# Função: exibir_usuarios
# Descrição:
#   Lista os nomes de usuário presentes na primeira coluna do arquivo.
# Parâmetros:
#   $1 -> Caminho do arquivo.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_usuarios() {
    local arquivo="$1"

    echo "[2] Usuários (primeira coluna):"
    cut -d ':' -f 1 "$arquivo"
    echo
}

# ------------------------------------------------------------------------------
# Função: exibir_soma_uids
# Descrição:
#   Soma os valores numéricos presentes na terceira coluna do arquivo.
# Parâmetros:
#   $1 -> Caminho do arquivo.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_soma_uids() {
    local arquivo="$1"

    echo "[3] Soma dos UIDs (terceira coluna):"
    awk -F ':' 'BEGIN {soma=0} NF >= 3 && $3 ~ /^[0-9]+$/ {soma += $3} END {print soma}' "$arquivo"
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Organiza a sequência principal de execução do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    validar_arquivo "$ARQUIVO"
    exibir_linhas_false "$ARQUIVO"
    exibir_usuarios "$ARQUIVO"
    exibir_soma_uids "$ARQUIVO"
}

principal
