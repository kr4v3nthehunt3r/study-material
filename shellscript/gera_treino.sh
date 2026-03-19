#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: gera_treino.sh
# Descrição do módulo:
#   Cria um diretório de treinamento e gera arquivos de texto preenchidos com
#   números aleatórios. A quantidade de arquivos e a quantidade de linhas por
#   arquivo podem ser personalizadas por parâmetros.
#
# Objetivos do módulo:
#   - Validar parâmetros numéricos;
#   - Criar o diretório de saída, se necessário;
#   - Gerar arquivos de texto automaticamente;
#   - Exibir um resumo final da geração.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

DIRETORIO="${1:-treinamento}"
QUANTIDADE_ARQUIVOS="${2:-10}"
LINHAS_POR_ARQUIVO="${3:-50}"

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Mostra ao usuário o formato esperado para execução do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 [diretorio] [quantidade_arquivos] [linhas_por_arquivo]"
    echo "Exemplo: $0 treinamento 10 50"
}

# ------------------------------------------------------------------------------
# Função: validar_inteiro_positivo
# Descrição:
#   Verifica se o valor informado é um número inteiro positivo.
# Parâmetros:
#   $1 -> Valor a ser validado.
#   $2 -> Nome lógico do campo validado.
# Retorno:
#   0 em caso de sucesso. Encerra o script em caso de erro.
# ------------------------------------------------------------------------------
validar_inteiro_positivo() {
    local valor="$1"
    local nome_campo="$2"

    if ! [[ "$valor" =~ ^[1-9][0-9]*$ ]]; then
        echo "[ERRO] $nome_campo deve ser um inteiro positivo." >&2
        exit 1
    fi
}

# ------------------------------------------------------------------------------
# Função: preparar_diretorio
# Descrição:
#   Cria o diretório de saída, caso ele ainda não exista.
# Parâmetros:
#   $1 -> Caminho do diretório.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
preparar_diretorio() {
    local diretorio="$1"
    mkdir -p "$diretorio"
}

# ------------------------------------------------------------------------------
# Função: gerar_arquivo_aleatorio
# Descrição:
#   Gera um arquivo de texto contendo uma quantidade definida de números
#   aleatórios, um por linha.
# Parâmetros:
#   $1 -> Caminho do arquivo a ser gerado.
#   $2 -> Quantidade de linhas a serem criadas.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
gerar_arquivo_aleatorio() {
    local arquivo="$1"
    local linhas="$2"
    local indice_linha=0

    : > "$arquivo"

    for ((indice_linha = 1; indice_linha <= linhas; indice_linha++)); do
        echo "$RANDOM" >> "$arquivo"
    done
}

# ------------------------------------------------------------------------------
# Função: gerar_conjunto_arquivos
# Descrição:
#   Controla a criação de todos os arquivos solicitados pelo usuário.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
gerar_conjunto_arquivos() {
    local indice_arquivo=0
    local arquivo_atual=""

    echo "[INFO] Gerando arquivos em: $DIRETORIO"

    for ((indice_arquivo = 1; indice_arquivo <= QUANTIDADE_ARQUIVOS; indice_arquivo++)); do
        arquivo_atual="$DIRETORIO/arquivo_${indice_arquivo}.txt"
        gerar_arquivo_aleatorio "$arquivo_atual" "$LINHAS_POR_ARQUIVO"
        echo "[OK] Criado: $arquivo_atual"
    done
}

# ------------------------------------------------------------------------------
# Função: exibir_resumo
# Descrição:
#   Exibe um resumo com os arquivos gerados no diretório de destino.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_resumo() {
    echo
    echo "[RESUMO] Conteúdo gerado com sucesso."
    ls -lh "$DIRETORIO"
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
    validar_inteiro_positivo "$QUANTIDADE_ARQUIVOS" "A quantidade de arquivos"
    validar_inteiro_positivo "$LINHAS_POR_ARQUIVO" "A quantidade de linhas por arquivo"
    preparar_diretorio "$DIRETORIO"
    gerar_conjunto_arquivos
    exibir_resumo
}

principal
