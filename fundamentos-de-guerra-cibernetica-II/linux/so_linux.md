# Resumo final 100% completo em tabelas — SO_Linux_2026_INTRO

## Identificação do material

| Campo | Conteúdo |
|---|---|
| Título do material | Sistema Operacional Linux |
| Instituição | Centro de Instrução de Guerra Eletrônica |
| Instrutor citado | 1º Ten Patrick |
| Total de páginas | 83 |
| Natureza do material | Apostila/apresentação introdutória de Linux com foco em estrutura do sistema, arquivos importantes, shell, comandos, variáveis de ambiente, rede, permissões, permissões especiais, permissões avançadas, `su`/`sudo` e localização de comandos |

## Mapa completo do PDF por páginas

| Páginas | Seção | Conteúdo principal |
|---|---|---|
| 1 | Capa | Identificação do curso/material |
| 2 | Apresentação | Slide de abertura |
| 3–4 | Objetivo | Objetivos gerais do conteúdo |
| 5–6 | Introdução | Conceito de sistema operacional e distribuições Linux |
| 7–9 | Conceitos | Onde o Linux pode ser encontrado |
| 10–22 | Arquivos importantes | Arquivos sensíveis e observações de segurança |
| 23–28 | Arquivos importantes | Estrutura de `/etc/passwd`, UIDs/GIDs, `/etc/shadow`, hashes e `/etc/group` |
| 29–30 | Shell | Conceito, papéis e dimensões do shell |
| 31 | Comandos | Estrutura de um comando, redirecionamento e operadores |
| 32–49 | Comandos | Lista de comandos e exemplos detalhados |
| 50 | Variáveis de ambiente | Variáveis essenciais do ambiente Unix/Linux |
| 51–59 | Gerência de rede | Ferramentas, exemplos e arquivos de configuração |
| 60–64 | Permissões | Modelo de permissões e `chmod` |
| 65–69 | Permissões especiais | SUID, SGID, Sticky Bit e busca por bits especiais |
| 70–73 | Permissões avançadas | `chattr`, atributos de sistema de arquivos e capabilities |
| 74–77 | su e sudo | Conceitos, comparação e regras em `/etc/sudoers` |
| 78–81 | whereis, which e locate | Localização de executáveis e arquivos |
| 82 | Conclusão | Encerramento |
| 83 | Capture The Flag | Referência ao ambiente Shellock Holmes |

## 1) Apresentação e objetivos

| Item | Resumo |
|---|---|
| Apresentação | A página 2 funciona como abertura formal da apresentação. |
| Objetivo geral | Conhecer a estrutura e os principais comandos do Linux. |
| Permissões e contas | Entender o funcionamento de permissões e contas de usuários. |
| Segurança do sistema | Conhecer aspectos relacionados à segurança do SO Linux. |
| Ferramentas de segurança | Utilizar ferramentas de segurança do Linux. |
| Temas avançados citados nos objetivos | Recuperação de senha de root, escape de shell restrito, envio de shell reverso e bind shell, escalação de privilégio e tunelamento com SSH. |
| Observação | A página 4 repete os objetivos com a marcação “EAD”. |

## 2) Introdução ao sistema operacional Linux

| Tópico | Resumo |
|---|---|
| Definição de sistema operacional | Conjunto de programas que, integrados como sistema, tornam os computadores operáveis. |
| Kernel | Responsável por abstrair o hardware, gerenciar acesso aos recursos e fornecer interface de programação. |
| Shell | Interface com o usuário e interpretador de comandos. |
| Utilitários do sistema | Programas usados para a execução de tarefas essenciais. |

## 3) Distribuições Linux

| Categoria mostrada | Exemplos exibidos no material |
|---|---|
| Desktop Linux | Ubuntu, Linux Mint, Fedora |
| Server Linux | Red Hat, Debian, CentOS |
| Embedded Linux | Raspberry Pi OS, Yocto Project |

## 4) Onde o Linux pode ser encontrado

| Ambiente/dispositivo citado | Observação |
|---|---|
| Smartphones Android | Exemplo de uso massivo em mobilidade |
| Roteadores de Internet | Uso em infraestrutura de rede |
| Smart TVs | Uso em eletrônicos de consumo |
| Dispositivos de streaming | Presença em appliances multimídia |
| Caixas de som inteligentes | Aplicação embarcada |
| E-readers | Dispositivos dedicados |
| Câmeras de segurança | Aplicação embarcada e de monitoramento |
| Sistemas automotivos | Aplicações em veículos |
| Drones | Uso em sistemas embarcados |
| Equipamentos de rede e servidores | Uso corporativo e de infraestrutura |
| Dispositivos médicos | Aplicações críticas |
| Relógios inteligentes | Aplicações móveis/embarcadas |
| Eletrodomésticos inteligentes | IoT |
| Servidores de imagens e impressoras multifuncionais | Equipamentos especializados |
| Câmeras digitais avançadas | Uso embarcado |
| Robôs domésticos | Automação residencial |
| TV boxes | Consumo multimídia |
| Consoles de videogame | Plataformas específicas |
| Sistemas de controle industrial | Ambientes industriais |

