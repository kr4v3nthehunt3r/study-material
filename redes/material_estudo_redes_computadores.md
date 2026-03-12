# Material de estudo aprofundado — Redes de Computadores

## 1. Arquitetura de protocolos, modelo OSI, TCP/IP e camadas

## Conceito central
Redes de computadores funcionam por meio de **protocolos**, isto é, regras formais que definem como dados são estruturados, transmitidos, recebidos e interpretados entre dispositivos.

Como a comunicação em rede é complexa, ela é organizada em **camadas**, de forma que cada camada execute um conjunto específico de funções e interaja com as camadas vizinhas.

Essa organização traz:
- padronização;
- modularidade;
- interoperabilidade;
- facilidade de manutenção e evolução tecnológica.

---

## O que é um protocolo
Um **protocolo de rede** define:
- formato dos dados;
- ordem de transmissão;
- forma de controle de erros;
- mecanismo de sincronização;
- comportamento esperado entre emissor e receptor.

### Exemplos
- **IP**: endereçamento e encaminhamento
- **TCP**: transporte confiável
- **UDP**: transporte leve e sem conexão
- **HTTP**: comunicação web
- **DNS**: resolução de nomes
- **SSH**: acesso remoto seguro

---

## Modelo OSI
O modelo **OSI (Open Systems Interconnection)** é uma referência conceitual com **7 camadas**.

| Camada | Nome | Função principal |
|---|---|---|
| 7 | Aplicação | Serviços de rede para aplicações |
| 6 | Apresentação | Formatação, codificação, compressão e criptografia |
| 5 | Sessão | Controle e gerenciamento da sessão |
| 4 | Transporte | Comunicação fim a fim, confiabilidade, portas |
| 3 | Rede | Endereçamento lógico e roteamento |
| 2 | Enlace | Comunicação local, quadros, MAC |
| 1 | Física | Transmissão de bits no meio físico |

### Observação importante
Na prática, o modelo OSI é muito usado para:
- estudar redes;
- diagnosticar falhas;
- classificar tecnologias e protocolos.

---

## Modelo TCP/IP
O modelo **TCP/IP** é o modelo prático utilizado na Internet.

| Camada TCP/IP | Equivalência aproximada no OSI | Exemplos |
|---|---|---|
| Aplicação | Aplicação + Apresentação + Sessão | HTTP, DNS, SSH, SMTP |
| Transporte | Transporte | TCP, UDP |
| Internet | Rede | IP, ICMP |
| Acesso à Rede | Enlace + Física | Ethernet, Wi‑Fi, ARP |

---

## Encapsulamento
Quando os dados saem de uma aplicação, cada camada adiciona seu próprio cabeçalho. Esse processo é chamado de **encapsulamento**.

Fluxo lógico:
- aplicação gera dados;
- transporte adiciona cabeçalho TCP ou UDP;
- rede adiciona cabeçalho IP;
- enlace adiciona cabeçalho e trailer do quadro;
- física transmite os bits.

No destino, ocorre o **desencapsulamento**.

### Termos importantes
- **Dados**: camada de aplicação
- **Segmento**: TCP
- **Datagrama**: UDP
- **Pacote**: IP
- **Quadro**: enlace
- **Bits**: física

---

## O que memorizar
- ordem das camadas OSI;
- equivalência OSI × TCP/IP;
- conceito de encapsulamento;
- função principal de cada camada.

---

## Sintaxe e comandos úteis
### Ver IP da máquina
```bash
ip addr
```

### Ver interfaces de rede
```bash
ip link
```

### Ver tabela ARP/neighbor
```bash
ip neigh
```

### Ver rotas
```bash
ip route
```

### Flags úteis do comando `ip`
```bash
ip addr show
ip route show
ip link show
```

---

# 2. Endereçamento IP: classes, endereços especiais, máscaras e CIDR

## Conceito central
O endereço IP identifica logicamente um dispositivo dentro de uma rede. Ele permite localizar origem e destino de pacotes.

---

## IPv4
O **IPv4** possui **32 bits**, normalmente representados em quatro octetos decimais.

Exemplo:
```text
192.168.1.10
```

