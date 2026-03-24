# Comandos de Rede e Firewall no Windows

Documento unificado com comandos úteis de **rede** e **firewall** no Windows, incluindo opções em **CMD/netsh** e **PowerShell**.

---

# Comandos de Rede no Windows

## Comandos básicos de rede

| Comando | Função |
|---|---|
| `ipconfig` | Exibe configuração IP da máquina |
| `ipconfig /all` | Mostra detalhes completos da interface de rede |
| `ipconfig /release` | Libera o endereço IP atual |
| `ipconfig /renew` | Renova o endereço IP |
| `ipconfig /flushdns` | Limpa o cache DNS |
| `ipconfig /displaydns` | Mostra o cache DNS local |
| `ping <host>` | Testa conectividade com outro host |
| `tracert <host>` | Mostra a rota até o destino |
| `pathping <host>` | Combina ping com rastreamento de rota |
| `nslookup <domínio>` | Consulta DNS |
| `arp -a` | Exibe a tabela ARP |
| `route print` | Mostra a tabela de rotas |
| `netstat -an` | Lista conexões e portas abertas |
| `netstat -ano` | Lista conexões, portas e PID do processo |
| `netstat -rn` | Exibe a tabela de roteamento |
| `hostname` | Mostra o nome da máquina |
| `getmac` | Mostra os endereços MAC |
| `nbtstat -n` | Mostra nomes NetBIOS locais |
| `nbtstat -A <IP>` | Consulta NetBIOS de um host remoto |
| `net view` | Lista computadores/recursos da rede |
| `net use` | Exibe ou conecta compartilhamentos de rede |
| `net share` | Mostra compartilhamentos locais |
| `telnet <host> <porta>` | Testa acesso a uma porta, se Telnet estiver habilitado |
| `curl <url>` | Faz requisições HTTP/HTTPS |
| `ftp <host>` | Acessa servidor FTP |
| `powershell Test-NetConnection <host>` | Testa conectividade via PowerShell |
| `powershell Resolve-DnsName <domínio>` | Consulta DNS via PowerShell |

## Comandos de diagnóstico mais usados

```cmd
ipconfig /all
ping 8.8.8.8
ping google.com
tracert google.com
nslookup google.com
netstat -ano
arp -a
route print
getmac
hostname
```

## Para ver portas abertas e conexões

```cmd
netstat -ano
netstat -an | findstr LISTENING
tasklist | findstr <PID>
```

## Para Wi-Fi no Windows

```cmd
netsh wlan show profiles
netsh wlan show interfaces
netsh wlan show networks
```

## Para adaptadores de rede

```cmd
netsh interface show interface
netsh interface ip show config
```

## Em PowerShell

```powershell
Get-NetIPConfiguration
Get-NetIPAddress
Get-NetRoute
Get-NetAdapter
Test-NetConnection google.com
Resolve-DnsName google.com
```

## Resumo por objetivo

| Objetivo | Comando |
|---|---|
| Ver IP da máquina | `ipconfig` |
| Ver detalhes completos | `ipconfig /all` |
| Testar internet | `ping 8.8.8.8` |
| Testar DNS | `nslookup google.com` |
| Ver rota até um site | `tracert google.com` |
| Ver portas abertas | `netstat -ano` |
| Ver MAC address | `getmac` |
| Ver cache DNS | `ipconfig /displaydns` |
| Limpar cache DNS | `ipconfig /flushdns` |
| Ver tabela ARP | `arp -a` |
| Ver rotas | `route print` |
| Ver Wi-Fi salvo | `netsh wlan show profiles` |

---

# Comandos de Firewall no Windows

Lista prática de comandos de **Firewall do Windows**, separada entre **CMD/netsh** e **PowerShell**.

## CMD / netsh

