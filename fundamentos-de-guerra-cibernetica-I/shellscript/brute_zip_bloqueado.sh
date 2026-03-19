#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: brute_zip_bloqueado.sh
# Descrição do módulo:
#   Este arquivo foi mantido apenas como registro de revisão. A automatização de
#   tentativas de senha contra arquivos protegidos não foi implementada nesta
#   versão.
#
# Uso:
#   ./brute_zip_bloqueado.sh
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: exibir_mensagem_bloqueio
# Descrição:
#   Informa que esta automação não está disponível nesta entrega.
# ------------------------------------------------------------------------------
exibir_mensagem_bloqueio() {
    echo "Este script não foi corrigido nem expandido nesta entrega."
    echo "Motivo: a automatização de tentativas de senha foi bloqueada."
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    exibir_mensagem_bloqueio
    exit 1
}

main
