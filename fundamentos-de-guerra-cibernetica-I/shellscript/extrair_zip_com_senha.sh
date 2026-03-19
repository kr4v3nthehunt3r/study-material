#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: extrair_zip_com_senha.sh
# Descrição do módulo:
#   Extrai um arquivo ZIP protegido por senha, contabiliza quantos itens foram
#   extraídos e remove o diretório temporário ao final.
#
# Uso:
#   ./extrair_zip_com_senha.sh <arquivo.zip>
# ==============================================================================

set -o nounset
set -o pipefail

DIRETORIO_TEMPORARIO="./temp_ext"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de uso do script.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <arquivo.zip>"
}

# ------------------------------------------------------------------------------
# Função: validar_dependencia
# Descrição:
#   Verifica se o utilitário unzip está instalado.
# ------------------------------------------------------------------------------
validar_dependencia() {
    if ! command -v unzip >/dev/null 2>&1; then
        echo "Erro: o utilitário 'unzip' não está instalado."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo
# Descrição:
#   Garante que o arquivo ZIP exista.
# Parâmetros:
#   $1 -> Caminho do arquivo ZIP.
# ------------------------------------------------------------------------------
validar_arquivo() {
    local arquivo_zip="$1"

    if [[ -z "$arquivo_zip" ]]; then
        echo "Erro: informe o arquivo ZIP."
        exibir_uso
        exit 1
    fi

    if [[ ! -f "$arquivo_zip" ]]; then
        echo "Erro: o arquivo '$arquivo_zip' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: ler_senha
# Descrição:
#   Lê a senha sem exibi-la no terminal.
# ------------------------------------------------------------------------------
ler_senha() {
    local senha

    read -r -s -p "Informe a senha do arquivo ZIP: " senha
    echo
    echo "$senha"
}

# ------------------------------------------------------------------------------
# Função: extrair_arquivo_zip
# Descrição:
#   Extrai o conteúdo do ZIP em um diretório temporário.
# Parâmetros:
#   $1 -> Arquivo ZIP.
#   $2 -> Senha.
# ------------------------------------------------------------------------------
extrair_arquivo_zip() {
    local arquivo_zip="$1"
    local senha="$2"

    rm -rf "$DIRETORIO_TEMPORARIO"
    mkdir -p "$DIRETORIO_TEMPORARIO"

    if unzip -P "$senha" -o "$arquivo_zip" -d "$DIRETORIO_TEMPORARIO" >/dev/null 2>&1; then
        echo "Quantidade de itens extraídos: $(find "$DIRETORIO_TEMPORARIO" -mindepth 1 | wc -l)"
    else
        echo "Erro: falha ao extrair o arquivo. Verifique a senha informada."
    fi
}

# ------------------------------------------------------------------------------
# Função: limpar_temporario
# Descrição:
#   Remove o diretório temporário utilizado na extração.
# ------------------------------------------------------------------------------
limpar_temporario() {
    rm -rf "$DIRETORIO_TEMPORARIO"
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local arquivo_zip="${1:-}"
    local senha

    validar_dependencia
    validar_arquivo "$arquivo_zip"
    senha="$(ler_senha)"
    extrair_arquivo_zip "$arquivo_zip" "$senha"
    limpar_temporario
}

main "${1:-}"