Cada octeto vai de `0` a `255`.

---

## Classes IPv4
Embora o uso atual seja dominado por **CIDR**, o estudo de classes continua sendo cobrado.

| Classe | Primeiro octeto | Uso tradicional |
|---|---:|---|
| A | 1–126 | Redes grandes |
| B | 128–191 | Redes médias |
| C | 192–223 | Redes pequenas |
| D | 224–239 | Multicast |
| E | 240–255 | Reservada |

### Observações
- `127.x.x.x` é reservado para **loopback**.
- `0.x.x.x` possui uso especial.
- Hoje, a divisão por classes foi amplamente substituída por **CIDR**.

---

## Endereços especiais
### Loopback
```text
127.0.0.1
```
Representa a própria máquina.

### Endereço não especificado
```text
0.0.0.0
```
Indica ausência de endereço definido.

### Broadcast geral
```text
255.255.255.255
```
Envia para todos os hosts da rede local, dependendo do contexto.

### Faixas privadas
- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

Esses IPs não são roteáveis publicamente na Internet.

---

## Máscara de rede
A máscara define quais bits representam:
- **rede**
- **host**

Exemplo:
```text
IP:       192.168.1.10
Máscara:  255.255.255.0
CIDR:     /24
```

Resultado:
- Rede: `192.168.1.0`
- Host: `10`
- Broadcast: `192.168.1.255`

---

## CIDR
**CIDR (Classless Inter-Domain Routing)** representa a quantidade de bits da rede.

Exemplos:
- `/24` → `255.255.255.0`
- `/16` → `255.255.0.0`
- `/8` → `255.0.0.0`

Quanto maior o número após a barra, menor a quantidade de hosts possíveis.

---

## Exemplo rápido de cálculo
Rede:
```text
192.168.1.0/24
```

- total de endereços: 256
- hosts utilizáveis: 254
- rede: `192.168.1.0`
- broadcast: `192.168.1.255`

---

## O que memorizar
- diferença entre IP público e privado;
- loopback;
- broadcast;
- máscara e CIDR;
- cálculo básico de sub-rede.

---

## Sintaxe e comandos úteis
### Mostrar IP e máscara
```bash
ip addr show
```

### Testar conectividade
```bash
ping 192.168.1.1
```

### Flags comuns do `ping`
```bash
ping -c 4 8.8.8.8
ping -i 0.5 8.8.8.8
ping -s 1000 8.8.8.8
```

#### Significado
- `-c 4` → envia 4 pacotes
- `-i 0.5` → intervalo de 0,5 s
- `-s 1000` → tamanho da carga útil

---

# 3. Camada de rede: funcionalidades, roteamento e ICMP

## Conceito central
A camada de rede é responsável por permitir a comunicação entre redes diferentes. Ela trata do **endereçamento lógico** e do **encaminhamento de pacotes**.

---

## Funções principais
- endereçamento IP;
- roteamento;
- encaminhamento;
- fragmentação;
- controle básico de alcance entre redes.

---

## Protocolo IP
O IP é o protocolo fundamental dessa camada.

### Características do IP
- não orientado à conexão;
- sem garantia de entrega;
- sem garantia de ordem;
- sem retransmissão nativa;
- entrega do tipo **best effort**.

Isso significa que o IP tenta entregar o pacote, mas não garante o sucesso.

---

## ICMP
O **ICMP (Internet Control Message Protocol)** é usado para mensagens de controle e diagnóstico.

### Mensagens conhecidas
- Echo Request
- Echo Reply
- Destination Unreachable
- Time Exceeded
- Redirect

### Aplicações práticas
- `ping` usa ICMP
- `traceroute` usa ICMP ou UDP, dependendo do sistema

---

## Sintaxe útil
### Ping
```bash
ping -c 4 8.8.8.8
```

### Traceroute
```bash
traceroute 8.8.8.8
```

### Em alguns sistemas
```bash
tracepath 8.8.8.8
```

### Flags comuns do `traceroute`
```bash
traceroute -n 8.8.8.8
traceroute -I 8.8.8.8
traceroute -m 10 8.8.8.8
```

