# Comandos Linux Unificados: Rede e Firewall

Este documento reúne, em um único arquivo, os principais **comandos de rede** e **comandos de firewall** no Linux, organizados por categoria e com a finalidade de cada comando.

---

# 1. Comandos de Rede no Linux

## 1.1 Comandos básicos de identificação de rede

| Comando | Função |
|---|---|
| `ip a` | Mostra interfaces de rede e endereços IP |
| `ip addr show` | Exibe IPs das interfaces |
| `ip link show` | Mostra o estado das interfaces |
| `hostname -I` | Mostra o IP da máquina |
| `hostname` | Mostra o nome do host |
| `uname -a` | Exibe informações do sistema |

## 1.2 Comandos de teste de conectividade

| Comando | Função |
|---|---|
| `ping 8.8.8.8` | Testa conectividade com um IP |
| `ping google.com` | Testa conectividade e resolução DNS |
| `tracepath google.com` | Mostra o caminho até o destino |
| `traceroute google.com` | Rastreia os saltos até o destino |
| `mtr google.com` | Combina ping com traceroute |

## 1.3 Comandos de DNS

| Comando | Função |
|---|---|
| `nslookup google.com` | Consulta DNS |
| `dig google.com` | Consulta DNS detalhada |
| `host google.com` | Resolve nome para IP |
| `cat /etc/resolv.conf` | Mostra os servidores DNS configurados |

## 1.4 Comandos de portas e conexões

| Comando | Função |
|---|---|
| `ss -tulnp` | Lista portas abertas e processos |
| `netstat -tulnp` | Lista conexões e portas abertas |
| `lsof -i` | Mostra processos usando rede |
| `lsof -i :80` | Mostra quem usa a porta 80 |
| `nc -zv 192.168.0.10 22` | Testa conexão em uma porta |
| `telnet 192.168.0.10 80` | Testa acesso a uma porta |

## 1.5 Comandos de rotas e gateway

| Comando | Função |
|---|---|
| `ip route` | Mostra a tabela de rotas |
| `route -n` | Exibe rotas em formato numérico |
| `ip route show default` | Mostra o gateway padrão |

## 1.6 Comandos de configuração de interface

| Comando | Função |
|---|---|
| `ifconfig` | Mostra/configura interfaces de rede |
| `ip link set eth0 up` | Ativa uma interface |
| `ip link set eth0 down` | Desativa uma interface |
| `ip addr add 192.168.1.10/24 dev eth0` | Adiciona IP manualmente |

## 1.7 Comandos de análise de rede

| Comando | Função |
|---|---|
| `arp -a` | Mostra tabela ARP |
| `ip neigh` | Mostra vizinhos ARP/NDP |
| `tcpdump -i eth0` | Captura tráfego da interface |
| `tcpdump -i any port 80` | Captura tráfego da porta 80 |
| `wireshark` | Analisador gráfico de pacotes |

## 1.8 Comandos HTTP e teste de serviço

| Comando | Função |
|---|---|
| `curl http://site.com` | Faz requisição HTTP |
| `curl -I http://site.com` | Mostra apenas cabeçalhos |
| `wget http://site.com` | Baixa conteúdo/arquivo |
| `openssl s_client -connect site.com:443` | Testa conexão TLS/SSL |

## 1.9 Comandos de rede local

| Comando | Função |
|---|---|
| `nmap 192.168.0.1` | Varre portas de um host |
| `nmap -sn 192.168.0.0/24` | Descobre hosts ativos na rede |
| `arp-scan --localnet` | Descobre dispositivos na rede local |

## 1.10 Comandos úteis de arquivos de configuração

| Arquivo/Comando | Função |
|---|---|
| `cat /etc/hosts` | Mostra mapeamentos locais de nome/IP |
| `cat /etc/hostname` | Mostra o hostname configurado |
| `nmcli device status` | Mostra status de rede via NetworkManager |
| `nmcli connection show` | Lista conexões salvas |
| `systemctl status NetworkManager` | Verifica status do serviço de rede |

## 1.11 Exemplos práticos rápidos de rede

```bash
ip a
ip route
ping 8.8.8.8
ping google.com
ss -tulnp
dig google.com
curl -I https://google.com
```

---

# 2. Comandos de Firewall no Linux

## 2.1 UFW (Ubuntu / Debian simplificado)

| Comando | Função |
|---|---|
| `sudo ufw status` | Mostra o status do firewall |
| `sudo ufw status verbose` | Mostra status detalhado |
| `sudo ufw enable` | Ativa o UFW |
| `sudo ufw disable` | Desativa o UFW |
| `sudo ufw reload` | Recarrega as regras |
| `sudo ufw allow 22` | Libera a porta 22 |
| `sudo ufw deny 22` | Bloqueia a porta 22 |
| `sudo ufw reject 22` | Rejeita conexões na porta 22 |
| `sudo ufw allow 80/tcp` | Libera HTTP TCP |
| `sudo ufw allow 53/udp` | Libera DNS UDP |
| `sudo ufw delete allow 22` | Remove a regra de liberação da porta 22 |
| `sudo ufw allow from 192.168.1.10` | Libera tráfego de um IP específico |
| `sudo ufw allow from 192.168.1.0/24` | Libera uma sub-rede |
| `sudo ufw allow from 192.168.1.10 to any port 22` | Libera SSH só para um IP |
| `sudo ufw deny from 10.0.0.5` | Bloqueia um IP específico |
| `sudo ufw app list` | Lista perfis de aplicativos |
| `sudo ufw app info OpenSSH` | Mostra detalhes do perfil OpenSSH |
| `sudo ufw allow OpenSSH` | Libera perfil do OpenSSH |

