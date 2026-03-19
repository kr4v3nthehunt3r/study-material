# Resumo para Estudo — Redes, TCP/IP e Wireshark

## Visão geral

Este material explica **como os dispositivos se comunicam em rede**, **como os dados passam por camadas**, **como funcionam protocolos como IP, TCP, UDP, DNS, HTTP e SMTP** e **como o Wireshark permite analisar tudo isso na prática**.

---

## 1. O que é uma rede de computadores

Uma rede de computadores é um conjunto de dispositivos conectados para compartilhar:

- informações
- serviços
- recursos

### Exemplos de dispositivos
- computadores
- notebooks
- servidores
- switches
- roteadores
- firewalls
- dispositivos IoT

### Ideia-chave
**Rede = comunicação entre dispositivos.**

---

## 2. Protocolos e camadas

Os **protocolos** são regras que permitem a comunicação entre os dispositivos.

Para facilitar o entendimento e a organização, a comunicação é dividida em **camadas**.

### Modelo OSI
Modelo teórico com 7 camadas:

1. Física  
2. Enlace  
3. Rede  
4. Transporte  
5. Sessão  
6. Apresentação  
7. Aplicação  

### Modelo TCP/IP
Modelo usado na prática:

1. Acesso à Rede  
2. Internet  
3. Transporte  
4. Aplicação  

### Macete
- **OSI = modelo didático**
- **TCP/IP = modelo real de uso**

---

## 3. Encapsulamento e desencapsulamento

### Encapsulamento
Quando os dados descem pelas camadas no envio, cada camada adiciona informações de controle.

### Desencapsulamento
Quando os dados chegam ao destino, cada camada remove sua parte até a aplicação receber a mensagem final.

### Macete
- **Encapsular = adicionar informações**
- **Desencapsular = remover informações**

---

## 4. Endereçamento IP

O endereço IP identifica um dispositivo na rede.

### IPv4
- possui **32 bits**
- é dividido em **4 octetos**
- exemplo: `192.168.1.10`

### Conceitos importantes
- **Endereço de rede**: identifica a rede
- **Endereço de broadcast**: envia para todos os hosts da rede
- **Hosts utilizáveis**: endereços entre rede e broadcast
- **Máscara de sub-rede**: separa rede e host
- **CIDR**: forma compacta de representar a máscara, como `/24`

### Exemplo rápido
Em uma rede `/24`:
- rede: `192.168.1.0`
- broadcast: `192.168.1.255`
- hosts válidos: `192.168.1.1` até `192.168.1.254`

---

## 5. IPv6

O IPv6 foi criado para resolver a limitação de endereços do IPv4.

### Características
- possui **128 bits**
- usa **hexadecimal**
- exemplo: `2001:db8::1`

### Vantagem principal
Oferece uma quantidade muito maior de endereços.

### Macete
- **IPv4 = 32 bits**
- **IPv6 = 128 bits**

---

## 6. Camada de Rede

A camada de rede é responsável por levar os pacotes entre origem e destino.

### Principais protocolos
- **IP**: endereçamento e roteamento
- **ICMP**: mensagens de controle e erro

### ICMP na prática
Usado em situações como:
- teste de conectividade (`ping`)
- aviso de destino inacessível
- tempo excedido (`traceroute`)

### Macete
- **IP = entrega**
- **ICMP = aviso e controle**

---

## 7. Camada de Transporte

Responsável pela comunicação entre processos de origem e destino.

### TCP
- orientado à conexão
- confiável
- garante ordem
- faz controle de erro
- usa confirmação de recebimento

### UDP
- não orientado à conexão
- mais simples e rápido
- não garante entrega
- não garante ordem

### Quando lembrar de cada um
- **TCP**: quando confiabilidade importa
- **UDP**: quando velocidade importa

### Macete
- **TCP = confiável**
- **UDP = rápido**

---

## 8. Portas

As portas identificam serviços e aplicações em cada host.

### Exemplos comuns
- `80` → HTTP
- `443` → HTTPS
- `53` → DNS
- `25` → SMTP

### Ideia-chave
**IP identifica o dispositivo; porta identifica o serviço.**

---

## 9. Camada de Aplicação

É a camada mais próxima do usuário.

Aqui ficam os protocolos usados diretamente pelos programas.

### Principais protocolos estudados
- **DNS**
- **HTTP**
- **SMTP**
- **FTP**

---

## 10. DNS