#### Significado
- `-n` → não resolve nomes
- `-I` → usa ICMP
- `-m 10` → limite máximo de saltos

---

## O que memorizar
- função da camada de rede;
- papel do IP;
- papel do ICMP;
- relação de ICMP com diagnóstico.

---

# 4. Roteamento de pacotes: arquitetura e protocolos

## Conceito central
Roteamento é o processo de selecionar o melhor caminho para enviar um pacote da origem ao destino através de múltiplas redes.

---

## Roteador
O roteador:
- analisa o IP de destino;
- consulta a tabela de roteamento;
- decide a interface de saída;
- encaminha o pacote ao próximo salto.

---

## Tabela de roteamento
A tabela de roteamento contém:
- rede de destino;
- máscara ou prefixo CIDR;
- gateway ou próximo salto;
- interface;
- métrica.

---

## Tipos de roteamento
## Estático
Configurado manualmente.

### Vantagens
- simples;
- previsível;
- baixo overhead.

### Desvantagens
- pouco escalável;
- difícil de manter em ambientes grandes.

## Dinâmico
Aprende e atualiza rotas automaticamente.

### Vantagens
- adaptável;
- escalável;
- reage a mudanças de topologia.

### Desvantagens
- mais complexo;
- consome recursos.

---

## Protocolos de roteamento
### RIP
- simples;
- baseado em contagem de saltos;
- limitado para ambientes maiores.

### OSPF
- estado de enlace;
- convergência melhor;
- muito usado em redes corporativas.

### BGP
- protocolo entre sistemas autônomos;
- base da Internet.

### EIGRP
- tradicionalmente associado a ambientes Cisco.

---

## Sintaxe e comandos úteis
### Ver tabela de roteamento
```bash
ip route
```

### Exemplo de saída típica
```text
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.10
```

### Adicionar rota estática
```bash
sudo ip route add 10.10.10.0/24 via 192.168.1.1
```

### Remover rota
```bash
sudo ip route del 10.10.10.0/24 via 192.168.1.1
```

---

## O que memorizar
- diferença entre roteamento estático e dinâmico;
- função da tabela de roteamento;
- finalidade dos protocolos de roteamento;
- conceito de gateway padrão.

---

# 5. Camada de transporte: TCP, UDP e mecanismos de controle

## Conceito central
A camada de transporte realiza a comunicação **fim a fim** entre processos em hosts diferentes. Ela usa **portas** para identificar aplicações.

---

## Funções principais
- segmentação;
- multiplexação por portas;
- controle de fluxo;
- controle de erro;
- confiabilidade, quando aplicável.

---

## TCP
O **TCP (Transmission Control Protocol)** é:
- orientado à conexão;
- confiável;
- ordenado;
- baseado em confirmação de recebimento.

### Recursos do TCP
- handshake de 3 vias;
- ACK;
- retransmissão;
- controle de fluxo;
- controle de congestionamento.

### Handshake de 3 vias
1. SYN
2. SYN-ACK
3. ACK

---

## UDP
O **UDP (User Datagram Protocol)** é:
- sem conexão;
- mais leve;
- sem confirmação;
- sem garantia de entrega ou ordem.

É útil quando:
- baixa latência é mais importante que confiabilidade;
- a aplicação já trata perda ou reordenação.

---

## Portas
Portas identificam processos ou serviços.

### Exemplos clássicos
- `80` → HTTP
- `443` → HTTPS
- `22` → SSH
- `53` → DNS
- `25` → SMTP

---

## Sintaxe e comandos úteis
### Ver conexões ativas
```bash
ss -tulpen
```

### Flags do `ss`
- `-t` → TCP
- `-u` → UDP
- `-l` → listening
- `-p` → processo
- `-e` → informações extras
- `-n` → sem resolver nomes

Exemplo:
```bash
ss -tunap
```

### Alternativa antiga
```bash
netstat -tulnp
```

---

## O que memorizar
- diferença entre TCP e UDP;
- handshake de 3 vias;
- portas;
- confiabilidade do TCP;
- situações de uso de UDP.

---

# 6. Camada de aplicação: DNS, HTTP e tipos de conexão

