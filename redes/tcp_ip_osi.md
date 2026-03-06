# Folha de Revisão Padronizada — TCP/IP, OSI, IP, TCP e HTTP

## 1. Modelo OSI

| Camada | Nome | Função Principal | Unidade de Dados | Exemplos |
|---:|---|---|---|---|
| 7 | Aplicação | Fornece serviços de rede às aplicações do usuário | Dados | HTTP, FTP, SMTP, DNS, SSH |
| 6 | Apresentação | Realiza tradução, compressão e criptografia dos dados | Dados | ASCII, JPEG, TLS |
| 5 | Sessão | Estabelece, mantém e encerra sessões de comunicação | Dados | Controle de diálogo |
| 4 | Transporte | Garante a comunicação fim a fim entre aplicações | Segmento | TCP, UDP |
| 3 | Rede | Realiza endereçamento lógico e roteamento | Pacote | IP, ICMP |
| 2 | Enlace | Organiza os dados em quadros e usa endereços físicos | Quadro | Ethernet, PPP |
| 1 | Física | Transmite bits pelo meio físico | Bit | UTP, fibra óptica, coaxial, wireless |

## 2. Resumo das Camadas do Modelo OSI

| Camada | Palavra-chave | Ponto Principal |
|---|---|---|
| Física | Bits | Meio físico e sinais |
| Enlace | MAC | Quadros, FCS e acesso ao meio |
| Rede | IP | Endereçamento lógico e roteamento |
| Transporte | Portas | Comunicação fim a fim |
| Sessão | Diálogo | Controle da sessão |
| Apresentação | Formato | Tradução, compressão e criptografia |
| Aplicação | Serviços | Interface com o usuário |

## 3. Encapsulamento dos Dados

| Camada | Unidade de Dados |
|---|---|
| Aplicação | Dados |
| Apresentação | Dados |
| Sessão | Dados |
| Transporte | Segmento |
| Rede | Pacote |
| Enlace | Quadro |
| Física | Bit |

## 4. Cabeçalho TCP

| Campo | Tamanho | Função |
|---|---:|---|
| Porta de Origem | 16 bits | Identifica a aplicação emissora |
| Porta de Destino | 16 bits | Identifica a aplicação receptora |
| Número de Sequência | 32 bits | Controla a ordem dos bytes transmitidos |
| Número de Acknowledgment | 32 bits | Confirma o recebimento dos dados |
| Data Offset | 4 bits | Indica o tamanho do cabeçalho TCP |
| Reservado | 3 bits | Reservado para uso futuro |
| Flags | 9 bits | Controlam o estado da conexão |
| Tamanho da Janela | 16 bits | Controla o fluxo de dados |
| Checksum | 16 bits | Verifica a integridade do segmento |
| Ponteiro de Urgência | 16 bits | Indica dados urgentes quando URG está ativa |
| Opções | Variável | Define parâmetros adicionais, como MSS |
| Padding | Variável | Alinha o cabeçalho em múltiplos de 32 bits |
| Dados | Variável | Conteúdo transportado pelo segmento |

## 5. Flags do TCP

| Flag | Nome | Função |
|---|---|---|
| SYN | Synchronize | Inicia a conexão |
| ACK | Acknowledgment | Confirma o recebimento |
| FIN | Finish | Encerra a conexão |
| RST | Reset | Reinicia ou aborta a conexão |
| PSH | Push | Entrega os dados imediatamente à aplicação |
| URG | Urgent | Indica presença de dados urgentes |

## 6. Comparação entre TCP e UDP

| Protocolo | Tipo de Comunicação | Vantagem | Limitação |
|---|---|---|---|
| TCP | Orientado à conexão | Confiável e ordenado | Maior overhead |
| UDP | Não orientado à conexão | Simples e rápido | Não garante entrega |

## 7. Cabeçalho IP (IPv4)

| Campo | Tamanho | Função |
|---|---:|---|
| Versão | 4 bits | Indica a versão do protocolo IP |
| IHL | 4 bits | Informa o tamanho do cabeçalho IP |
| ToS / DSCP | 8 bits | Define prioridade e tratamento do pacote |
| Comprimento Total | 16 bits | Indica o tamanho total do pacote |
| Identificação | 16 bits | Identifica fragmentos do mesmo pacote |
| Flags | 3 bits | Controlam a fragmentação |
| Offset do Fragmento | 13 bits | Indica a posição do fragmento |
| TTL | 8 bits | Limita a vida útil do pacote |
| Protocolo | 8 bits | Indica o protocolo da camada superior |
| Checksum do Cabeçalho | 16 bits | Verifica a integridade do cabeçalho IP |
| Endereço IP de Origem | 32 bits | Identifica o host emissor |
| Endereço IP de Destino | 32 bits | Identifica o host receptor |
| Opções | Variável | Permite funções adicionais |

## 8. Valores do Campo Protocolo no IP

| Valor | Protocolo |
|---:|---|
| 1 | ICMP |
| 6 | TCP |
| 17 | UDP |

## 9. Cabeçalho HTTP

| Campo | Exemplo | Função |
|---|---|---|
| Método | GET, POST, PUT, DELETE | Define a ação da requisição |
| URL | /index.html | Identifica o recurso solicitado |
| Versão HTTP | HTTP/1.1 | Indica a versão do protocolo |
| Host | www.exemplo.com | Identifica o servidor de destino |
| User-Agent | Mozilla/5.0 | Identifica o cliente |
| Content-Type | application/json | Define o tipo do conteúdo |
| Content-Length | 1234 | Indica o tamanho do corpo da mensagem |
| Connection | keep-alive | Define o comportamento da conexão |

## 10. Endereço Físico x Endereço Lógico

| Tipo de Endereço | Camada | Exemplo | Finalidade |
|---|---|---|---|
| Endereço Físico | Enlace | MAC Address | Identificar a interface na rede local |
| Endereço Lógico | Rede | IP Address | Identificar o host entre redes |

## 11. Comparação entre Protocolos

| Protocolo | Camada | Função Principal |
|---|---|---|
| TCP | Transporte | Garantir entrega confiável |
| UDP | Transporte | Fornecer entrega rápida e simples |
| IP | Rede | Realizar endereçamento e roteamento |
| HTTP | Aplicação | Permitir comunicação web |

## 12. Fluxo da Comunicação em Rede

| Etapa | Descrição |
|---|---|
| Aplicação | Gera os dados, como uma requisição HTTP |
| Transporte | Adiciona portas e segmenta os dados |
| Rede | Adiciona endereços IP e define o roteamento |
| Enlace | Cria o quadro com MAC e FCS |
| Física | Transmite os bits pelo meio físico |

## 13. Resumo para Prova

| Pergunta | Resposta |
|---|---|
| TCP pertence a qual camada? | Camada de Transporte |
| UDP pertence a qual camada? | Camada de Transporte |
| IP pertence a qual camada? | Camada de Rede |
| HTTP pertence a qual camada? | Camada de Aplicação |
| Qual camada usa portas? | Camada de Transporte |
| Qual camada usa IP? | Camada de Rede |
| Qual camada usa MAC? | Camada de Enlace |
| Unidade da Camada de Transporte | Segmento |
| Unidade da Camada de Rede | Pacote |
| Unidade da Camada de Enlace | Quadro |
| Unidade da Camada Física | Bit |

## 14. Ordem das Camadas do Modelo OSI

| Ordem | Camada |
|---:|---|
| 7 | Aplicação |
| 6 | Apresentação |
| 5 | Sessão |
| 4 | Transporte |
| 3 | Rede |
| 2 | Enlace |
| 1 | Física |
