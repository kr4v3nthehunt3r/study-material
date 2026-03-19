# Filtros Wireshark (Display Filters)



---

## Convenção adotada

- `X.X.X.X` = endereço IPv4 de exemplo
- `N` = número de stream/fluxo
- Todos os exemplos abaixo usam **Display Filters** do Wireshark
- Quando houver mais de uma opção equivalente, o padrão preferido foi simplificado

---

## 1. Endereços MAC e IP

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| MAC | Filtrar por MAC de origem ou destino | `eth.addr == 00:1A:2B:3C:4D:5E` | Ethernet II -> Source/Destination |
| IP | Ver tráfego de um host | `ip.addr == X.X.X.X` | IPv4 -> Source/Destination |
| IP origem | Isolar origem | `ip.src == X.X.X.X` | IPv4 -> Source |
| IP destino | Isolar destino | `ip.dst == X.X.X.X` | IPv4 -> Destination |
| IPv6 | Mostrar somente IPv6 | `ipv6` | Cabeçalho IPv6 |

---

## 2. Protocolos básicos

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| TCP | Mostrar somente TCP | `tcp` | TCP -> Src Port / Dst Port |
| UDP | Mostrar somente UDP | `udp` | UDP -> Src Port / Dst Port |
| HTTP | Mostrar tráfego HTTP | `http` | HTTP decodificado |
| DNS | Mostrar tráfego DNS | `dns` | DNS |
| ICMP | Mostrar tráfego ICMP | `icmp` | ICMP |
| ARP | Mostrar tráfego ARP | `arp` | ARP |
| NTP | Mostrar tráfego NTP | `ntp` | NTP |
| SMTP | Mostrar tráfego SMTP | `smtp` | SMTP |
| DHCP/BOOTP | Mostrar DHCP | `bootp` | Opções DHCP |
| NBNS | Mostrar NetBIOS Name Service | `nbns` | Query/Response |
| LLMNR | Mostrar LLMNR | `llmnr` | Query/Name |
| mDNS | Mostrar mDNS | `mdns` | Nomes/serviços |

---

## 3. Portas e transporte

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| Porta TCP | Isolar porta TCP 80 | `tcp.port == 80` | TCP -> ports |
| Porta TCP | Isolar porta TCP 443 | `tcp.port == 443` | TCP -> ports |
| Porta UDP | Isolar DNS via UDP | `udp.port == 53` | UDP -> ports |
| Porta UDP | Isolar NTP via UDP | `udp.port == 123` | UDP -> ports |
| DNS por porta | Confirmar DNS via UDP ou TCP | `(udp.port == 53) || (tcp.port == 53)` | Transporte DNS |
| SMTP por portas | Isolar SMTP padrão/submissão | `(tcp.port == 25) || (tcp.port == 587)` | TCP -> ports |

---

## 4. Handshake TCP e TLS

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| TLS handshake | Identificar Client Hello | `tls.handshake.type == 1` | TLS -> Handshake Type |
| HTTPS | Ver tráfego HTTPS/TLS na 443 | `tcp.port == 443` | TCP -> ports |
| TCP SYN | Identificar início de conexão | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Flags TCP |
| TCP SYN-ACK | Identificar resposta do servidor | `tcp.flags.syn == 1 && tcp.flags.ack == 1` | Flags TCP |
| Sessão TCP específica | Filtrar pacote de controle/sessão | `tcp.seq == 1 && tcp.ack == 1 && tcp.len == 0 && !(tcp.flags.push == 1)` | Seq / Ack / Len / Flags |

---

## 5. Flags TCP

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| SYN | Filtrar pacotes SYN | `tcp.flags == 0x02` | Flags TCP |
| ACK | Filtrar pacotes ACK | `tcp.flags == 0x10` | Flags TCP |
| SYN sem ACK | Identificar SYN puro | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Flags TCP |
| SYN-ACK | Identificar SYN-ACK | `tcp.flags.syn == 1 && tcp.flags.ack == 1` | Flags TCP |

---

## 6. Streams e fluxos

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| Stream TCP | Isolar uma conversa TCP | `tcp.stream eq N` | Follow TCP Stream |
| Stream UDP | Isolar um fluxo UDP | `udp.stream eq N` | Fluxo UDP |
| Exemplo TCP | Exemplo direto de stream | `tcp.stream eq 5` | Mesmo fluxo |
| Modelo genérico | Placeholder para stream TCP | `tcp.stream eq <num_stream>` | Mesmo fluxo |

---

## 7. HTTP

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| HTTP geral | Ver tudo HTTP | `http` | HTTP decodificado |
| Requisições HTTP | Ver método, host e URI | `http.request` | `http.request.method`, `http.host`, `http.request.uri` |
| Respostas HTTP | Ver status e headers | `http.response` | `http.response.code` |
| Método GET | Isolar GET | `http.request.method == "GET"` | Campo Method |
| Método POST | Isolar POST | `http.request.method == "POST"` | Campo Method |
| URI com extensão | Caçar downloads comuns | `http.request && http.request.uri matches "\\.(exe|msi)$"` | URI requisitada |
| Redirect 301 | Localizar redirecionamento permanente | `http.response.code == 301` | Código HTTP |
| Redirect 302 | Localizar redirecionamento temporário | `http.response.code == 302` | Código HTTP |
| Header Location | Encontrar URL de redirecionamento | `frame contains "Location:"` | Header `Location:` |
| User-Agent | Identificar cliente HTTP | `http.user_agent` | Campo `User-Agent` |

---

