#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: filtra_uol.sh
# Descrição do módulo:
#   Lê um arquivo de entrada contendo endereços de e-mail, valida cada linha
#   e grava em um arquivo de saída apenas os e-mails pertencentes ao domínio
#   @uol.com.br.
#
# Objetivos do módulo:
#   - Validar parâmetros e existência do arquivo de entrada;
#   - Processar o conteúdo linha a linha;
#   - Filtrar somente e-mails válidos do domínio desejado;
#   - Exibir um resumo final da execução.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

ARQUIVO_ENTRADA="${1:-emails.txt}"
ARQUIVO_SAIDA="${2:-validos_uol.txt}"
REGEX_UOL='^[A-Za-z0-9._%+-]+@uol\.com\.br$'
TOTAL_VALIDOS=0
TOTAL_INVALIDOS=0

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de utilização do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 [arquivo_entrada] [arquivo_saida]"
    echo "Exemplo: $0 emails.txt validos_uol.txt"
}

# ------------------------------------------------------------------------------
# Função: validar_arquivo_entrada
# Descrição:
#   Verifica se o arquivo de entrada existe e se possui permissão de leitura.
# Parâmetros:
#   $1 -> Caminho do arquivo de entrada.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_arquivo_entrada() {
    local arquivo_entrada="$1"

    if [[ ! -f "$arquivo_entrada" ]]; then
        echo "[ERRO] Arquivo de entrada não encontrado: $arquivo_entrada" >&2
        exit 1
    fi

    if [[ ! -r "$arquivo_entrada" ]]; then
        echo "[ERRO] Sem permissão de leitura no arquivo: $arquivo_entrada" >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: normalizar_email
# Descrição:
#   Remove espaços em branco no início e no fim de uma linha recebida.
# Parâmetros:
#   $1 -> Conteúdo bruto da linha.
# Retorno:
#   Imprime o valor normalizado na saída padrão.
# ------------------------------------------------------------------------------
normalizar_email() {
    local email_bruto="$1"
    sed 's/^[[:space:]]*//;s/[[:space:]]*$//' <<< "$email_bruto"
}

# ------------------------------------------------------------------------------
# Função: email_uol_valido
# Descrição:
#   Testa se a string recebida corresponde a um e-mail válido do domínio UOL.
# Parâmetros:
#   $1 -> Endereço de e-mail.
# Retorno:
#   0 se for válido; 1 caso contrário.
# ------------------------------------------------------------------------------
email_uol_valido() {
    local email="$1"
    [[ "$email" =~ $REGEX_UOL ]]
}

# ------------------------------------------------------------------------------
# Função: processar_emails
# Descrição:
#   Percorre o arquivo de entrada linha a linha e grava no arquivo de saída
#   somente os e-mails válidos do domínio @uol.com.br.
# Parâmetros:
#   $1 -> Arquivo de entrada.
#   $2 -> Arquivo de saída.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
processar_emails() {
    local arquivo_entrada="$1"
    local arquivo_saida="$2"
    local email=""

    : > "$arquivo_saida"

    while IFS= read -r email || [[ -n "$email" ]]; do
        email="$(normalizar_email "$email")"

        [[ -z "$email" ]] && continue

        if email_uol_valido "$email"; then
            echo "$email" >> "$arquivo_saida"
            ((TOTAL_VALIDOS+=1))
        else
            ((TOTAL_INVALIDOS+=1))
        fi
    done < "$arquivo_entrada"
}

# ------------------------------------------------------------------------------
# Função: exibir_resumo
# Descrição:
#   Exibe um resumo com os totais de e-mails válidos e inválidos processados.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_resumo() {
    echo "[OK] E-mails válidos do domínio @uol.com.br salvos em: $ARQUIVO_SAIDA"
    echo "[INFO] Total válidos: $TOTAL_VALIDOS"
    echo "[INFO] Total ignorados/inválidos: $TOTAL_INVALIDOS"
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Coordena o fluxo principal de execução do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    validar_arquivo_entrada "$ARQUIVO_ENTRADA"
    processar_emails "$ARQUIVO_ENTRADA" "$ARQUIVO_SAIDA"
    exibir_resumo
}

principal