## 5) Arquivos importantes do sistema

| Arquivo/caminho | Função apresentada no material |
|---|---|
| `/etc/passwd` | Informações da conta do usuário |
| `/etc/shadow` | Informações da conta do usuário e hash de senha |
| `/etc/group` | Nomes dos grupos |
| `/etc/network/interfaces` | Configuração de rede |
| `/etc/netplan` | Pode armazenar arquivos de configuração de rede |
| `/etc/resolv.conf` | Configuração de DNS |
| `/home/<USER>/.bash_history` | Histórico do Bash do usuário |
| `~/.ssh/` | Armazenamento de chaves SSH |
| `/var/spool/cron` | Lista de arquivos cron (tarefas agendadas) |
| `/var/log/apache2/access.log` | Registro de conexão do Apache |
| `/etc/fstab` | Contém montagens locais e de rede/compartilhamentos configurados |

## 6) Observações de segurança sobre arquivos importantes

| Ponto | Resumo |
|---|---|
| Restrições de acesso | Muitos desses arquivos possuem permissões restritas e exigem privilégios de administrador para visualização ou alteração. |
| Importância operacional | São vitais para a operação do sistema. |
| Relevância em segurança | Podem ser alvo de monitoramento ou manipulação em cenários de segurança. |

## 7) Estrutura de `/etc/passwd`

| Campo | Significado no material |
|---|---|
| `aluno` | Nome do usuário/login |
| `x` | Indica que a senha criptografada está armazenada em `/etc/shadow` |
| `1001` (UID) | Identificador único do usuário |
| `1001` (GID) | Identificador do grupo principal do usuário |
| Campo GECOS | Informações adicionais, como nome completo, sala, telefones e outro campo livre |
| `/home/aluno` | Diretório home do usuário |
| `/bin/bash` | Shell padrão executado no login |

## 8) UIDs e GIDs

| Faixa/valor | Interpretação |
|---|---|
| `0` | Reservado ao root/superusuário |
| `1 a 999` | Normalmente reservado a usuários/grupos do sistema e serviços |
| `1000+` | Normalmente utilizado para usuários/grupos comuns |

## 9) Estrutura de `/etc/shadow`

| Campo/parte | Significado |
|---|---|
| Nome do usuário | Identifica a conta |
| Hash da senha | Senha criptografada; no exemplo, com yescrypt |
| Última troca | Quantidade de dias desde 1º de janeiro de 1970 até a última alteração |
| Mínimo de dias | Intervalo mínimo para alteração da senha |
| Máximo de dias | Intervalo máximo/expiração da senha |
| Aviso prévio | Quantos dias antes o usuário será avisado |
| Inactivity period | Campo que pode indicar período de inatividade |
| Expiration date | Campo que pode indicar data de expiração da conta |
| Reserved | Campo reservado para uso futuro |

## 10) Tipos de hash citados no material

| Algoritmo citado | Formato apresentado | Observação resumida no material |
|---|---|---|
| DES | `$1$salt$hashed_password` | Apresentado como antigo, fraco e obsoleto |
| MD5 | `$1$salt$hashed_password` | Apresentado como mais robusto que DES, mas inseguro |
| SHA-256 | `$5$salt$hashed_password` | Mais resistente que MD5 e DES |
| SHA-512 | `$6$salt$hashed_password` | Bastante seguro e recomendado |
| bcrypt | `$2a$cost$salt$hashed_password` | Inclui fator de custo ajustável |
| yescrypt | `$y$salt$hashed_password` | Algoritmo mais recente, resistente a força bruta |

## 11) Estrutura de `/etc/group`

| Campo | Significado |
|---|---|
| `group_name` | Nome do grupo |
| `password` | Campo historicamente usado para senha de grupo; hoje costuma ser `x` ou vazio |
| `GID` | Identificador único do grupo |
| `member_list` | Lista de membros do grupo |

## 12) O que é um shell

