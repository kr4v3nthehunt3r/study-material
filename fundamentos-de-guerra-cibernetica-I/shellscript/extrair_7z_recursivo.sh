#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: extrair_7z_recursivo.sh
# Descrição do módulo:
#   Realiza a extração recursiva de arquivos .7z aninhados. Para cada arquivo,
#   tenta usar como senha o nome do arquivo sem a extensão, reproduzindo um
#   fluxo comum em laboratórios e exercícios controlados.
#
# Uso:
#   ./extrair_7z_recursivo.sh <arquivo_inicial.7z>
# ==============================================================================

set -o nounset
set -o pipefail

DIRETORIO_SAIDA="./saida_extracao_7z"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de uso do script.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <arquivo_inicial.7z>"
}

# ------------------------------------------------------------------------------
# Função: validar_dependencia
# Descrição:
#   Verifica se o comando 7z está disponível no sistema.
# ------------------------------------------------------------------------------
validar_dependencia() {
    if ! command -v 7z >/dev/null 2>&1; then
        echo "Erro: o utilitário '7z' não está instalado."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo_inicial
# Descrição:
#   Valida a existência do arquivo inicial informado pelo usuário.
# Parâmetros:
#   $1 -> Caminho do arquivo .7z inicial.
# ------------------------------------------------------------------------------
validar_arquivo_inicial() {
    local arquivo="$1"

    if [[ -z "$arquivo" ]]; then
        echo "Erro: informe o arquivo inicial .7z."
        exibir_uso
        exit 1
    fi

    if [[ ! -f "$arquivo" ]]; then
        echo "Erro: o arquivo '$arquivo' não foi encontrado."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: descobrir_proximo_7z
# Descrição:
#   Procura o próximo arquivo .7z dentro do diretório de saída e retorna apenas
#   o primeiro resultado encontrado.
# ------------------------------------------------------------------------------
descobrir_proximo_7z() {
    find "$DIRETORIO_SAIDA" -type f -name "*.7z" | sort | head -n 1
}

# ------------------------------------------------------------------------------
# Função: extrair_arquivo
# Descrição:
#   Extrai um arquivo .7z usando como senha o nome do arquivo sem extensão.
# Parâmetros:
#   $1 -> Caminho do arquivo .7z.
# ------------------------------------------------------------------------------
extrair_arquivo() {
    local arquivo="$1"
    local nome_base
    local senha

    nome_base="$(basename "$arquivo")"
    senha="${nome_base%.7z}"

    echo "Extraindo: $arquivo"
    echo "Senha testada: $senha"

    if ! 7z x "$arquivo" -p"$senha" -o"$DIRETORIO_SAIDA" -y >/dev/null 2>&1; then
        echo "Erro: não foi possível extrair '$arquivo' com a senha derivada."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: limpar_arquivo_extraido
# Descrição:
#   Remove o arquivo já processado para evitar reprocessamento.
# Parâmetros:
#   $1 -> Caminho do arquivo extraído.
# ------------------------------------------------------------------------------
limpar_arquivo_extraido() {
    local arquivo="$1"
    rm -f -- "$arquivo"
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Controla o fluxo principal de extração recursiva.
# ------------------------------------------------------------------------------
main() {
    local arquivo_atual="${1:-}"

    validar_dependencia
    validar_arquivo_inicial "$arquivo_atual"
    mkdir -p "$DIRETORIO_SAIDA"

    cp -f -- "$arquivo_atual" "$DIRETORIO_SAIDA/"

    arquivo_atual="$(find "$DIRETORIO_SAIDA" -maxdepth 1 -type f -name "*.7z" | sort | head -n 1)"

    while [[ -n "$arquivo_atual" && -f "$arquivo_atual" ]]; do
        extrair_arquivo "$arquivo_atual"
        limpar_arquivo_extraido "$arquivo_atual"
        arquivo_atual="$(descobrir_proximo_7z)"
    done

    echo "Extração concluída. Conteúdo final disponível em: $DIRETORIO_SAIDA"
}

main "${1:-}"
