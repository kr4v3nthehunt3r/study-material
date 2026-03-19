#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: localizar_credenciais_expostas.sh
# Descrição do módulo:
#   Procura, em arquivos de um diretório local, padrões textuais que podem
#   indicar exposição indevida de credenciais ou segredos. O objetivo é
#   defensivo: apoiar revisão de conteúdo em ambiente autorizado.
#
# Uso:
#   ./localizar_credenciais_expostas.sh [diretorio] [arquivo_relatorio]
# ==============================================================================

set -o nounset
set -o pipefail

PADROES_CREDENCIAIS=(
    "password="
    "senha="
    "pass:"
    "credenciais="
    "access_key="
    "secret_key="
)

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Garante que o diretório informado exista.
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
# Função: montar_argumentos_grep
# Descrição:
#   Constrói a lista de argumentos do grep com base nos padrões definidos.
# ------------------------------------------------------------------------------
montar_argumentos_grep() {
    local padrao

    for padrao in "${PADROES_CREDENCIAIS[@]}"; do
        printf '%s\n' "-e" "$padrao"
    done
}

# ------------------------------------------------------------------------------
# Função: analisar_arquivos
# Descrição:
#   Procura ocorrências suspeitas em arquivos de texto do diretório.
# Parâmetros:
#   $1 -> Diretório de análise.
#   $2 -> Arquivo de relatório.
# ------------------------------------------------------------------------------
analisar_arquivos() {
    local diretorio="$1"
    local relatorio="$2"
    local -a args_grep=()

    mapfile -t args_grep < <(montar_argumentos_grep)

    {
        echo "Relatório de possíveis credenciais expostas"
        echo "Diretório analisado: $diretorio"
        echo "------------------------------------------------------------"
    } > "$relatorio"

    if find "$diretorio" -type f -exec grep -IHni "${args_grep[@]}" {} + | tee -a "$relatorio"; then
        echo "Relatório salvo em: $relatorio"
    else
        echo "Nenhum padrão de credencial foi encontrado." | tee -a "$relatorio"
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
    local relatorio="${2:-credenciais_expostas.log}"

    validar_diretorio "$diretorio"
    analisar_arquivos "$diretorio" "$relatorio"
}

main "${1:-}" "${2:-}"