| Dimensão | Resumo |
|---|---|
| Conceito geral | Programa que fornece a interface pela qual o usuário executa comandos e, por extensão, a plataforma de operação construída ao redor dele |
| Interface usuário ↔ sistema | Comunicação via terminal, digitação de textos, convenções de sistema e chamadas de sistema |
| Interpretador de comandos | Separação de palavras, classificação de comandos, expansões e acionamento de mecanismos |
| Linguagem de programação | Linguagem estruturada para controlar execução, implementar procedimentos, scripts e funções |
| Plataforma | Operação no estilo Unix, fluxos de texto, pipes, redirecionamentos e utilitários da base do sistema |

## 13) Estrutura de um comando

| Componente | Conteúdo apresentado |
|---|---|
| Invocação | Executáveis, comandos internos ou funções |
| Argumentos | Vetor de parâmetros `ARGV[0] ... ARGV[N]`, representados por `$0`, `$1` ... `$N` |
| Redirecionamento de leitura | `<` |
| Redirecionamento de escrita | `>` e `>>` |
| Operador `;` | Execução incondicional e síncrona, um depois do outro |
| Operador `&` | Execução incondicional e assíncrona |
| Operador `&&` | Encadeamento condicional em caso de sucesso |
| Operador `||` | Encadeamento condicional em caso de erro |
| Operador `\|` | Pipe; conecta `stdout` do primeiro comando ao `stdin` do comando seguinte |

## 14) Lista geral de comandos úteis para gerência de arquivos

| Comando | Finalidade apresentada |
|---|---|
| `ls` | Listar conteúdo de diretório |
| `cd` | Alterar diretório atual |
| `cp` | Copiar |
| `mv` | Mover/renomear arquivos |
| `rm` | Remover/apagar arquivos |
| `mkdir` | Criar diretórios |
| `file` | Exibir tipo de um arquivo |
| `touch` | Criar arquivo ou alterar data/hora |
| `cat` | Ler conteúdo de arquivos |
| `grep` | Buscar e filtrar linhas por padrão |
| `less` | Ler conteúdo de arquivos com paginação |
| `head` | Ler as primeiras linhas |
| `tail` | Ler as últimas linhas |
| `find` | Localizar arquivos e diretórios com base em critérios |

## 15) Comando `ls`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `ls` |
| Intermediário | `ls -l`, `ls -a`, `ls -lh`, `ls -S`, `ls -1` |
| Avançado | `ls -lah /path/to/directory`, `ls -d`, `ls -R` |

## 16) Comando `cd`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `cd /caminho/do/diretório`, `cd diretório` |
| Intermediário | `cd ..`, `cd ~`, `cd` |
| Avançado | `cd ~/Documentos/Projetos`, `cd -`, `cd /`, `cd ~usuário` |

## 17) Comando `mv`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `mv arquivo.txt /caminho/do/destino` |
| Intermediário | `mv arquivo_antigo.txt arquivo_novo.txt`, `mv antigo_diretorio novo_diretório`, `mv /caminho/para/diretorio1 /novo/caminho/para/diretorio1`, `mv -i arquivo.txt /caminho/para/diretório` |
| Avançado | `mv arquivo1.txt arquivo2.txt arquivo3.txt /caminho/do/diretório`, `mv /diretorio/origem/* /caminho/do/diretório`, `mv -n arquivo.txt /caminho/para/diretório` |

## 18) Comando `rm`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `rm arquivo.txt` |
| Intermediário | `rm -i arquivo.txt`, `rm arquivo1.txt arquivo2.txt`, `rm -r /diretorio`, `rm /caminho/para/diretorio/*.log` |
| Avançado | `rm -rf /diretorio`, `rm arquivo.txt && echo "Arquivo removido com sucesso"` |

## 19) Comando `mkdir`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `mkdir novo_diretorio` |
| Intermediário | `mkdir novo_diretorio`, `mkdir -p /caminho/completo/novo_diretorio`, `mkdir dir1 dir2 dir3` |
| Avançado | `mkdir -m 755 novo_diretorio`, `mkdir -p projeto/{src,bin,doc/{info,man},lib}` |

## 20) Comando `file`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `file arquivo.txt` |
| Intermediário | `file arquivo1.txt arquivo2.pdf`, `file *`, `file /caminho/para/diretorio/*.jpg` |
| Avançado | `cat arquivo.txt | file -` |

## 21) Comando `touch`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `touch novo_arquivo.txt` |
| Intermediário | `touch -c arquivo_existente.txt`, `touch arquivos_novos.txt && ls -l arquivos_novos.txt`, `touch arquivo_criado.txt && chmod 600 arquivo_criado.txt` |
| Avançado | `touch -r arquivo_referencia.txt nome_do_arquivo.txt`, `touch -t 202407291200 arquivo.txt` |

