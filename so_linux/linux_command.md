# Comandos Linux em Tabelas

## 1) Informações do sistema

| Comando | Função |
|---|---|
| `uname -a` | Exibe informações completas do kernel e da arquitetura do sistema. |
| `cat /etc/os-release` | Mostra a distribuição Linux e sua versão. |
| `hostname` | Exibe o nome da máquina. |
| `uptime` | Mostra há quanto tempo o sistema está ligado e a carga média. |
| `free -h` | Exibe o uso de memória RAM e swap em formato legível. |
| `top` | Monitora processos e uso de recursos em tempo real. |
| `htop` | Versão interativa e mais amigável do `top`. |
| `lscpu` | Mostra informações detalhadas da CPU. |
| `lsusb` | Lista dispositivos conectados via USB. |
| `lspci` | Lista dispositivos conectados ao barramento PCI. |

## 2) Discos / HD

| Comando | Função |
|---|---|
| `df -h` | Mostra o uso de espaço em disco por partição. |
| `du -sh *` | Exibe o tamanho de arquivos e diretórios no local atual. |
| `lsblk` | Lista discos, partições e dispositivos de bloco. |
| `fdisk -l` | Lista partições dos discos. |
| `mount` | Mostra sistemas de arquivos montados. |
| `umount /mnt/ponto` | Desmonta um ponto de montagem. |
| `blkid` | Exibe UUID, tipo e metadados de partições. |
| `smartctl -a /dev/sda` | Mostra informações SMART do disco. |

## 3) Manipulação de arquivos

| Comando | Função |
|---|---|
| `cp origem destino` | Copia arquivos ou diretórios da origem para o destino. |
| `mv origem destino` | Move ou renomeia arquivos e diretórios. |
| `rm arquivo` | Remove um arquivo. |
| `rm -r pasta` | Remove diretórios e seu conteúdo recursivamente. |
| `touch arquivo` | Cria um arquivo vazio ou atualiza sua data de modificação. |
| `mkdir pasta` | Cria um diretório. |
| `ln -s alvo link` | Cria um link simbólico. |
| `less arquivo` | Abre um arquivo para leitura paginada. |
| `more arquivo` | Exibe o conteúdo do arquivo por páginas. |
| `head arquivo` | Mostra as primeiras linhas do arquivo. |
| `tail arquivo` | Mostra as últimas linhas do arquivo. |
| `tail -f arquivo.log` | Acompanha atualizações do arquivo em tempo real. |
| `grep 'palavra' arquivo` | Procura uma palavra ou padrão dentro do arquivo. |
| `wc -l arquivo` | Conta a quantidade de linhas do arquivo. |

## 4) Usuários e grupos

| Comando | Função |
|---|---|
| `whoami` | Mostra o usuário atual. |
| `id usuario` | Exibe UID, GID e grupos do usuário. |
| `adduser usuario` | Cria usuário com configuração mais amigável/interativa. |
| `useradd usuario` | Cria um usuário de forma direta. |
| `passwd usuario` | Define ou altera a senha do usuário. |
| `deluser usuario` | Remove um usuário. |
| `userdel usuario` | Exclui um usuário do sistema. |
| `groupadd grupo` | Cria um grupo. |
| `groups usuario` | Mostra os grupos aos quais o usuário pertence. |
| `usermod -aG grupo usuario` | Adiciona o usuário a um grupo suplementar. |

## 5) Permissões e propriedades

| Comando | Função |
|---|---|
| `chgrp grupo arquivo` | Altera o grupo proprietário do arquivo. |
| `stat arquivo` | Exibe detalhes completos do arquivo, como permissões, tamanho e timestamps. |

## 6) Processos

| Comando | Função |
|---|---|
| `ps aux` | Lista processos em execução. |
| `top` | Monitora processos em tempo real. |
| `htop` | Monitor interativo de processos. |
| `pgrep nome` | Busca o PID de um processo pelo nome. |
| `kill PID` | Envia sinal para encerrar um processo. |
| `kill -9 PID` | Força o encerramento imediato do processo. |
| `pkill nome` | Encerra processos pelo nome. |
| `jobs` | Lista tarefas em segundo plano da sessão atual. |
| `bg` | Retoma uma tarefa em segundo plano. |
| `fg` | Traz uma tarefa para o primeiro plano. |
| `nice` | Inicia um processo com prioridade ajustada. |
| `renice` | Altera a prioridade de um processo em execução. |

## 7) Pacotes e atualizações

| Comando | Função |
|---|---|
| `apt update` | Atualiza a lista de pacotes nos sistemas baseados em Debian/Ubuntu/Kali. |
| `apt upgrade` | Atualiza os pacotes instalados. |
| `apt install pacote` | Instala um pacote via APT. |
| `dnf update` | Atualiza pacotes em distribuições que usam DNF. |
| `yum install pacote` | Instala um pacote via YUM. |
| `dnf install pacote` | Instala um pacote via DNF. |
| `yum remove pacote` | Remove um pacote via YUM. |
| `dnf remove pacote` | Remove um pacote via DNF. |
| `rpm -qa` | Lista pacotes instalados em sistemas baseados em RPM. |

## 8) Redes

| Comando | Função |
|---|---|
| `ip a` | Exibe interfaces e endereços IP. |
| `ifconfig` | Mostra ou configura interfaces de rede. |
| `ping host` | Testa conectividade com outro host. |
| `traceroute host` | Mostra o caminho percorrido até o destino. |
| `netstat -tulnp` | Lista portas abertas e serviços em escuta. |
| `ss -tulwn` | Exibe sockets e portas em uso. |
| `nslookup dominio` | Consulta DNS de um domínio. |
| `dig dominio` | Realiza consulta DNS detalhada. |
| `curl url` | Faz requisições para URLs e APIs. |
| `wget url` | Baixa arquivos da web. |
| `scp origem destino` | Copia arquivos de forma segura via SSH. |
| `ssh usuario@host` | Conecta remotamente a um host via SSH. |

## 9) Compactação, sincronização e backup

| Comando | Função |
|---|---|
| `zip arquivo.zip arquivos` | Compacta arquivos em formato ZIP. |
| `unzip arquivo.zip` | Extrai arquivos ZIP. |
| `gzip arquivo` | Compacta um arquivo em formato GZ. |
| `gunzip arquivo.gz` | Descompacta arquivo GZ. |
| `rsync -av src/ dest/` | Sincroniza arquivos e diretórios preservando atributos. |
| `dd if=/dev/sda of=/caminho/backup.img` | Cria uma imagem/backup bruto de um disco. |

> Observação: a seção “Permissões e Propriedades” aparece parcialmente no PDF, então só foi possível transcrever com segurança os comandos visíveis.
