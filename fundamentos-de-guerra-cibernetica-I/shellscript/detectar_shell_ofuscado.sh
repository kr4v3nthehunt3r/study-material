#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: detectar_shell_ofuscado.sh
# Descrição do módulo:
#   Procura padrões suspeitos de ofuscação ou execução dinâmica em scripts shell,
#   gerando um relatório com as ocorrências encontradas.
#
# Uso:
#   ./detectar_shell_ofuscado.sh [diretorio] [arquivo_relatorio]
# ==============================================================================

set -o nounset
set -o pipefail

PADROES_SUSPEITOS=(
    "eval"
    "base64"
    "xxd"
    "perl -e"
    "python -c"
    "shc"
    "exec"
    "xor"
    "openssl"
)

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Garante que o diretório informado exista.
# Parâmetros:
#   $1 -> Caminho do diretório a ser analisado.
# ------------------------------------------------------------------------------
validar_diretorio() {
    local diretorio="$1"

    if [[ ! -d "$diretorio" ]]; then
        echo "Erro: o diretório '$diretorio' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: montar_argumentos_grep
# Descrição:
#   Monta dinamicamente os argumentos -e do grep a partir da lista de padrões.
# ------------------------------------------------------------------------------
montar_argumentos_grep() {
    local padrao

    for padrao in "${PADROES_SUSPEITOS[@]}"; do
        printf '%s\n' "-e" "$padrao"
    done
}

# ------------------------------------------------------------------------------
# Função: analisar_scripts
# Descrição:
#   Varre scripts .sh e grava em relatório as correspondências encontradas.
# Parâmetros:
#   $1 -> Diretório a ser analisado.
#   $2 -> Arquivo de relatório.
# ------------------------------------------------------------------------------
analisar_scripts() {
    local diretorio="$1"
    local relatorio="$2"
    local -a args_grep=()

    mapfile -t args_grep < <(montar_argumentos_grep)

    {
        echo "Relatório de padrões suspeitos em scripts shell"
        echo "Diretório analisado: $diretorio"
        echo "------------------------------------------------------------"
    } > "$relatorio"

    if find "$diretorio" -type f -name "*.sh" -exec grep -Hni "${args_grep[@]}" {} + | tee -a "$relatorio"; then
        echo "Relatório salvo em: $relatorio"
    else
        echo "Nenhum padrão suspeito foi encontrado." | tee -a "$relatorio"
        echo "Relatório salvo em: $relatorio"
    fi
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-.}"
    local relatorio="${2:-scripts_suspeitos.log}"

    validar_diretorio "$diretorio"
    analisar_scripts "$diretorio" "$relatorio"
}

main "${1:-}" "${2:-}"