| Comando | Função |
|---|---|
| `netsh advfirewall show allprofiles` | Mostra o estado dos perfis Domain, Private e Public |
| `netsh advfirewall set allprofiles state on` | Ativa o firewall em todos os perfis |
| `netsh advfirewall set allprofiles state off` | Desativa o firewall em todos os perfis |
| `netsh advfirewall firewall show rule name=all` | Lista todas as regras do firewall |
| `netsh advfirewall firewall show rule name="NOME_DA_REGRA"` | Exibe uma regra específica |
| `netsh advfirewall firewall add rule name="Liberar 80" dir=in action=allow protocol=TCP localport=80` | Cria regra de entrada liberando a porta 80 |
| `netsh advfirewall firewall add rule name="Bloquear 445" dir=in action=block protocol=TCP localport=445` | Cria regra de entrada bloqueando a porta 445 |
| `netsh advfirewall firewall delete rule name="Liberar 80"` | Remove uma regra pelo nome |
| `netsh advfirewall firewall set rule name="NOME_DA_REGRA" new enable=yes` | Habilita uma regra existente |
| `netsh advfirewall firewall set rule name="NOME_DA_REGRA" new enable=no` | Desabilita uma regra existente |
| `netsh advfirewall export "C:\firewall.wfw"` | Exporta a configuração do firewall |
| `netsh advfirewall import "C:\firewall.wfw"` | Importa a configuração do firewall |
| `netsh advfirewall reset` | Restaura as configurações padrão do firewall |
| `netsh advfirewall show currentprofile` | Exibe o perfil atualmente ativo |
| `netsh advfirewall set domainprofile firewallpolicy blockinbound,allowoutbound` | Define política do perfil Domain |
| `netsh advfirewall set privateprofile firewallpolicy blockinbound,allowoutbound` | Define política do perfil Private |
| `netsh advfirewall set publicprofile firewallpolicy blockinbound,allowoutbound` | Define política do perfil Public |

## PowerShell

| Comando | Função |
|---|---|
| `Get-NetFirewallProfile` | Exibe configurações dos perfis do firewall |
| `Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True` | Ativa o firewall nos perfis informados |
| `Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled False` | Desativa o firewall nos perfis informados |
| `Get-NetFirewallRule` | Lista regras do firewall |
| `Get-NetFirewallRule -DisplayName "*RDP*"` | Filtra regras pelo nome exibido |
| `New-NetFirewallRule -DisplayName "Liberar 3389" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3389` | Cria regra para liberar RDP |
| `New-NetFirewallRule -DisplayName "Bloquear 21" -Direction Inbound -Action Block -Protocol TCP -LocalPort 21` | Cria regra para bloquear FTP na porta 21 |
| `Set-NetFirewallRule -DisplayName "Liberar 3389" -Enabled True` | Habilita uma regra |
| `Set-NetFirewallRule -DisplayName "Liberar 3389" -Enabled False` | Desabilita uma regra |
| `Remove-NetFirewallRule -DisplayName "Liberar 3389"` | Remove uma regra |
| `Enable-NetFirewallRule -DisplayGroup "Remote Desktop"` | Habilita um grupo de regras |
| `Disable-NetFirewallRule -DisplayGroup "Remote Desktop"` | Desabilita um grupo de regras |

## Exemplos prontos

### Ver status do firewall
```cmd
netsh advfirewall show allprofiles
```

```powershell
Get-NetFirewallProfile
```

### Ativar firewall
```cmd
netsh advfirewall set allprofiles state on
```

```powershell
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True
```

### Criar regra para liberar uma porta
```cmd
netsh advfirewall firewall add rule name="Liberar 8080" dir=in action=allow protocol=TCP localport=8080
```

```powershell
New-NetFirewallRule -DisplayName "Liberar 8080" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8080
```

### Bloquear uma porta
```cmd
netsh advfirewall firewall add rule name="Bloquear 23" dir=in action=block protocol=TCP localport=23
```

```powershell
New-NetFirewallRule -DisplayName "Bloquear 23" -Direction Inbound -Action Block -Protocol TCP -LocalPort 23
```

### Exportar e restaurar configuração
```cmd
netsh advfirewall export "C:\firewall.wfw"
netsh advfirewall reset
netsh advfirewall import "C:\firewall.wfw"
```

## Observação importante

Muitos desses comandos exigem **Prompt de Comando** ou **PowerShell** executado como **administrador**, especialmente para criar, alterar, importar, exportar ou resetar regras e perfis.