## 22) Comando `cat`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `cat arquivo.txt` |
| Intermediário | `cat arquivo1.txt arquivo2.txt` |
| Avançado | `cat arquivo1.txt arquivo2.txt > combinado.txt`, `cat arquivo1.txt arquivo2.txt >> combinado.txt`, `cat > novo_arquivo.txt` |

## 23) Comando `grep`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `grep "padrão" arquivo.txt` |
| Intermediário | `grep -n "padrão" nome_do_arquivo.txt`, `grep "padrão" arquivo1.txt arquivo2.txt`, `grep -l "padrão" /caminho/para/diretorio/*`, `grep -v "padrão" nome_do_arquivo.txt`, `grep -o "padrão" nome_do_arquivo.txt` |
| Avançado | `grep -B 3 -A 2 "padrão" nome_do_arquivo.txt`, `grep -ri "padrão" /caminho/para/diretorio/` |

## 24) Comando `less`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `less arquivo.txt` |
| Intermediário | `comando | less`, `less -N nome_do_arquivo.txt`, `less -p "padrão" nome_do_arquivo.txt` |
| Avançado | `less arquivo1.txt arquivo2.txt` |

## 25) Navegação dentro do `less`

| Tecla/comando | Função apresentada |
|---|---|
| `Page Up` | Navegar para frente uma página |
| `Page Down` | Navegar para trás uma página |
| `seta para baixo` | Navegar para frente uma linha |
| `seta para cima` | Navegar para trás uma linha |
| `/` | Pesquisar string no arquivo |
| `n` | Próxima ocorrência |
| `Shift+N` | Ocorrência anterior |
| `g` | Ir para linha específica |
| `q` | Sair do `less` |

## 26) Comando `head`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `head arquivo.txt` |
| Intermediário | `head -n 5 arquivo.txt`, `head -n 10 arquivo1.txt arquivo2.txt`, `ls -l | head`, `head -c 20 arquivo.txt` |
| Avançado | `head -n 10 -q arquivo1.txt arquivo2.txt` |

## 27) Comando `tail`

| Nível | Exemplos apresentados |
|---|---|
| Básico | `tail arquivo.txt` |
| Intermediário | `tail -n 20 arquivo.txt`, `tail -c 100 nome_do_arquivo.txt`, `tail -n +2 arquivo.txt` |
| Avançado | `tail -f arquivo.log`, `tail -f -s 5 nome_do_arquivo.txt`, `tail -n 50 nome_do_arquivo.txt | grep "padrão"` |

## 28) Comando `find` — sintaxe e uso geral

| Item | Conteúdo |
|---|---|
| Sintaxe básica | `find [caminho] [parâmetros] [ações]` |
| Finalidade | Localizar arquivos e diretórios segundo critérios e, opcionalmente, executar ações sobre os resultados |

## 29) Comando `find` — exemplos básicos e intermediários

| Nível | Exemplos apresentados |
|---|---|
| Básico | `find /caminho/para/diretorio`, `find /caminho/para/diretorio -name "nome_do_arquivo.txt"`, `find /caminho/para/diretorio -name "*.txt"` |
| Intermediário | `find /caminho/para/diretorio -type d -name "nome_do_diretorio"`, `find /caminho/para/diretorio -type f -name "nome_do_arquivo"`, `find /caminho/para/diretorio -mtime -7`, `find /caminho/para/diretorio -size +100M`, `find /caminho/para/diretorio -perm 644`, `find /caminho/para/diretorio -user nome_do_usuario`, `find /caminho/para/diretorio -group nome_do_grupo` |

## 30) Comando `find` — exemplos avançados

| Exemplo | Finalidade |
|---|---|
| `find /caminho/para/diretorio -name "*.log" -exec ls -lh {} \;` | Encontrar arquivos e executar `ls -lh` em cada um |
| `find /caminho/para/diretorio -type f -name "*.txt" -exec grep -l "padrão" {} \;` | Encontrar arquivos `.txt` cujo conteúdo contém um padrão |
| `find /caminho/para/diretorio -name "*.jpg" -exec cp {} /caminho/para/novo_diretorio \;` | Copiar arquivos encontrados para outro diretório |
| `find /caminho/para/diretorio -type f -name "*.sh" -maxdepth 2 -exec chmod 755 {} \;` | Alterar permissões de arquivos `.sh` até o primeiro nível de subdiretórios |

## 31) Comando `find` — diferença entre `-exec ... {} \;` e `-exec ... {} +`