## Conceito central
A camada de aplicação reúne protocolos que oferecem serviços diretamente aos softwares utilizados pelo usuário.

---

## DNS
O **DNS (Domain Name System)** traduz nomes em endereços IP.

Exemplo:
```text
www.exemplo.com -> 203.0.113.10
```

### Tipos de registro importantes
- `A` → IPv4
- `AAAA` → IPv6
- `MX` → e-mail
- `NS` → servidor autoritativo
- `CNAME` → alias
- `TXT` → texto/validação/políticas

---

## Sintaxe DNS
### Usando `dig`
```bash
dig example.com
dig example.com A
dig example.com MX
dig +short example.com
```

### Flags/opções úteis do `dig`
- `+short` → saída resumida
- `@8.8.8.8` → consulta servidor específico

Exemplo:
```bash
dig @8.8.8.8 example.com A +short
```

### Usando `nslookup`
```bash
nslookup example.com
```

---

## HTTP
O **HTTP** é o protocolo de comunicação entre cliente e servidor web.

### Métodos comuns
- `GET`
- `POST`
- `PUT`
- `DELETE`
- `HEAD`

### Códigos de status
- `200` → OK
- `301` → redirecionamento
- `400` → requisição inválida
- `401` → não autenticado
- `403` → proibido
- `404` → não encontrado
- `500` → erro interno

---

## Sintaxe útil com `curl`
### Fazer requisição GET
```bash
curl http://example.com
```

### Mostrar cabeçalhos
```bash
curl -I http://example.com
```

### Seguir redirecionamento
```bash
curl -L http://example.com
```

### Requisição POST
```bash
curl -X POST http://example.com/api -d "nome=teste"
```

### Flags comuns do `curl`
- `-I` → apenas cabeçalhos
- `-L` → segue redirecionamento
- `-X` → define método HTTP
- `-d` → envia dados
- `-H` → cabeçalho customizado
- `-k` → ignora verificação TLS
- `-v` → modo verboso

Exemplo:
```bash
curl -v -H "Accept: application/json" https://example.com
```

---

## HTTPS
É o HTTP protegido por **TLS**.

Ele fornece:
- confidencialidade;
- integridade;
- autenticação do servidor.

---

## O que memorizar
- função do DNS;
- tipos de registro;
- função do HTTP;
- diferença entre HTTP e HTTPS;
- requisição e resposta.

---

# 7. Acesso remoto seguro: SSH, TLS/SSL e SFTP

## Conceito central
Acesso remoto seguro envolve proteger a comunicação contra:
- leitura indevida;
- alteração indevida;
- falsificação de identidade.

---

## Princípios fundamentais
### Confidencialidade
Somente partes autorizadas devem ler o conteúdo.

### Integridade
Os dados não devem ser alterados indevidamente.

### Autenticação
É preciso verificar a identidade das partes.

---

## SSH
O **SSH (Secure Shell)** permite acesso remoto seguro.

### Usos comuns
- acesso a terminal remoto;
- administração de servidores;
- tunelamento;
- cópia segura de arquivos.

### Sintaxe básica
```bash
ssh usuario@host
```

### Especificar porta
```bash
ssh -p 2222 usuario@host
```

### Usar chave privada
```bash
ssh -i ~/.ssh/id_rsa usuario@host
```

### Flags importantes do `ssh`
- `-p` → porta
- `-i` → arquivo de chave
- `-v` → verbose
- `-L` → túnel local
- `-R` → túnel reverso

Exemplo:
```bash
ssh -v -p 22 usuario@192.168.1.20
```

---

## TLS/SSL
O **TLS** protege sessões de comunicação. O termo SSL ainda é usado historicamente, mas o protocolo moderno é o TLS.

### Aplicações
- HTTPS
- SMTPS
- IMAPS
- VPNs e outras soluções seguras

### Conceitos importantes
- certificado digital;
- chave pública e privada;
- autoridade certificadora;
- handshake TLS.

---

## SFTP
O **SFTP** permite transferência segura de arquivos, normalmente sobre SSH.

### Sintaxe
```bash
sftp usuario@host
```

