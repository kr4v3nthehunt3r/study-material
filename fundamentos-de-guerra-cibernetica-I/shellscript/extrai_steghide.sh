#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: extrai_steghide.sh
# Descrição do módulo:
#   Realiza a extração autorizada de conteúdo oculto com a ferramenta steghide
#   a partir de um arquivo fornecido pelo usuário. O script solicita a senha
#   de forma interativa e não executa tentativas automatizadas.
#
# Objetivos do módulo:
#   - Validar o arquivo alvo;
#   - Verificar a disponibilidade do comando steghide;
#   - Ler a senha com segurança;
#   - Executar a extração autorizada.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

ARQUIVO_ALVO="${1:-}"
SENHA=""

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Informa a forma correta de utilização do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 <arquivo_esteganografado>"
    echo "Exemplo: $0 imagem.jpg"
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo_alvo
# Descrição:
#   Verifica se o arquivo informado existe no sistema de arquivos.
# Parâmetros:
#   $1 -> Caminho do arquivo alvo.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_arquivo_alvo() {
    local arquivo_alvo="$1"

    if [[ -z "$arquivo_alvo" ]]; then
        exibir_uso >&2
        exit 1
    fi

    if [[ ! -f "$arquivo_alvo" ]]; then
        echo "[ERRO] Arquivo não encontrado: $arquivo_alvo" >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: validar_dependencia_steghide
# Descrição:
#   Confere se o comando steghide está instalado no sistema.
# Parâmetros:
#   Nenhum.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_dependencia_steghide() {
    if ! command -v steghide >/dev/null 2>&1; then
        echo "[ERRO] O comando 'steghide' não está instalado no sistema." >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: ler_senha
# Descrição:
#   Solicita a senha ao usuário sem exibir o valor digitado na tela.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
ler_senha() {
    read -r -s -p "Informe a senha autorizada para extração: " SENHA
    echo

    if [[ -z "$SENHA" ]]; then
        echo "[ERRO] Nenhuma senha foi informada." >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: extrair_conteudo
# Descrição:
#   Executa a extração do conteúdo oculto usando a senha informada pelo usuário.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum. Encerra o script em caso de falha na extração.
# ------------------------------------------------------------------------------
extrair_conteudo() {
    if steghide extract -sf "$ARQUIVO_ALVO" -p "$SENHA"; then
        echo "[OK] Extração concluída com sucesso."
    else
        echo "[ERRO] Não foi possível extrair o conteúdo com a senha fornecida." >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Orquestra a execução principal do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    validar_arquivo_alvo "$ARQUIVO_ALVO"
    validar_dependencia_steghide
    ler_senha
    extrair_conteudo
}

principal
