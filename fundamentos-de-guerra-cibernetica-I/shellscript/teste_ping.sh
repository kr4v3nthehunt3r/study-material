#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: teste_ping.sh
# Descrição do módulo:
#   Executa um teste simples de conectividade com o comando ping, exibindo as
#   respostas recebidas e o resumo estatístico ao final da execução.
#
# Objetivos do módulo:
#   - Validar o host informado e a quantidade de testes;
#   - Verificar a presença do comando ping;
#   - Executar o teste de conectividade;
#   - Exibir apenas as linhas mais relevantes do resultado.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

HOST="${1:-}"
QUANTIDADE="${2:-3}"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Mostra ao usuário a forma correta de executar o script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <host_ou_ip> [quantidade]"
    echo "Exemplo: $0 8.8.8.8 3"
}

# ------------------------------------------------------------------------------
# Função: validar_quantidade
# Descrição:
#   Verifica se a quantidade informada é um número inteiro positivo.
# Parâmetros:
#   $1 -> Quantidade informada.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_quantidade() {
    local quantidade="$1"

    if ! [[ "$quantidade" =~ ^[1-9][0-9]*$ ]]; then
        echo "[ERRO] A quantidade de testes deve ser um inteiro positivo." >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: validar_dependencia_ping
# Descrição:
#   Confere se o comando ping está disponível no sistema.
# Parâmetros:
#   Nenhum.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_dependencia_ping() {
    if ! command -v ping >/dev/null 2>&1; then
        echo "[ERRO] O comando 'ping' não está disponível no sistema." >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: executar_ping
# Descrição:
#   Executa o teste de ping e filtra as linhas mais relevantes da saída.
# Parâmetros:
#   $1 -> Host ou IP de destino.
#   $2 -> Quantidade de pacotes.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
executar_ping() {
    local host="$1"
    local quantidade="$2"

    ping -c "$quantidade" "$host" 2>/dev/null \
        | grep -E 'bytes from|from |min/avg/max|packets transmitted|round-trip|rtt'
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
    if [[ -z "$HOST" ]]; then
        exibir_uso >&2
        exit 1
    fi

    validar_quantidade "$QUANTIDADE"
    validar_dependencia_ping
    executar_ping "$HOST" "$QUANTIDADE"
}

principal