### Especificar porta
```bash
sftp -P 2222 usuario@host
```

### Comandos internos do SFTP
```text
ls
pwd
cd
get arquivo.txt
put arquivo.txt
exit
```

---

## SCP
Embora não esteja no seu tópico principal, costuma ser cobrado junto.

### Enviar arquivo
```bash
scp arquivo.txt usuario@host:/tmp/
```

### Baixar arquivo
```bash
scp usuario@host:/tmp/arquivo.txt .
```

---

## O que memorizar
- finalidade do SSH;
- finalidade do TLS;
- diferença entre SSH, TLS e SFTP;
- diferença entre FTP e SFTP;
- importância de autenticação, integridade e criptografia.

---

# 8. Filtros para análise de tráfego

## Conceito central
Filtros permitem reduzir volume de dados e focar no tráfego relevante.

---

## Tipos de filtros
## Filtros de captura
Aplicados antes da captura. Diminuem o que será coletado.

## Filtros de exibição
Aplicados depois da captura. Não alteram o arquivo, apenas a visualização.

---

## Exemplos de filtros de exibição no Wireshark
```text
ip.addr == 192.168.1.10
ip.src == 10.0.0.5
ip.dst == 8.8.8.8
tcp
udp
dns
http
icmp
tcp.port == 80
tcp.flags.syn == 1
```

---

## Exemplos de filtros de captura no tcpdump/Wireshark
```bash
tcpdump host 192.168.1.10
tcpdump src host 10.0.0.5
tcpdump dst port 53
tcpdump tcp
tcpdump udp
tcpdump icmp
```

### Sintaxe útil com `tcpdump`
```bash
sudo tcpdump -i eth0
sudo tcpdump -i eth0 host 192.168.1.10
sudo tcpdump -i eth0 port 80
sudo tcpdump -i eth0 -nn
sudo tcpdump -i eth0 -w captura.pcap
```

### Flags importantes do `tcpdump`
- `-i` → interface
- `-n` → não resolve nomes
- `-nn` → não resolve nomes nem portas
- `-w` → salva em arquivo
- `-r` → lê arquivo salvo
- `-c` → limita quantidade de pacotes
- `-v`, `-vv`, `-vvv` → mais detalhes

Exemplo:
```bash
sudo tcpdump -i eth0 -nn -c 20 tcp port 80
```

---

## Usando `tshark`
```bash
tshark -r captura.pcap
tshark -r captura.pcap -Y "dns"
tshark -r captura.pcap -Y "tcp.port == 443"
```

### Flags úteis do `tshark`
- `-r` → lê arquivo
- `-Y` → filtro de exibição
- `-i` → captura em interface
- `-w` → grava captura

---

## O que memorizar
- diferença entre filtro de captura e exibição;
- sintaxe básica de filtros;
- uso de `tcpdump`, `tshark` e Wireshark.

---

# 9. Interpretação de tráfego de rede

## Conceito central
Analisar tráfego não é apenas identificar pacotes, mas entender o **comportamento da comunicação**.

---

## O que observar
- origem e destino;
- portas;
- protocolo utilizado;
- sequência temporal;
- início e término da sessão;
- volume;
- repetição;
- erros;
- retransmissões;
- ausência de resposta.

---

## Padrões comuns de interpretação
### Muitos pacotes DNS
Pode indicar:
- navegação intensa;
- serviços consultando nomes;
- falha de cache;
- alta dependência de resolução de nomes.

### SYN repetidos sem resposta
Pode indicar:
- porta fechada;
- filtro/firewall;
- host indisponível;
- rota incorreta.

### ICMP Destination Unreachable
Pode indicar:
- destino inacessível;
- falha de rota;
- serviço indisponível;
- bloqueio intermediário.

### Retransmissões TCP
Pode indicar:
- perda de pacotes;
- congestionamento;
- latência elevada;
- problema de qualidade de enlace.

### Requisição DNS seguida de conexão TCP/HTTP
Mostra o fluxo natural:
1. resolução de nome;
2. obtenção de IP;
3. abertura de conexão;
4. troca de dados.

---

