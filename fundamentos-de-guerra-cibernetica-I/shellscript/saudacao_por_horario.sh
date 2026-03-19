#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: saudacao_por_horario.sh
# Descrição do módulo:
#   Exibe uma saudação de acordo com a hora atual do sistema.
#
# Uso:
#   ./saudacao_por_horario.sh
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: obter_hora_atual
# Descrição:
#   Retorna a hora atual no formato de 24 horas.
# ------------------------------------------------------------------------------
obter_hora_atual() {
    date +%H
}

# ------------------------------------------------------------------------------
# Função: gerar_saudacao
# Descrição:
#   Define a saudação com base na hora informada.
# Parâmetros:
#   $1 -> Hora atual.
# ------------------------------------------------------------------------------
gerar_saudacao() {
    local hora="$1"

    if (( hora >= 6 && hora < 12 )); then
        echo "Bom dia!"
    elif (( hora >= 12 && hora < 18 )); then
        echo "Boa tarde!"
    else
        echo "Boa noite!"
    fi
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local hora_atual

    hora_atual="$(obter_hora_atual)"
    gerar_saudacao "$hora_atual"
}

main