| Variante | Funcionamento |
|---|---|
| `-exec ... {} \;` | Executa o comando individualmente para cada arquivo encontrado |
| `-exec ... {} +` | Agrupa vários arquivos e passa todos de uma vez ao comando |
| Exemplo individual | `find /tmp -type f -name "*.tmp" -exec rm {} \; -exec echo "Removido: {}" \;` |
| Exemplo em lote | `find . -type f -name "*.txt" -exec mv -t /destino {} +` |

## 32) Variáveis de ambiente

| Variável/comando | Função apresentada |
|---|---|
| `PATH` | Define diretórios onde o sistema procura executáveis |
| `export PATH=$PATH:/novo/diretório` | Adiciona diretórios à busca de executáveis |
| `HOME` | Define o diretório inicial do usuário |
| `USER` | Armazena o nome do usuário atual |
| `SHELL` | Define o shell padrão do usuário |
| `LANG` | Define configurações regionais e de idioma |
| `export LANG=pt_BR.UTF-8` | Ajusta idioma e formatos regionais |
| `PWD` | Armazena o diretório de trabalho atual |
| `LOGNAME` | Armazena o nome de login do usuário |
| `env` | Exibe as variáveis de ambiente atuais |

## 33) Gerência de rede — visão geral

| Comando/ferramenta | Função apresentada |
|---|---|
| `ifconfig` / `ip` | Gerenciar interfaces de rede |
| `ifup` / `ifdown` | Ativar/desativar interfaces |
| `netstat` / `ss` | Exibir conexões de rede ativas |

## 34) Comando `ifconfig`

| Nível | Exemplos apresentados |
|---|---|
| Descrição | Configura e exibe informações sobre interfaces; alterações não são persistentes |
| Básico | `ifconfig` |
| Intermediário | `ifconfig eth0`, `ifconfig eth0 down`, `ifconfig eth0 up`, `ifconfig eth0 192.168.1.100` |
| Avançado | `ifconfig eth0 192.168.1.100 netmask 255.255.255.0 up`, `ifconfig eth0 hw ether 00:11:22:33:44:55` |

## 35) Comando `ip`

| Nível | Exemplos apresentados |
|---|---|
| Descrição | Ferramenta moderna do pacote `iproute2`; mais abrangente e poderosa que `ifconfig`; alterações não são persistentes |
| Básico | `ip addr`, `ip route`, `ip neigh`, `ip monitor all` |
| Intermediário | `ip addr show eth0`, `ip link set eth0 up`, `ip link set eth0 down`, `ip link set eth0 address 00:11:22:33:44:55`, `ip neigh flush all` |
| Avançado | `ip route add 192.168.1.0/24 via 192.168.1.1`, `ip addr add 192.168.1.101/24 dev eth0 label rede_interna`, `ip addr del 192.168.1.101/24 dev eth0 label rede_interna` |

## 36) Comandos `ifup` e `ifdown`

| Nível | Exemplos apresentados |
|---|---|
| Descrição | Ativam e desativam interfaces com base em arquivos de configuração, como `/etc/network/interfaces` |
| Básico | `ifup eth0`, `ifdown eth0` |
| Intermediário | `sudo ifup -a`, `sudo ifdown -a` |
| Avançado | `ifdown eth0 && ifup eth0` |

## 37) Comando `netstat`

| Nível | Exemplos apresentados |
|---|---|
| Descrição | Exibe conexões de rede, rotas, estatísticas de interfaces e conexões masquerade |
| Básico | `netstat` |
| Intermediário | `netstat -i`, `netstat -tuln`, `netstat -tunap` |
| Avançado | `netstat -anp | grep :80` |

## 38) Comando `ss`

| Nível | Exemplos apresentados |
|---|---|
| Descrição | Ferramenta para investigar conexões de rede; substitui `netstat`, com melhor desempenho e filtragem |
| Básico | `ss` |
| Intermediário | `ss -tuln`, `ss -tunap` |
| Avançado | `ss -o state established '( dport = :ssh or sport = :ssh )'` |

## 39) Configuração de rede em Debian/Ubuntu (`/etc/network/interfaces`)

| Campo | Conteúdo apresentado |
|---|---|
| Distribuições | Debian, Ubuntu e derivados |
| Caminho | `/etc/network/interfaces` |
| Vantagens | Estrutura simples, fácil compreensão, edição manual e suporte a múltiplas interfaces |
| Desvantagens | Exige reinício do serviço para aplicar mudanças; menos recursos avançados que métodos modernos |
| Exemplo | `auto eth0`, `iface eth0 inet static`, `address 192.168.1.100`, `netmask 255.255.255.0`, `gateway 192.168.1.1`, `dns-nameservers 8.8.8.8 8.8.4.4` |