## Perguntas que você deve saber responder
- Quem iniciou a comunicação?
- Qual protocolo foi usado?
- Houve resposta?
- Houve erro?
- A sessão foi concluída?
- Onde está o provável ponto de falha?

---

# 10. Análise de arquivos capturados (.pcap e .pcapng)

## Conceito central
Arquivos `.pcap` e `.pcapng` armazenam pacotes para análise posterior.

Isso permite:
- revisar incidentes;
- estudar protocolos;
- investigar falhas;
- documentar comportamento de rede.

---

## Fluxo de análise recomendado
### 1. Abrir a captura
Ferramentas:
- Wireshark
- tshark
- tcpdump

### 2. Identificar hosts principais
Ver quais IPs mais aparecem.

### 3. Identificar protocolos
Exemplo:
- ARP
- DNS
- ICMP
- TCP
- HTTP
- TLS

### 4. Filtrar o que importa
Aplicar filtros de IP, porta, protocolo ou flags.

### 5. Observar cronologia
Ver a ordem dos eventos.

### 6. Interpretar o resultado
Relacionar protocolo, destino, resposta, erros e conclusão.

---

## O que procurar numa captura
- IP de origem e destino;
- portas de origem e destino;
- handshake TCP;
- consultas DNS;
- requisições HTTP;
- alertas ICMP;
- retransmissões;
- reset TCP (`RST`);
- encerramento com `FIN`.

---

## Exemplo de fluxo esperado numa navegação web
1. Consulta DNS:
```text
Cliente -> DNS: Qual é o IP de www.site.com?
```

2. Resposta DNS:
```text
DNS -> Cliente: www.site.com = 203.0.113.10
```

3. Abertura TCP:
```text
SYN -> SYN/ACK -> ACK
```

4. Requisição HTTP:
```text
GET / HTTP/1.1
```

5. Resposta:
```text
HTTP/1.1 200 OK
```

---

## Comandos úteis
### Ler arquivo com `tcpdump`
```bash
tcpdump -r captura.pcap
```

### Ler com mais detalhes
```bash
tcpdump -nn -r captura.pcap
```

### Filtrar arquivo
```bash
tcpdump -nn -r captura.pcap port 53
```

### Ler com `tshark`
```bash
tshark -r captura.pcap -Y "icmp"
```

---

# Bloco extra — comandos essenciais para revisão

## Diagnóstico básico
```bash
ip addr
ip route
ping -c 4 8.8.8.8
traceroute 8.8.8.8
ss -tulpen
```

## DNS
```bash
dig example.com
dig +short example.com
nslookup example.com
```

## HTTP
```bash
curl -I https://example.com
curl -v https://example.com
curl -L http://example.com
```

## SSH/SFTP
```bash
ssh usuario@host
ssh -p 2222 usuario@host
sftp usuario@host
scp arquivo.txt usuario@host:/tmp/
```

## Captura/análise
```bash
sudo tcpdump -i eth0 -nn
sudo tcpdump -i eth0 -w captura.pcap
tshark -r captura.pcap -Y "dns"
```

---

# Resumo de memorização rápida

## Você precisa saber bem:
- camadas OSI e TCP/IP;
- encapsulamento;
- IP, máscara, CIDR, broadcast e loopback;
- função de IP e ICMP;
- roteamento e tabela de rotas;
- diferença entre TCP e UDP;
- DNS, HTTP e HTTPS;
- SSH, TLS e SFTP;
- filtros em Wireshark/tcpdump;
- leitura de `.pcap`.

---

# Questões de fixação

1. Qual é a diferença entre o modelo OSI e o modelo TCP/IP?  
2. O que significa `/24` em CIDR?  
3. Qual é a função do protocolo ICMP?  
4. Para que serve uma tabela de roteamento?  
5. Qual a diferença prática entre TCP e UDP?  
6. O que o DNS resolve?  
7. Qual a diferença entre HTTP e HTTPS?  
8. O que faz o comando `ssh -p 2222 usuario@host`?  
9. Qual a diferença entre filtro de captura e filtro de exibição?  
10. O que significa observar vários `SYN` sem `SYN-ACK`?
