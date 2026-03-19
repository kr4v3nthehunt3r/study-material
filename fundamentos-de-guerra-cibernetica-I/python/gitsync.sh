#!/bin/bash

# Cores e Caminhos
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'
LOG_FILE="$HOME/.gitsync_history.log"
BACKUP_DIR="$HOME/GitBackups"

echo -e "${CYAN}=== Git Management System [Ultimate Shield] ===${NC}"

# --- FUNÇÃO: REGISTRAR LOG ---
log_action() {
    local status=$1
    local message=$2
    local repo=$(basename "$(pwd)")
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [REPO: $repo] [STATUS: $status] - $message" >> "$LOG_FILE"
}

# --- FUNÇÃO: BACKUP LOCAL ---
create_backup() {
    mkdir -p "$BACKUP_DIR"
    local repo_name=$(basename "$(pwd)")
    local backup_name="${repo_name}_$(date +'%Y%m%d_%H%M%S').tar.gz"
    echo -e "${YELLOW}[*] Criando backup local em $BACKUP_DIR...${NC}"
    tar --exclude='.git' -czf "$BACKUP_DIR/$backup_name" . 2>/dev/null
    log_action "BACKUP" "Backup criado: $backup_name"
}

# --- FUNÇÃO: CONFIGURAÇÃO GLOBAL ---
config_git() {
    git config --global pull.rebase false
    if [ -z "$(git config --global user.name)" ]; then
        read -p "Digite seu nome de usuário: " GIT_NAME
        read -p "Digite seu e-mail do GitHub: " GIT_EMAIL
        git config --global user.name "$GIT_NAME"
        git config --global user.email "$GIT_EMAIL"
    fi
}

# --- FUNÇÃO: VERIFICAÇÃO SSH ---
check_ssh() {
    SSH_KEY="$HOME/.ssh/id_ed25519"
    [ ! -f "$SSH_KEY" ] && ssh-keygen -t ed25519 -C "$(git config --global user.email)" -N "" -f "$SSH_KEY"
    eval "$(ssh-agent -s)" > /dev/null
    ssh-add "$SSH_KEY" 2>/dev/null

    if ! ssh -T -o ConnectTimeout=5 -o StrictHostKeyChecking=no git@github.com 2>&1 | grep -q "successfully authenticated"; then
        echo -e "${RED}[!] ERRO SSH! Adicione esta chave ao GitHub:${NC}"
        cat "${SSH_KEY}.pub"
        read -p "Aperte ENTER após adicionar..."
        check_ssh
    fi
}

# --- FUNÇÃO: SYNC ---
sync_repo() {
    [ ! -d .git ] && git init
    
    if [ -z "$(git remote get-url origin 2>/dev/null)" ]; then
        read -p "Nome do repositório no GitHub: " REPO_NAME
        git remote add origin "git@github.com:kr4v3nthehunt3r/${REPO_NAME}.git"
    fi

    git branch -M main
    git add .
    
    if ! git diff-index --quiet HEAD --; then
        read -p "Mensagem do commit: " MSG
        [ -z "$MSG" ] && MSG="auto-sync $(date +'%T')"
        git commit -m "$MSG"
    fi

    echo -e "${YELLOW}[*] Sincronizando...${NC}"
    if git push -u origin main 2>/dev/null; then
        echo -e "${GREEN}[V] Push realizado com sucesso!${NC}"
        log_action "SUCCESS" "Push concluído."
    else
        echo -e "${RED}[!] Conflito ou erro detectado.${NC}"
        echo -e "1) Forçar Push (Cria backup antes) | 2) Pull Automático | 3) Sair"
        read -p "Opção: " OPT
        case $OPT in
            1) 
                create_backup
                git push -f origin main && log_action "FORCE_PUSH" "Push forçado com backup."
                ;;
            2) 
                if git pull origin main --no-edit --allow-unrelated-histories; then
                    git push origin main
                    log_action "SUCCESS" "Pull e Push concluídos."
                else
                    log_action "ERROR" "Falha no Merge manual necessário."
                fi
                ;;
            *) exit ;;
        esac
    fi
}

# --- MENU ---
config_git
check_ssh

echo -e "\n${CYAN}MENU:${NC}"
echo -e "1) Sincronizar (Push/Pull)"
echo -e "2) Ver Logs de Atividade"
echo -e "3) Limpar Backups Antigos"
echo -e "4) Download (Clone) em /Downloads"
echo -e "5) Sair"
read -p "Opção: " MAIN_OPT

case $MAIN_OPT in
    1) sync_repo ;;
    2) [ -f "$LOG_FILE" ] && tail -n 15 "$LOG_FILE" || echo "Sem logs ainda." ;;
    3) rm -rf "$BACKUP_DIR"/* && echo "Backups limpos." ;;
    4) cd $HOME/Downloads && read -p "URL: " URL && git clone "$URL" ;;
    *) exit ;;
esac