## 40) Configuração de rede com Netplan (`/etc/netplan/`)

| Campo | Conteúdo apresentado |
|---|---|
| Distribuições | Ubuntu 17.10+ e sistemas baseados em Ubuntu |
| Caminho | `/etc/netplan/` |
| Vantagens | Usa YAML, é flexível, legível, suporta VLANs, bonding e bridges, e aplica mudanças com `sudo netplan apply` |
| Desvantagens | Exige conhecimento de YAML e depende da versão/funções suportadas |
| Exemplo resumido | `network:`, `version: 2`, `ethernets:`, `eth0:`, `dhcp4: no`, `addresses: - 192.168.1.100/24`, `gateway4: 192.168.1.1`, `nameservers: addresses: [8.8.8.8, 8.8.4.4]` |

## 41) Configuração de rede em RHEL/CentOS/Fedora (`/etc/sysconfig/network-scripts/`)

| Campo | Conteúdo apresentado |
|---|---|
| Distribuições | RHEL, CentOS, Fedora e derivados |
| Caminho | `/etc/sysconfig/network-scripts/` |
| Vantagens | Estrutura similar ao modelo tradicional, com configuração detalhada por interface |
| Desvantagens | Requer reinício do serviço (`systemctl restart network`) e é menos flexível que o Netplan para cenários avançados |
| Exemplo resumido | `DEVICE=eth0`, `BOOTPROTO=none`, `ONBOOT=yes`, `IPADDR=192.168.1.100`, `NETMASK=255.255.255.0`, `GATEWAY=192.168.1.1`, `DNS1=8.8.8.8`, `DNS2=8.8.4.4` |

## 42) Modelo de permissões no Linux

| Aspecto | Resumo |
|---|---|
| Base do modelo | Posse de arquivo ou diretório |
| Classes | Dono, grupo e outros usuários |
| Permissões por classe | Leitura (`r`), escrita (`w`) e execução (`x`) |

## 43) Leitura do resultado de `ls -l`

| Campo exibido | Significado |
|---|---|
| Tipo de objeto | Identifica se é arquivo, diretório etc. |
| Permissões do dono (`u`) | Direitos do proprietário |
| Permissões do grupo (`g`) | Direitos do grupo |
| Permissões de outros (`o`) | Direitos dos demais usuários |
| Número de links | Quantidade de links para o arquivo |
| Dono do arquivo | Proprietário |
| Grupo do arquivo | Grupo associado |
| Tamanho do arquivo | Tamanho em bytes |
| Data/hora | Última modificação |

## 44) Metadados com `stat`

| Informação destacada | Resumo |
|---|---|
| Exibição simbólica | Exemplo: `-rw-r--r--` |
| Exibição octal | Exemplo: `0644` |
| Outras informações | Tamanho, blocos, inode, links, UID, GID, tempos de acesso, modificação, mudança e criação |

## 45) Uso de `chmod`

| Forma | Exemplos apresentados |
|---|---|
| Modo octal | `chmod 644 arquivo.txt`, `chmod 600 arquivo1.txt arquivo2.txt`, `chmod -R 755 diretório/` |
| Modo simbólico | `chmod u+w arquivo.txt`, `chmod o-r arquivo.txt`, `chmod a+x arquivo.txt`, `chmod +r,g+x arquivo.txt` |
| Em múltiplos arquivos/diretórios | `chmod a+rx /caminho/do/diretorio/*` |

## 46) Efeito das permissões em diretórios

| Permissão | Efeito apresentado |
|---|---|
| Leitura (`r`) | Permite listar o conteúdo do diretório |
| Escrita (`w`) | Permite criar, excluir e renomear arquivos e subdiretórios |
| Execução (`x`) | Permite acessar o diretório e navegar por seus subdiretórios |

## 47) SUID (Set User ID)

| Aspecto | Resumo |
|---|---|
| Definição | Faz com que o usuário que executa o arquivo tenha os direitos do dono do arquivo |
| Risco | Apresentado como um dos principais vetores de escalação de privilégio |
| Identificação | No `ls -l`, aparece `s` no lugar do `x` para o usuário |
| Exemplo citado | `/usr/bin/passwd` com permissão `-rwsr-xr-x` |

## 48) Exemplos de programas com SUID citados

| Programa | Finalidade/justificativa apresentada |
|---|---|
| `/usr/bin/passwd` | Alterar senhas; precisa acessar `/etc/shadow` |
| `/usr/bin/su` | Trocar para outra conta de usuário |
| `/usr/bin/chsh` | Alterar shell padrão do usuário |
| `/usr/bin/chfn` | Alterar informações pessoais em `/etc/passwd` |
| `/usr/bin/ping` | Enviar pacotes ICMP |
| `/usr/bin/crontab` | Editar arquivos cron do usuário |
| `/usr/bin/iptables` | Gerenciar regras de firewall |
| `/usr/bin/resize` | Ajustar tamanho do terminal |

