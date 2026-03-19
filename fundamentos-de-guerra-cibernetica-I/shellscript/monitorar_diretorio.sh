#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: monitorar_diretorio.sh
# Descrição do módulo:
#   Monitora um diretório em tempo real usando inotifywait e informa eventos de
#   criação, remoção e movimentação de arquivos.
#
# Uso:
#   ./monitorar_diretorio.sh [diretorio]
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: validar_dependencia
# Descrição:
#   Verifica se o utilitário inotifywait está instalado.
# ------------------------------------------------------------------------------
validar_dependencia() {
    if ! command -v inotifywait >/dev/null 2>&1; then
        echo "Erro: o utilitário 'inotifywait' não está instalado."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Garante que o diretório informado exista.
# Parâmetros:
#   $1 -> Caminho do diretório a ser monitorado.
# ------------------------------------------------------------------------------
validar_diretorio() {
    local diretorio="$1"

    if [[ ! -d "$diretorio" ]]; then
        echo "Erro: o diretório '$diretorio' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: monitorar_eventos
# Descrição:
#   Monitora eventos de criação, exclusão e movimentação no diretório.
# Parâmetros:
#   $1 -> Caminho do diretório a ser monitorado.
# ------------------------------------------------------------------------------
monitorar_eventos() {
    local diretorio="$1"

    echo "[+] Monitorando diretório: $diretorio"

    inotifywait -m -e create,delete,move --format '%e|%w%f' "$diretorio" 2>/dev/null | while IFS='|' read -r evento caminho; do
        echo "[Evento: $evento] $caminho"
    done
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local diretorio="${1:-.}"

    validar_dependencia
    validar_diretorio "$diretorio"
    monitorar_eventos "$diretorio"
}

main "${1:-}"