## 2.2 iptables

| Comando | Função |
|---|---|
| `sudo iptables -L` | Lista regras |
| `sudo iptables -L -n -v` | Lista regras com detalhes |
| `sudo iptables -S` | Mostra regras em formato de comandos |
| `sudo iptables -F` | Limpa regras |
| `sudo iptables -X` | Remove cadeias personalizadas |
| `sudo iptables -P INPUT DROP` | Define política padrão da cadeia INPUT |
| `sudo iptables -P FORWARD DROP` | Define política padrão da cadeia FORWARD |
| `sudo iptables -P OUTPUT ACCEPT` | Define política padrão da cadeia OUTPUT |
| `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT` | Libera SSH |
| `sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT` | Libera HTTP |
| `sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT` | Libera HTTPS |
| `sudo iptables -A INPUT -s 192.168.1.10 -j ACCEPT` | Libera um IP específico |
| `sudo iptables -A INPUT -s 10.0.0.5 -j DROP` | Bloqueia um IP |
| `sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT` | Permite conexões já estabelecidas |
| `sudo iptables -A INPUT -i lo -j ACCEPT` | Permite loopback |
| `sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT` | Remove regra específica |
| `sudo iptables-save` | Exibe regras para backup |
| `sudo iptables-restore < regras.txt` | Restaura regras salvas |

## 2.3 nftables

| Comando | Função |
|---|---|
| `sudo nft list ruleset` | Lista todas as regras |
| `sudo nft flush ruleset` | Limpa todas as regras |
| `sudo nft add table inet filtro` | Cria tabela |
| `sudo nft add chain inet filtro input '{ type filter hook input priority 0; }'` | Cria cadeia INPUT |
| `sudo nft add rule inet filtro input tcp dport 22 accept` | Libera SSH |
| `sudo nft add rule inet filtro input tcp dport 80 accept` | Libera HTTP |
| `sudo nft add rule inet filtro input tcp dport 443 accept` | Libera HTTPS |
| `sudo nft add rule inet filtro input ip saddr 192.168.1.10 accept` | Libera um IP |
| `sudo nft add rule inet filtro input ip saddr 10.0.0.5 drop` | Bloqueia um IP |
| `sudo nft list table inet filtro` | Lista regras de uma tabela |
| `sudo nft delete table inet filtro` | Remove tabela |

## 2.4 firewalld (RHEL / CentOS / Fedora)

| Comando | Função |
|---|---|
| `sudo firewall-cmd --state` | Mostra se o firewalld está ativo |
| `sudo firewall-cmd --get-active-zones` | Mostra zonas ativas |
| `sudo firewall-cmd --get-default-zone` | Mostra a zona padrão |
| `sudo firewall-cmd --list-all` | Lista regras da zona atual |
| `sudo firewall-cmd --permanent --add-service=http` | Libera HTTP permanentemente |
| `sudo firewall-cmd --permanent --add-service=https` | Libera HTTPS permanentemente |
| `sudo firewall-cmd --permanent --add-service=ssh` | Libera SSH permanentemente |
| `sudo firewall-cmd --permanent --remove-service=ssh` | Remove regra de SSH |
| `sudo firewall-cmd --permanent --add-port=8080/tcp` | Libera porta TCP |
| `sudo firewall-cmd --permanent --remove-port=8080/tcp` | Remove liberação da porta |
| `sudo firewall-cmd --reload` | Recarrega as regras |
| `sudo firewall-cmd --list-services` | Lista serviços liberados |
| `sudo firewall-cmd --list-ports` | Lista portas liberadas |
| `sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.10" accept'` | Libera IP específico |
| `sudo firewall-cmd --permanent --add-source=192.168.1.0/24` | Adiciona origem confiável |

## 2.5 Verificações úteis

| Comando | Função |
|---|---|
| `sudo ss -tulnp` | Lista portas abertas |
| `sudo netstat -tulnp` | Lista portas e serviços |
| `sudo lsof -i` | Mostra processos usando rede |
| `sudo systemctl status ufw` | Verifica status do UFW |
| `sudo systemctl status firewalld` | Verifica status do firewalld |
| `sudo systemctl status nftables` | Verifica status do nftables |

## 2.6 Exemplos práticos rápidos de firewall

```bash
sudo ufw status
sudo ufw allow 22
sudo ufw allow 80/tcp
sudo ufw enable
```

```bash
sudo iptables -L -n -v
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

```bash
sudo firewall-cmd --list-all
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

```bash
sudo nft list ruleset
sudo nft add rule inet filtro input tcp dport 22 accept
```

---

# 3. Resumo rápido

## 3.1 Rede
- Identificação de interfaces: `ip a`, `ip link show`
- Teste de conectividade: `ping`, `traceroute`, `mtr`
- Resolução DNS: `dig`, `nslookup`, `host`
- Portas e serviços: `ss`, `netstat`, `lsof`, `nc`
- Captura e análise: `tcpdump`, `wireshark`

## 3.2 Firewall
- UFW: mais simples para Ubuntu/Debian
- iptables: tradicional e poderoso
- nftables: substituto moderno do iptables
- firewalld: comum em Fedora, RHEL e CentOS

