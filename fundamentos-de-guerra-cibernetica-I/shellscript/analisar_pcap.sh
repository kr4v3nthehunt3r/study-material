#!/bin/bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: analisar_pcap.sh
# Descrição do módulo:
#   Executa análise de um arquivo PCAP utilizando ferramentas disponíveis no
#   ambiente, como Zeek, Suricata, TShark e YARA. Cada etapa só é executada se
#   a respectiva ferramenta estiver instalada.
#
# Uso:
#   ./analisar_pcap.sh <arquivo.pcap> [diretorio_saida]
# ==============================================================================

set -o nounset
set -o pipefail

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de uso do script.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <arquivo.pcap> [diretorio_saida]"
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo_pcap
# Descrição:
#   Valida a existência do arquivo PCAP informado.
# Parâmetros:
#   $1 -> Caminho do arquivo PCAP.
# ------------------------------------------------------------------------------
validar_arquivo_pcap() {
    local arquivo_pcap="$1"

    if [[ -z "$arquivo_pcap" ]]; then
        echo "Erro: informe o arquivo PCAP."
        exibir_uso
        exit 1
    fi

    if [[ ! -f "$arquivo_pcap" ]]; then
        echo "Erro: o arquivo '$arquivo_pcap' não existe."
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: executar_zeek
# Descrição:
#   Processa o PCAP com Zeek, caso a ferramenta esteja disponível.
# Parâmetros:
#   $1 -> Arquivo PCAP.
#   $2 -> Diretório de saída.
# ------------------------------------------------------------------------------
executar_zeek() {
    local arquivo_pcap="$1"
    local diretorio_saida="$2"

    if command -v zeek >/dev/null 2>&1; then
        zeek -r "$arquivo_pcap" > "$diretorio_saida/zeek.log" 2>&1
        echo "Zeek: análise concluída."
    else
        echo "Zeek: não instalado; etapa ignorada."
    fi
}

# ------------------------------------------------------------------------------
# Função: executar_suricata
# Descrição:
#   Processa o PCAP com Suricata, caso a ferramenta esteja disponível.
# Parâmetros:
#   $1 -> Arquivo PCAP.
#   $2 -> Diretório de saída.
# ------------------------------------------------------------------------------
executar_suricata() {
    local arquivo_pcap="$1"
    local diretorio_saida="$2"

    if command -v suricata >/dev/null 2>&1; then
        mkdir -p "$diretorio_saida/suricata"
        suricata -r "$arquivo_pcap" -l "$diretorio_saida/suricata" >/dev/null 2>&1
        echo "Suricata: análise concluída."
    else
        echo "Suricata: não instalado; etapa ignorada."
    fi
}

# ------------------------------------------------------------------------------
# Função: executar_tshark
# Descrição:
#   Filtra portas específicas com TShark, caso disponível.
# Parâmetros:
#   $1 -> Arquivo PCAP.
#   $2 -> Diretório de saída.
# ------------------------------------------------------------------------------
executar_tshark() {
    local arquivo_pcap="$1"
    local diretorio_saida="$2"

    if command -v tshark >/dev/null 2>&1; then
        tshark -r "$arquivo_pcap" -Y "tcp.port==4444 || tcp.port==3389 || tcp.port==8080" > "$diretorio_saida/portas_interesse.log" 2>/dev/null
        echo "TShark: filtro aplicado com sucesso."
    else
        echo "TShark: não instalado; etapa ignorada."
    fi
}

# ------------------------------------------------------------------------------
# Função: executar_yara
# Descrição:
#   Executa YARA caso a ferramenta e a regra local estejam disponíveis.
# Parâmetros:
#   $1 -> Arquivo PCAP.
#   $2 -> Diretório de saída.
# ------------------------------------------------------------------------------
executar_yara() {
    local arquivo_pcap="$1"
    local diretorio_saida="$2"
    local regra_yara="./r.yar"

    if command -v yara >/dev/null 2>&1 && [[ -f "$regra_yara" ]]; then
        yara -r "$regra_yara" "$arquivo_pcap" > "$diretorio_saida/yara.log" 2>&1
        echo "YARA: verificação concluída."
    else
        echo "YARA: não instalado ou regra './r.yar' ausente; etapa ignorada."
    fi
}

# ------------------------------------------------------------------------------
# Função: main
# Descrição:
#   Coordena o fluxo principal do script.
# ------------------------------------------------------------------------------
main() {
    local arquivo_pcap="${1:-}"
    local diretorio_saida="${2:-./logs_ana}"

    validar_arquivo_pcap "$arquivo_pcap"
    mkdir -p "$diretorio_saida"

    executar_zeek "$arquivo_pcap" "$diretorio_saida"
    executar_suricata "$arquivo_pcap" "$diretorio_saida"
    executar_tshark "$arquivo_pcap" "$diretorio_saida"
    executar_yara "$arquivo_pcap" "$diretorio_saida"

    echo "Arquivos de saída disponíveis em: $diretorio_saida"
}

main "${1:-}" "${2:-}"
