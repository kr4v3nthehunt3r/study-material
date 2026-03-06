# Resumo de Linux para Estudo

## 1. Ideia central
**Linux é um sistema operacional formado por 3 partes principais:**
- **Kernel** → gerencia o hardware
- **Shell** → recebe e interpreta comandos
- **Utilitários** → executam tarefas do sistema

## 2. Como pensar no Shell
Pense assim:

**Usuário → Shell → Sistema**

O shell é a “porta de entrada” do Linux: ele faz a interface com o usuário, interpreta comandos, permite scripts, pipes e redirecionamentos.

## 3. Comandos que mais caem
Decore esse bloco:

- **ls** = listar
- **cd** = entrar/trocar diretório
- **cp** = copiar
- **mv** = mover/renomear
- **rm** = remover
- **mkdir** = criar diretório
- **touch** = criar arquivo / atualizar data
- **cat** = mostrar conteúdo
- **grep** = procurar texto
- **less** = ler arquivo com rolagem
- **head** = primeiras linhas
- **tail** = últimas linhas
- **find** = localizar arquivos

## 4. Estrutura de um comando
Um comando pode ter:
- **nome do comando**
- **argumentos**
- **redirecionamento**
- **operadores**

Operadores importantes:
- `;` = executa um depois do outro
- `&&` = executa o próximo se deu certo
- `||` = executa o próximo se deu erro
- `|` = envia a saída de um comando para o outro
- `&` = execução assíncrona

## 5. Permissões — a lógica principal
No Linux, toda permissão gira em torno de:
- **dono**
- **grupo**
- **outros**

E cada um pode ter:
- **r** = leitura
- **w** = escrita
- **x** = execução

## 6. Regra mental das permissões
**Permissão responde à pergunta: quem pode fazer o quê?**

Exemplo:
- `r` = pode ler
- `w` = pode alterar
- `x` = pode executar

## 7. Arquivos importantes para decorar
Os principais arquivos citados no material são:
- **/etc/passwd** → informações da conta
- **/etc/shadow** → senha e hash
- **/etc/group** → grupos
- **/etc/fstab** → montagem de sistemas de arquivos
- **/etc/network/interfaces** e **/etc/netplan** → rede

## 8. Contas e identificação
- **UID/GID 0** = root
- **1 a 999** = contas de sistema/serviços
- **1000+** = usuários comuns

## 9. Segurança — o que mais lembrar
- **/etc/shadow** guarda hashes de senha e políticas de expiração.
- O material cita hashes como **MD5, SHA-256, SHA-512, bcrypt e yescrypt**.
- **sudo** permite executar comandos com privilégio elevado de forma controlada e com registro em log.

## 10. Rede — visão rápida
Comandos de rede mais importantes:
- **ifconfig / ip**
- **ifup / ifdown**
- **netstat / ss**

No material, a configuração moderna aparece com **Netplan** em `/etc/netplan/`, usando YAML e aplicação com `netplan apply`.

## Macete para memorizar
Estude em 4 blocos:

**1. Estrutura** → kernel, shell, utilitários  
**2. Comandos** → navegar, copiar, mover, apagar, buscar  
**3. Permissões** → dono, grupo, outros + r w x  
**4. Segurança** → root, sudo, shadow, hashes, rede

## Frase-resumo
**Linux = estrutura + comandos + permissões + segurança.**
