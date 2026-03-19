#!/usr/bin/env bash
# ==============================================================================
# Autor: Kr4v3n
# Arquivo: busca_coords.sh
# Descrição do módulo:
#   Procura coordenadas geográficas em formato decimal em arquivos de texto de
#   um diretório informado. Para cada ocorrência encontrada, o script exibe
#   o nome do arquivo e a linha correspondente.
#
# Objetivos do módulo:
#   - Validar o diretório de busca;
#   - Localizar arquivos legíveis no diretório;
#   - Pesquisar possíveis coordenadas geográficas;
#   - Exibir o resultado de forma organizada.
# ==============================================================================

set -o errexit
set -o nounset
set -o pipefail

DIRETORIO_BUSCA="${1:-.}"
REGEX_COORD='-?[0-9]{1,3}\.[0-9]{1,6},[[:space:]]*-?[0-9]{1,3}\.[0-9]{1,6}'
ENCONTROU=0

# ------------------------------------------------------------------------------
# Função: exibir_uso
# Descrição:
#   Exibe a forma correta de executar o script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_uso() {
    echo "Uso: $0 [diretorio]"
    echo "Exemplo: $0 ."
}

# ------------------------------------------------------------------------------
# Função: validar_diretorio
# Descrição:
#   Confere se o caminho informado corresponde a um diretório válido.
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
# Função: listar_arquivos_legiveis
# Descrição:
#   Lista, em formato nulo, os arquivos legíveis do diretório informado.
# Parâmetros:
#   $1 -> Caminho do diretório.
# Retorno:
#   Imprime a lista de arquivos na saída padrão.
# ------------------------------------------------------------------------------
listar_arquivos_legiveis() {
    local diretorio="$1"
    find "$diretorio" -maxdepth 1 -type f -readable -print0
}

# ------------------------------------------------------------------------------
# Função: arquivo_tem_coordenada
# Descrição:
#   Testa se um arquivo contém pelo menos uma ocorrência compatível com a
#   expressão regular de coordenadas.
# Parâmetros:
#   $1 -> Caminho do arquivo.
# Retorno:
#   0 se encontrar coordenadas; 1 caso contrário.
# ------------------------------------------------------------------------------
arquivo_tem_coordenada() {
    local arquivo="$1"
    grep -E -q -- "$REGEX_COORD" "$arquivo"
}

# ------------------------------------------------------------------------------
# Função: exibir_ocorrencias_arquivo
# Descrição:
#   Mostra o arquivo e as linhas em que coordenadas foram encontradas.
# Parâmetros:
#   $1 -> Caminho do arquivo.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_ocorrencias_arquivo() {
    local arquivo="$1"
    echo "[ARQUIVO] $arquivo"
    grep -En -- "$REGEX_COORD" "$arquivo"
    echo
}

# ------------------------------------------------------------------------------
# Função: processar_arquivos
# Descrição:
#   Percorre os arquivos do diretório e imprime apenas aqueles que contêm
#   coordenadas compatíveis com o padrão configurado.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
processar_arquivos() {
    local arquivo=""

    while IFS= read -r -d '' arquivo; do
        if arquivo_tem_coordenada "$arquivo"; then
            ENCONTROU=1
            exibir_ocorrencias_arquivo "$arquivo"
        fi
    done < <(listar_arquivos_legiveis "$DIRETORIO_BUSCA")
}

# ------------------------------------------------------------------------------
# Função: exibir_resultado_final
# Descrição:
#   Informa ao usuário quando nenhuma coordenada compatível foi encontrada.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
exibir_resultado_final() {
    if [[ "$ENCONTROU" -eq 0 ]]; then
        echo "[INFO] Nenhuma coordenada compatível foi encontrada em: $DIRETORIO_BUSCA"
    fi
}

# ------------------------------------------------------------------------------
# Função: principal
# Descrição:
#   Controla o fluxo principal de execução do script.
# Parâmetros:
#   Nenhum.
# Retorno:
#   Nenhum.
# ------------------------------------------------------------------------------
principal() {
    validar_diretorio "$DIRETORIO_BUSCA"
    processar_arquivos
    exibir_resultado_final
}

principal
