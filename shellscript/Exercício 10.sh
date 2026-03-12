#!/bin/bash

# 1. Solicita as entradas do usuário
read -p "Informe o caminho do diretório (Ex: /home/user/): " DIR
read -p "Informe o nome do arquivo com extensão (Ex: notas.txt): " ARQ

# 2. Validação: Verifica se o diretório existe (-d)
if [ ! -d "$DIR" ]; then
    echo "Erro: Diretório não encontrado!"
    exit 1
fi

# 3. Validação: Verifica se o nome do arquivo contém caracteres inválidos
# Regex que permite apenas letras, números, pontos, hífens e underlines
if [[ ! "$ARQ" =~ ^[a-zA-Z0-9._-]+$ ]]; then
    echo "Erro: Nome de arquivo inválido!"
    exit 1
fi

CAMINHO_COMPLETO="${DIR%/}/${ARQ}"

# 4. Verifica a existência do arquivo e executa as ações
if [ -f "$CAMINHO_COMPLETO" ]; then
    echo "Arquivo encontrado!"
    
    # Ação A: Criar uma cópia de backup com timestamp
    BACKUP_NAME="${CAMINHO_COMPLETO}.bak.$(date +%Y%m%d%H%M)"
    cp "$CAMINHO_COMPLETO" "$BACKUP_NAME"
    echo "Ação A executada: Backup criado em $BACKUP_NAME"

else
    echo "Arquivo não encontrado!"
    
    # Ação B: Criar um novo arquivo vazio
    touch "$CAMINHO_COMPLETO"
    echo "Ação B executada: Novo arquivo vazio criado em $CAMINHO_COMPLETO"
fi