## 49) SGID (Set Group ID)

| Aspecto | Resumo |
|---|---|
| Definição | Faz com que o usuário, ao executar um arquivo, receba os direitos do grupo dono do arquivo |
| Risco | O material afirma que está sujeito aos mesmos problemas do SUID |
| Definição em arquivo | `chmod g+s nome_do_arquivo` ou `chmod 2644 nome_do_arquivo` |
| Em diretórios | Faz com que arquivos/subdiretórios herdem o grupo do diretório pai |
| Aparência | `s` no lugar do `x` para o grupo |

## 50) Sticky Bit

| Aspecto | Resumo |
|---|---|
| Definição | Permissão especial, geralmente aplicada a diretórios |
| Efeito | Impede que usuários sem privilégios excluam ou renomeiem arquivos de outros usuários no mesmo diretório |
| Uso típico | Diretórios compartilhados, como `/tmp` |
| Definição | `chmod +t nome_do_diretório` ou `chmod 1777 nome_do_diretório` |
| Exemplo citado | `/tmp` com `drwxrwxrwt` |

## 51) Busca por permissões especiais

| Objetivo | Comando apresentado |
|---|---|
| Encontrar arquivos com SUID | `find / -perm /4000 -type f 2>/dev/null` |
| Encontrar arquivos com SGID | `find / -perm /2000 -type f 2>/dev/null` |
| Encontrar diretórios com SGID | `find / -perm /2000 -type d 2>/dev/null` |
| Encontrar arquivos com Sticky Bit | `find / -perm /1000 -type f 2>/dev/null` |
| Encontrar todos com bits especiais | `find / -perm /7000 2>/dev/null` |

## 52) Atributos de sistema de arquivos (`chattr`)

| Atributo | Efeito apresentado | Exemplo |
|---|---|---|
| Imutável | Arquivo não pode ser alterado, renomeado ou excluído | `chattr +i /caminho/para/arquivo`, `chattr -i /caminho/para/arquivo` |
| Append-only | Permite apenas adicionar dados ao final do arquivo | `chattr +a /caminho/para/arquivo`, `chattr -a /caminho/para/arquivo` |

## 53) Capabilities — conceito

| Item | Resumo |
|---|---|
| Definição | Subconjunto de permissões associado a processo ou arquivo |
| Objetivo | Fornecer granularidade fina no controle de permissões |
| Exemplo citado | `CAP_NET_ADMIN` para administração de rede |
| Benefício | Reduz necessidade de conceder permissões amplas de root |
| Ganho de segurança | Aumenta flexibilidade e reduz exposição |

## 54) Capabilities — comparação com permissões tradicionais

| Modelo | Resumo |
|---|---|
| Tradicional Unix | Permissões `rwx` para proprietário, grupo e outros; operações avançadas geralmente exigem root |
| Capabilities | Controle mais específico, maior segurança e maior flexibilidade |

## 55) Capabilities — verificação e configuração

| Ação | Exemplo apresentado |
|---|---|
| Verificar capability em arquivo | `getcap /caminho/para/arquivo` |
| Exemplo de verificação | `getcap /bin/ping` → `/bin/ping = cap_net_raw+ep` |
| Adicionar capabilities | `sudo setcap cap_net_admin,cap_net_raw+ep /caminho/para/arquivo` |
| Remover capabilities | `sudo setcap -r /caminho/para/arquivo` |

## 56) Capabilities — riscos e mitigação

| Tema | Resumo |
|---|---|
| Risco de escalação | Arquivos com capabilities vulneráveis podem ser explorados para escalar privilégios |
| Exemplo citado | Binário com `CAP_NET_ADMIN` podendo ser manipulado para executar comandos como root |
| Mitigação | Auditar regularmente, usar apenas quando necessário e manter sistema/software atualizados |

## 57) `su` e `sudo` — conceitos básicos

| Comando | Resumo |
|---|---|
| `su` | Troca de usuário dentro da sessão; sem argumentos, troca para root; requer senha do usuário-alvo |
| `sudo` | Executa comandos com permissões de outro usuário, geralmente root; pede a senha do usuário atual; oferece controle detalhado |

## 58) Comparação entre `su` e `sudo`

