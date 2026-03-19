#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: valida_backup.sh
# Descrição do módulo:
#   Valida um diretório informado e verifica se um arquivo existe dentro dele.
#   Se o arquivo já existir, cria uma cópia de backup com timestamp. Caso o
#   arquivo não exista, cria um novo arquivo vazio no caminho especificado.
#
# Objetivos do módulo:
#   - Ler e validar entradas do usuário;
#   - Montar o caminho completo do arquivo;
#   - Criar backup de arquivos já existentes;
#   - Criar arquivo novo quando ele ainda não existir.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

DIRETORIO="${1:-}"
ARQUIVO="${2:-}"
CAMINHO_COMPLETO=""
TIMESTAMP=""

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a sintaxe de uso do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 [diretorio] [arquivo]"
    echo "Exemplo: $0 /tmp exemplo.txt"
}

# ------------------------------------------------------------------------------
# Função: ler_entradas_interativas
# Descrição:
#   Solicita ao usuário diretório e nome do arquivo quando não informados na
#   linha de comando.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
ler_entradas_interativas() {
    if [[ -z "$DIRETORIO" ]]; then
        read -r -p "Informe o diretório: " DIRETORIO
    fi

    if [[ -z "$ARQUIVO" ]]; then
        read -r -p "Informe o nome do arquivo: " ARQUIVO
    fi
}

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Verifica se o diretório informado existe e é válido.
# Parâmetros:
#   $1 -> Caminho do diretório.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_diretorio() {
    local diretorio="$1"

    if [[ ! -d "$diretorio" ]]; then
        echo "[ERRO] Diretório inválido: $diretorio" >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: montar_caminho_arquivo
# Descrição:
#   Monta o caminho absoluto do arquivo a partir do diretório e do nome
#   informados pelo usuário.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
montar_caminho_arquivo() {
    CAMINHO_COMPLETO="${DIRETORIO%/}/${ARQUIVO}"
    TIMESTAMP="$(date +%Y%m%d%H%M%S)"
}

# ------------------------------------------------------------------------------
# Função: criar_backup_ou_arquivo
# Descrição:
#   Cria uma cópia de backup quando o arquivo já existe; caso contrário,
#   cria um novo arquivo vazio.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
criar_backup_ou_arquivo() {
    local backup=""

    if [[ -f "$CAMINHO_COMPLETO" ]]; then
        backup="${CAMINHO_COMPLETO}.bak.${TIMESTAMP}"
        cp -- "$CAMINHO_COMPLETO" "$backup"
        echo "[OK] Backup criado: $backup"
    else
        touch -- "$CAMINHO_COMPLETO"
        echo "[OK] Novo arquivo criado: $CAMINHO_COMPLETO"
    fi
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Executa o fluxo principal do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    ler_entradas_interativas

    if [[ -z "$DIRETORIO" || -z "$ARQUIVO" ]]; then
        exibir_uso >&2
        exit 1
    fi

    validar_diretorio "$DIRETORIO"
    montar_caminho_arquivo
    criar_backup_ou_arquivo
}

principal