O DNS converte nomes em endereços IP.

### Exemplo
Em vez de decorar um IP numérico, usamos um nome como:
`www.exemplo.com`

O DNS faz a tradução desse nome para o IP correspondente.

### Macete
**DNS = traduz nome em IP**

---

## 11. HTTP

O HTTP é o protocolo usado na navegação web.

### Métodos comuns
- **GET** → solicitar dados
- **POST** → enviar dados

### Códigos de resposta comuns
- **200** → OK
- **301** → redirecionamento
- **404** → não encontrado
- **505** → versão HTTP não suportada

### Macete
**HTTP = comunicação da web**

---

## 12. SMTP

O SMTP é o protocolo usado para envio de e-mails.

### Comandos comuns
- `HELO` / `EHLO`
- `MAIL FROM`
- `RCPT TO`
- `DATA`
- `QUIT`
- `STARTTLS`

### Macete
**SMTP = envio de e-mail**

---

## 13. Wireshark

O Wireshark é uma ferramenta de análise de tráfego de rede.

Ele permite:
- capturar pacotes em tempo real
- abrir arquivos `.pcap`
- visualizar protocolos
- analisar IPs e portas
- inspecionar cabeçalhos
- reconstruir conversas

### Para que serve
- estudar protocolos
- identificar problemas de rede
- analisar tráfego suspeito
- entender o fluxo de comunicação

### Macete
**Wireshark = raio-X da rede**

---

## 14. Filtros no Wireshark

### Filtros de captura
Aplicados antes da captura.

### Filtros de exibição
Aplicados depois da captura.

### Exemplos
```text
ip.addr == 192.168.0.1
tcp.port == 80
udp.port == 53
```

### Ideia-chave
- **captura** = filtra antes
- **exibição** = filtra depois

---

## 15. HTTPS e TLS

### HTTP
Envia dados sem criptografia.

### HTTPS
Usa **TLS** para criptografar a comunicação.

### No Wireshark
É comum encontrar:
- porta `443`
- mensagens como `Client Hello`
- mensagens como `Server Hello`

### Macete
- **HTTP = sem criptografia**
- **HTTPS = com criptografia**

---

## 16. Funções úteis do Wireshark

### Recursos importantes
- **Protocol Hierarchy**
- **Conversations**
- **Endpoints**
- **IO Graphs**
- **Follow TCP Stream**
- **Follow UDP Stream**

### Para que ajudam
- ver quais protocolos aparecem mais
- identificar quem conversa com quem
- analisar volume de tráfego
- reconstruir sessões completas

---

## Resumo-relâmpago

- **Rede** = ligação entre dispositivos  
- **Protocolo** = regra de comunicação  
- **OSI** = modelo teórico  
- **TCP/IP** = modelo prático  
- **IPv4** = 32 bits  
- **IPv6** = 128 bits  
- **IP** = endereçamento e roteamento  
- **ICMP** = mensagens de controle  
- **TCP** = confiável  
- **UDP** = rápido  
- **DNS** = traduz nome para IP  
- **HTTP** = navegação web  
- **SMTP** = envio de e-mail  
- **Wireshark** = análise de pacotes  

---

## Mnemônico final

**IP localiza, TCP garante, UDP agiliza, DNS traduz, HTTP navega, SMTP envia e o Wireshark mostra tudo.**

---

## Perguntas rápidas para revisão

### 1. Qual a diferença entre OSI e TCP/IP?
O OSI é um modelo teórico; o TCP/IP é o modelo usado na prática.

### 2. O que é encapsulamento?
É o processo de adicionar informações de controle em cada camada no envio dos dados.

### 3. Qual a principal função do IP?
Identificar dispositivos e permitir o roteamento dos pacotes.

### 4. Qual a diferença entre TCP e UDP?
TCP é confiável e orientado à conexão; UDP é mais simples, rápido e sem garantia de entrega.

### 5. O que o DNS faz?
Traduz nomes de domínio em endereços IP.

### 6. Para que serve o Wireshark?
Capturar e analisar pacotes de rede.

### 7. Qual a diferença entre HTTP e HTTPS?
HTTPS usa criptografia com TLS; HTTP não usa.

---

## Fechamento

Para estudar melhor, memorize nesta ordem:

**Rede → Camadas → IP → TCP/UDP → DNS/HTTP/SMTP → Wireshark**

Essa sequência ajuda a entender a lógica completa da comunicação em redes.