| Critério | `su` | `sudo` |
|---|---|---|
| Troca/execução | Muda a sessão atual para outro usuário | Executa comandos específicos com privilégios elevados |
| Senha | Senha do usuário-alvo | Senha do usuário atual |
| Sessão | Mantém sessão elevada até sair | Eleva apenas o comando solicitado |
| Segurança | Menos seguro | Mais seguro e com possibilidade de registro |
| Exemplo | `su -` | `sudo apt update` |

## 59) Configuração e uso de `sudo`

| Aspecto | Conteúdo apresentado |
|---|---|
| Arquivo de configuração | `/etc/sudoers` |
| Forma de edição | `sudo visudo` |
| Finalidade | Definir quais usuários executam quais comandos e sob quais condições |
| Exemplo de regra | `alice ALL=(ALL) NOPASSWD: ALL` |
| Executar comando elevado | `sudo [comando]` |
| Executar como outro usuário | `sudo -u [usuário] [comando]` |
| Listar permissões autorizadas | `sudo -l` |
| Iniciar shell interativo como root | `sudo -i` |
| Segurança adicional | `sudo` mantém logs e permite controle granular |

## 60) Exemplos de regras em `/etc/sudoers`

| Regra/exemplo | Interpretação |
|---|---|
| `usuario ALL=(ALL) ALL` | Usuário pode executar qualquer comando como qualquer usuário em qualquer máquina |
| `usuario ALL=(ALL) NOPASSWD: ALL` | Usuário executa comandos sem senha |
| `%admin ALL=(ALL) /usr/bin/apt-get` | Grupo `admin` pode executar `apt-get` |
| `usuario ALL=(sysadmin) /usr/bin/systemctl` | Usuário pode executar `systemctl` como `sysadmin` |
| `usuario hostname=(ALL) ALL` | Regra válida apenas em host específico |
| `usuario ALL=(ALL) /usr/bin/command --option` | Permissão condicionada a comando e parâmetro específicos |
| `usuario ALL=(ALL) !/usr/bin/command` | Proibição explícita de comando |
| `usuario ALL=(ALL) NOPASSWD: ALL, /usr/bin/command` | Regra com exceção de solicitação de senha para comando específico |

## 61) `which`, `whereis` e `locate` — visão geral

| Comando | Finalidade |
|---|---|
| `which` | Localiza executáveis no `PATH` |
| `whereis` | Localiza executáveis, manuais e arquivos relacionados |
| `locate` | Busca arquivos/diretórios com base em banco indexado |

## 62) Comando `which`

| Item | Conteúdo apresentado |
|---|---|
| Uso | `which comando` |
| Exemplo | `which ls` |
| Saída típica | `/bin/ls` |
| Funcionamento | Verifica diretórios listados na variável `PATH` |
| Utilidade | Verificar qual executável está sendo chamado |

## 63) Comando `whereis`

| Item | Conteúdo apresentado |
|---|---|
| Uso | `whereis comando` |
| Exemplo | `whereis ls` |
| Saída típica | `ls: /bin/ls /usr/share/man/man1/ls.1.gz` |
| Funcionamento | Procura executáveis, manuais e fontes em locais padrão |
| Utilidade | Encontrar arquivos relacionados ao comando |

## 64) Comando `locate`

| Item | Conteúdo apresentado |
|---|---|
| Uso | `locate nome_do_arquivo` |
| Exemplo | `locate ls` |
| Saída típica | `/bin/ls /usr/share/man/man1/ls.1.gz` |
| Funcionamento | Usa banco de dados indexado, normalmente atualizado por `updatedb` |
| Utilidade | Busca rápida de arquivos e diretórios em todo o sistema |
| Limitação citada | Pode retornar muitos resultados |

## 65) Conclusão do material

| Item | Resumo |
|---|---|
| Encerramento | A página 82 apresenta apenas a mensagem “CONCLUSÃO!” como fechamento do conteúdo. |

## 66) Seção final: Capture The Flag

| Campo | Conteúdo |
|---|---|
| Título | Capture The Flag |
| Ambiente citado | Shellock Holmes |
| Endereço informado no material | `http://shellock.cige/` |

## 67) Síntese final do conteúdo inteiro

| Eixo | Síntese |
|---|---|
| Fundamentos | Explica o que é sistema operacional, kernel, shell e distribuições Linux |
| Operação | Cobre arquivos importantes, shell, variáveis de ambiente e comandos básicos/intermediários/avançados |
| Administração | Trata de rede, permissões, usuários, grupos e `sudo` |
| Segurança | Destaca arquivos sensíveis, permissões especiais, capabilities e temas ofensivos citados nos objetivos |
| Encerramento | Fecha com conclusão breve e referência ao laboratório/CTF Shellock Holmes |
