#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: inventario_rede.sh
# Descrição do módulo:
#   Realiza um inventário simples e autorizado de uma sub-rede IPv4 /24. O
#   script identifica hosts que respondem a ping e, quando o nmap estiver
#   disponível, consulta de forma conservadora as portas 22, 80 e 443.
#
# Objetivos do módulo:
#   - Validar o endereço IPv4 informado;
#   - Determinar o prefixo da rede /24;
#   - Testar a disponibilidade dos hosts com ping;
#   - Exibir portas abertas conhecidas quando nmap estiver disponível.
#
# Observação:
#   Utilize este script apenas em redes e ativos sob sua responsabilidade e
#   com autorização explícita.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

ALVO="${1:-}"
PREFIXO=""
NMAP_DISPONIVEL=0

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de execução do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <ip_da_subrede_ou_host>"
    echo "Exemplo: $0 192.168.0.10"
}

# ------------------------------------------------------------------------------
# Função: validar_ipv4
# Descrição:
#   Confere se o endereço informado está no formato IPv4 e se todos os octetos
#   estão dentro da faixa válida de 0 a 255.
# Parâmetros:
#   $1 -> Endereço IPv4 informado pelo usuário.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_ipv4() {
    local ip="$1"
    local o1=""
    local o2=""
    local o3=""
    local o4=""
    local octeto=""

    if [[ -z "$ip" ]]; then
        exibir_uso >&2
        exit 1
    fi

    if ! [[ "$ip" =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
        echo "[ERRO] Informe um IPv4 válido no formato x.x.x.x" >&2
        exit 1
    fi

    IFS='.' read -r o1 o2 o3 o4 <<< "$ip"

    for octeto in "$o1" "$o2" "$o3" "$o4"; do
        if (( octeto < 0 || octeto > 255 )); then
            echo "[ERRO] IPv4 fora da faixa válida: $ip" >&2
            exit 1
        fi
    done
}

# ------------------------------------------------------------------------------
# Função: validar_dependencias
# Descrição:
#   Verifica se o comando ping está disponível e registra se o nmap existe.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum. Encerra o script se o ping não estiver disponível.
# ------------------------------------------------------------------------------
validar_dependencias() {
    if ! command -v ping >/dev/null 2>&1; then
        echo "[ERRO] O comando 'ping' não está disponível." >&2
        exit 1
    fi

    if command -v nmap >/dev/null 2>&1; then
        NMAP_DISPONIVEL=1
    fi
}

# ------------------------------------------------------------------------------
# Função: definir_prefixo_rede
# Descrição:
#   Calcula o prefixo /24 a partir do IPv4 informado.
# Parâmetros:
#   $1 -> Endereço IPv4 informado pelo usuário.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
definir_prefixo_rede() {
    local ip="$1"
    PREFIXO="$(awk -F'.' '{print $1"."$2"."$3}' <<< "$ip")"
}

# ------------------------------------------------------------------------------
# Função: host_ativo
# Descrição:
#   Testa se um host responde a uma requisição de ping.
# Parâmetros:
#   $1 -> Endereço IPv4 do host.
# Retorno:
#   0 se o host responder; 1 caso contrário.
# ------------------------------------------------------------------------------
host_ativo() {
    local host="$1"
    ping -c 1 -W 1 "$host" >/dev/null 2>&1
}

# ------------------------------------------------------------------------------
# Função: exibir_portas_abertas
# Descrição:
#   Consulta, de forma conservadora, as portas 22, 80 e 443 do host informado
#   quando a ferramenta nmap estiver disponível.
# Parâmetros:
#   $1 -> Endereço IPv4 do host.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_portas_abertas() {
    local host="$1"

    if [[ "$NMAP_DISPONIVEL" -eq 1 ]]; then
        nmap -Pn -T2 -p 22,80,443 "$host" 2>/dev/null \
            | awk '/^[0-9]+\// && /open/ {print "  [PORTA] " $1 " " $3}'
    else
        echo "  [INFO] nmap não instalado; pulando verificação de portas."
    fi
}

# ------------------------------------------------------------------------------
# Função: varrer_rede
# Descrição:
#   Percorre os endereços da rede /24 e exibe os hosts que responderem ao ping.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
varrer_rede() {
    local indice_host=0
    local host=""

    echo "[INFO] Iniciando varredura autorizada na rede: ${PREFIXO}.0/24"

    for ((indice_host = 1; indice_host <= 254; indice_host++)); do
        host="${PREFIXO}.${indice_host}"

        if host_ativo "$host"; then
            echo "[ATIVO] $host"
            exibir_portas_abertas "$host"
        fi
    done
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Organiza o fluxo principal de execução do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    validar_ipv4 "$ALVO"
    validar_dependencias
    definir_prefixo_rede "$ALVO"
    varrer_rede
}

principal