## 8. DNS

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| DNS geral | Ver DNS | `dns` | DNS |
| Consultas DNS | Ver domínio pesquisado | `dns.flags.response == 0` | `dns.qry.name` |
| Respostas DNS | Ver respostas do DNS | `dns.flags.response == 1` | `dns.a`, `dns.aaaa` |
| Resposta A | Ver IPv4 retornado | `dns.flags.response == 1 && dns.a` | Campo A |
| Resposta AAAA | Ver IPv6 retornado | `dns.flags.response == 1 && dns.aaaa` | Campo AAAA |

---

## 9. ICMP, ARP e descoberta de hosts

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| ARP | Ver ARP | `arp` | ARP |
| ARP por IP | Obter MAC associado a um IP | `arp && arp.src.proto_ipv4 == X.X.X.X` | Ethernet II MAC |
| ICMP geral | Ver ICMP | `icmp` | ICMP |
| Echo Request | Identificar ping | `icmp.type == 8` | ICMP Type |

---

## 10. DHCP, nomes e descoberta local

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| DHCP/BOOTP | Descobrir IP e hostname | `bootp` | Opções DHCP |
| Hostname DHCP | Filtrar hostname no DHCP | `bootp.option.hostname` | Hostname |
| NBNS | Nome NetBIOS | `nbns` | Name query/response |
| LLMNR | Nome de host Windows | `llmnr` | Query/Name |
| mDNS | Descoberta de serviços locais | `mdns` | Nomes/serviços |

---

## 11. NTP

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| NTP geral | Isolar NTP | `ntp` | NTP |
| Porta NTP | Confirmar UDP/123 | `udp.port == 123` | UDP dst/src port |
| Versão NTP | Ver versão do protocolo | `ntp.version` | Campo Version |
| TTL no NTP | Correlacionar TTL do host | `ntp && ip.ttl` | IPv4 -> TTL |

---

## 12. SMTP

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| SMTP geral | Ver SMTP | `smtp` | SMTP |
| SMTP por portas | Pegar comunicação SMTP | `(tcp.port == 25) || (tcp.port == 587)` | TCP -> ports |
| Banner/versão | Achar serviço/versão | `frame contains "220"` | Linha `220 ... ESMTP ...` |
| AUTH | Achar autenticação | `frame contains "AUTH"` | AUTH LOGIN/PLAIN |
| MAIL FROM | E-mail de origem | `frame contains "MAIL FROM:"` | Comando MAIL FROM |
| RCPT TO | E-mail de destino | `frame contains "RCPT TO:"` | Comando RCPT TO |
| DATA | Início do corpo da mensagem | `frame contains "DATA"` | Corpo após DATA |

---

## 13. Conteúdo, payload e inspeção textual

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| Palavra no frame | Buscar string no payload | `frame contains "senha"` | Payload/frame |
| XML | Encontrar XML no tráfego | `frame contains "<?xml"` | Trecho XML |
| STS | Encontrar tag STS | `frame contains "<STS"` | Valor/ID no XML |
| Header Location | Capturar redirect “na marra” | `frame contains "Location:"` | Header `Location:` |

---

## 14. Tamanho, tempo e TTL

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| Tamanho do pacote | Filtrar frames grandes | `frame.len > 1000` | Frame length |
| Tempo | Filtrar após data/hora | `frame.time >= "2023-09-19 14:00:00"` | Timestamp do frame |
| TTL geral | Ver TTL | `ip.ttl` | IPv4 -> Time to Live |
| TTL específico | Filtrar TTL conhecido | `ip.ttl == 64` | TTL |
| TTL específico | Filtrar TTL conhecido | `ip.ttl == 128` | TTL |
| TTL específico | Filtrar TTL conhecido | `ip.ttl == 255` | TTL |

---

## 15. Expressões lógicas úteis

| Categoria | Objetivo | Filtro | Confirmar no pacote |
|---|---|---|---|
| IP + porta | Combinar origem e serviço | `(ip.src == 192.168.1.1) && (tcp.port == 80)` | Source + Port |
| SYN | Confirmar início de conexão | `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Flags TCP |
| SYN-ACK | Confirmar resposta do handshake | `tcp.flags.syn == 1 && tcp.flags.ack == 1` | Flags TCP |

---

## 16. Lista rápida padronizada

```bash
eth.addr == 00:1A:2B:3C:4D:5E
ip.addr == X.X.X.X
ip.src == X.X.X.X
ip.dst == X.X.X.X
ipv6
tcp
udp
tcp.port == 80
tcp.port == 443
udp.port == 53
udp.port == 123
http
http.request
http.response
http.request.method == "GET"
http.request.method == "POST"
http.user_agent
http.request && http.request.uri matches "\.(exe|msi)$"
http.response.code == 301
http.response.code == 302
dns
dns.flags.response == 0
dns.flags.response == 1
dns.flags.response == 1 && dns.a
dns.flags.response == 1 && dns.aaaa
arp
arp && arp.src.proto_ipv4 == X.X.X.X
icmp
icmp.type == 8
ntp
ntp.version
smtp
bootp
bootp.option.hostname
nbns
llmnr
mdns
frame.len > 1000
frame contains "senha"
frame contains "Location:"
frame contains "<?xml"
frame contains "<STS"
frame.time >= "2023-09-19 14:00:00"
ip.ttl
ip.ttl == 64
ip.ttl == 128
ip.ttl == 255
tcp.flags == 0x02
tcp.flags == 0x10
tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.flags.syn == 1 && tcp.flags.ack == 1
tls.handshake.type == 1
tcp.stream eq N
udp.stream eq N
tcp.seq == 1 && tcp.ack == 1 && tcp.len == 0 && !(tcp.flags.push == 1)
(udp.port == 53) || (tcp.port == 53)
(tcp.port == 25) || (tcp.port == 587)
(ip.src == 192.168.1.1) && (tcp.port == 80)
```

---

