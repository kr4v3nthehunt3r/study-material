# Resumo final 100% completo em tabelas — SO Windows_2026

> Documento resumido integralmente em formato tabular, cobrindo todas as seções, abertura, sumário e encerramento.

## 1. Identificação do material

| Campo | Conteúdo |
|---|---|
| Arquivo-base | SO Windows_2026.pdf |
| Curso | Curso de Guerra Cibernética 2026 |
| Instituição | Centro de Instrução de Guerra Eletrônica |
| Assunto | SO Windows |
| Instrutor | Cap Trindade |
| Trilha apresentada no PDF | 1º Sistema Operacional Windows; 2º Exploração Windows; 3º Active Directory (AD) |
| Extensão do material | 188 páginas no PDF, sendo 16 seções temáticas, além de capa, sumário e encerramento |
| Abordagem geral | Material introdutório-prático com ênfase em administração local do Windows, linha de comando, rede, segurança, eventos e noções iniciais de coleta/análise técnica |

## 2. Páginas preliminares e estrutura geral

| Página | Conteúdo |
|---|---|
| 1 | Capa institucional do Curso de Guerra Cibernética 2026. |
| 2 | Identificação do assunto ('SO Windows') e do instrutor (Cap Trindade). |
| 3 | Página de abertura com citação motivacional. |
| 4 | Apresenta a trilha didática: Sistema Operacional Windows → Exploração Windows → Active Directory. |
| 5 | Sumário geral com os 16 temas do material. |
| 188 | Página de encerramento ('Obrigado pela atenção de todos'). |

## 3. Mapa geral das 16 seções

| Seção | Título | Páginas | Objetivo principal |
|---|---|---|---|
| 1 | Estrutura de arquivos | 6–10 | Apresentar a organização lógica do armazenamento no Windows, das unidades até as pastas de sistema e perfis de usuário. |
| 2 | Extensões de arquivos | 11–17 | Explicar o papel das extensões, seus limites e a importância de validar o tipo real do arquivo. |
| 3 | Comandos básicos | 18–34 | Introduzir a operação do Windows por linha de comando com ênfase em CMD e apoio de PowerShell. |
| 4 | Permissões | 35–60 | Explicar o modelo de controle de acesso do Windows e o gerenciamento prático de permissões. |
| 5 | Informações do sistema | 61–67 | Mostrar como coletar informações essenciais do host e do Windows para contextualização técnica. |
| 6 | Gerenciamento de usuários e grupos | 68–79 | Apresentar contas locais, grupos e operações administrativas básicas. |
| 7 | Gerenciamento de redes | 80–89 | Mostrar comandos para inspecionar e alterar parâmetros de rede no Windows. |
| 8 | Gerenciamento de firewall | 90–99 | Introduzir consulta do status do firewall e gerenciamento básico de regras. |
| 9 | Gerenciamento de programas, processos e serviços | 100–116 | Diferenciar programas, processos e serviços e mostrar sua administração básica. |
| 10 | Gerenciamento de tarefas agendadas | 117–124 | Apresentar automação por tarefas agendadas e seus diferentes contextos de execução. |
| 11 | Gerenciamento de antivírus | 125–128 | Abordar o gerenciamento do Windows Defender e a verificação do estado de proteção. |
| 12 | Registro do Windows | 129–142 | Introduzir a estrutura do Registro do Windows e as operações básicas sobre chaves e valores. |
| 13 | Log e eventos | 143–150 | Mostrar noções básicas de registro e consulta de eventos do Windows. |
| 14 | Dump de memória RAM | 151–166 | Explicar a relevância da memória volátil e demonstrar um fluxo básico de aquisição com FTK Imager. |
| 15 | Realizar cópia de disco do S.O. Windows | 167–173 | Apresentar o conceito de imagem/clonagem de disco e sua conversão para uso em ambientes virtualizados. |
| 16 | Recuperar arquivos apagados em dispositivos | 174–187 | Apresentar o princípio da recuperação de arquivos excluídos e o uso básico do Recuva. |

## 4. Seção 1 — Estrutura de arquivos

| Campo | Conteúdo |
|---|---|
| Título da seção | Estrutura de arquivos |
| Páginas | 6–10 |
| Objetivo | Apresentar a organização lógica do armazenamento no Windows, das unidades até as pastas de sistema e perfis de usuário. |
| Subtemas centrais | Unidade de disco; diretório raiz; pastas de sistema; subpastas relevantes de C:\Windows; diretórios de usuário. |
| Comandos / ferramentas / recursos | Explorador de Arquivos (conceitual). |
| Pontos-chave para revisão | C:\ como raiz típica do sistema; Program Files, ProgramData, Windows, Users; System32, SysWOW64, Temp, Logs, Installer, SoftwareDistribution, Prefetch; AppData e pastas padrão do perfil. |

### 4.1 Mapa detalhado por página — Seção 1

| Página | Resumo do conteúdo da página |
|---|---|
| 6 | Página de abertura da seção 1. |
| 7 | Introdução visual da seção 'Estrutura de arquivos'. |
| 8 | Explica unidade de disco, diretório raiz e pastas de sistema principais. |
| 9 | Detalha subpastas relevantes de C:\Windows, como System32, SysWOW64, Temp, Logs, Installer, SoftwareDistribution e Prefetch. |
| 10 | Mostra diretórios de usuário e subpastas padrão, incluindo Desktop, Documents, Downloads, Music, Pictures, Videos e AppData. |

## 5. Seção 2 — Extensões de arquivos

| Campo | Conteúdo |
|---|---|
| Título da seção | Extensões de arquivos |
| Páginas | 11–17 |
| Objetivo | Explicar o papel das extensões, seus limites e a importância de validar o tipo real do arquivo. |
| Subtemas centrais | Funcionalidade das extensões; alteração de extensões; extensões ocultas; arquivos do sistema; magic numbers; validação por assinatura. |
| Comandos / ferramentas / recursos | Explorador de Arquivos; PowerShell para leitura de bytes iniciais. |
| Pontos-chave para revisão | Extensão não altera formato interno; exibir itens ocultos; verificar assinatura/binário real; lista de magic numbers comuns. |

### 5.1 Mapa detalhado por página — Seção 2

| Página | Resumo do conteúdo da página |
|---|---|
| 11 | Página de abertura da seção 2. |
| 12 | Define extensões de arquivo e sua funcionalidade para identificação de tipos e associação com programas. |
| 13 | Explica alteração de extensões e visualização de extensões ocultas/arquivos do sistema. |
| 14 | Introduz magic numbers e lista assinaturas de formatos comuns. |
| 15 | Apresenta a pergunta-problema sobre validar se a extensão corresponde ao formato real do arquivo. |
| 16 | Mostra, em PowerShell, a leitura dos primeiros bytes para validar a assinatura do arquivo. |
| 17 | Exemplo/continuação visual da validação de assinaturas. |

## 6. Seção 3 — Comandos básicos

| Campo | Conteúdo |
|---|---|
| Título da seção | Comandos básicos |
| Páginas | 18–34 |
| Objetivo | Introduzir a operação do Windows por linha de comando com ênfase em CMD e apoio de PowerShell. |
| Subtemas centrais | Diferença entre CMD e PowerShell; abertura do terminal; navegação; listagem; busca; manipulação de arquivos; filtros; atributos; integridade via whoami. |
| Comandos / ferramentas / recursos | help, dir, cd, md/mkdir, rd, type, ren, xcopy, del, whoami, tree, shutdown, echo, >, >>, sort, |, 2>nul, attrib, findstr. |
| Pontos-chave para revisão | Abrir terminal normal ou como administrador; usar filtros e redirecionamento; identificar grupos/privilégios; ocultação reforçada com +S +H. |

### 6.1 Mapa detalhado por página — Seção 3

| Página | Resumo do conteúdo da página |
|---|---|
| 18 | Página de abertura da seção 3. |
| 19 | Introdução aos comandos básicos; delimita foco em CMD com apoio de PowerShell. |
| 20 | Compara CMD e PowerShell como CLIs do Windows. |
| 21 | Página ilustrativa comparando CMD e PowerShell. |
| 22 | Mostra como abrir CMD/PowerShell com e sem privilégios administrativos via teclado. |
| 23 | Apresenta o comando help para listar comandos disponíveis. |
| 24 | Apresenta help <comando> e /? para ajuda contextual de um comando. |
| 25 | Explica cls, dir, dir /a, dir /q, busca com curingas, cd, md/mkdir e rd com opções. |
| 26 | Explica type, ren, xcopy (inclusive /e e /s) e del. |
| 27 | Mostra whoami e whoami /priv. |
| 28 | Mostra whoami /groups para visualizar grupos e nível de integridade. |
| 29 | Apresenta tree, tree /f e shutdown com opções de desligar, logoff, reiniciar e forçar. |
| 30 | Explica echo e redirecionadores > e >>. |
| 31 | Explica sort, sort /r, pipe (|) e supressão de erros com 2>nul. |
| 32 | Explica attrib, attrib /d, attrib /s e uso de +S +H. |
| 33 | Comenta o efeito do atributo +S e a ocultação de arquivos protegidos do sistema. |
| 34 | Apresenta findstr para filtrar linhas e buscar conteúdo em múltiplos arquivos. |

## 7. Seção 4 — Permissões

| Campo | Conteúdo |
|---|---|
| Título da seção | Permissões |
| Páginas | 35–60 |
| Objetivo | Explicar o modelo de controle de acesso do Windows e o gerenciamento prático de permissões. |
| Subtemas centrais | ACL, ACE e DACL; herança; permissões básicas; permissões avançadas; grupos internos; uso de icacls; interface gráfica; nível de integridade. |
| Comandos / ferramentas / recursos | icacls; whoami /groups; interface gráfica de Propriedades > Segurança. |
| Pontos-chave para revisão | Diferença entre remover e negar; heranças OI/CI/IO/NP; níveis Low, Medium, High, System e TrustedInstaller. |

### 7.1 Mapa detalhado por página — Seção 4

| Página | Resumo do conteúdo da página |
|---|---|
| 35 | Página de abertura da seção 4. |
| 36 | Define ACL, ACE e DACL e anuncia estudo de permissões básicas, avançadas e heranças. |
| 37 | Explica marcas de herança como I, OI e CI. |
| 38 | Exemplifica herança de permissões com OI, CI, IO e NP em estrutura de diretórios. |
| 39 | Lista permissões básicas como Full access, Modify e Read/Execute. |
| 40 | Inicia as permissões avançadas: Delete, Read Control, Write DAC e correlatas. |
| 41 | Continua permissões avançadas: Maximum allowed, Generic read/write/execute/all. |
| 42 | Continua permissões avançadas: Append Data, Read/Write Extended Attributes, Execute/Traverse e Delete Child. |
| 43 | Introduz o comando icacls para exibir, modificar, fazer backup e restaurar ACLs. |
| 44 | Explica grupos internos (BUILTIN) e o formato de permissões por usuário/grupo local ou de domínio. |
| 45 | Detalha o grupo BUILTIN\Users e permissões usuais de usuários padrão. |
| 46 | Mostra adição de permissões básicas com icacls /grant. |
| 47 | Explica a diferença entre remover permissão e negar permissão. |
| 48 | Exemplo prático visual do impacto de negar permissões. |
| 49 | Mostra a remoção/substituição de permissões com icacls /grant:r. |
| 50 | Mostra como remover todas as permissões concedidas com icacls /remove:g. |
| 51 | Mostra como negar permissões com icacls /deny. |
| 52 | Mostra como remover negações de permissão com icacls /remove:d. |
| 53 | Mostra como adicionar heranças e desabilitar herança convertendo permissões herdadas em explícitas. |
| 54 | Mostra como remover heranças/permissões herdadas com icacls /inheritance:r. |
| 55 | Demonstra o gerenciamento de permissões pela interface gráfica do Windows. |
| 56 | Continuação visual do exemplo de permissões na interface gráfica. |
| 57 | Continuação visual do exemplo de permissões na interface gráfica. |
| 58 | Explica níveis de integridade/confiança: Low, Medium, High, System e TrustedInstaller. |
| 59 | Relaciona integridade ao nível de acesso obtido e cita whoami /groups e UAC bypass no contexto do curso. |
| 60 | Exemplo visual comparando terminais com integridade alta e média. |

## 8. Seção 5 — Informações do sistema

| Campo | Conteúdo |
|---|---|
| Título da seção | Informações do sistema |
| Páginas | 61–67 |
| Objetivo | Mostrar como coletar informações essenciais do host e do Windows para contextualização técnica. |
| Subtemas centrais | Nome do host; MAC; data; drivers; histórico de comandos; versão/build; KBs/hotfixes. |
| Comandos / ferramentas / recursos | hostname, getmac /v, date, date /t, driverquery, doskey /history, ver, systeminfo. |
| Pontos-chave para revisão | SO, versão, build e KB influenciam correções e compatibilidade; systeminfo exibe hotfixes. |

### 8.1 Mapa detalhado por página — Seção 5

| Página | Resumo do conteúdo da página |
|---|---|
| 61 | Página de abertura da seção 5. |
| 62 | Lista comandos para coleta de informações do Windows: hostname, getmac, date, driverquery e doskey /history. |
| 63 | Mostra o comando ver e a relação entre build e versão oficial do Windows. |
| 64 | Explica a importância de identificar SO, versão, build e KB/hotfix para entender compatibilidades e correções. |
| 65 | Introduz a questão de como descobrir os KBs instalados. |
| 66 | Apresenta systeminfo como fonte de detalhes do sistema e dos hotfixes/KBs. |
| 67 | Página ilustrativa/continuação da seção 5. |

## 9. Seção 6 — Gerenciamento de usuários e grupos

| Campo | Conteúdo |
|---|---|
| Título da seção | Gerenciamento de usuários e grupos |
| Páginas | 68–79 |
| Objetivo | Apresentar contas locais, grupos e operações administrativas básicas. |
| Subtemas centrais | Tipos de conta; listagem de usuários; consulta de conta; criação; exclusão; troca de senha; ativação/desativação; grupos locais; inclusão e remoção em grupos. |
| Comandos / ferramentas / recursos | net user, whoami, net localgroup. |
| Pontos-chave para revisão | Diversas ações exigem integridade alta; contas padrão e grupos internos estruturam permissões locais. |

### 9.1 Mapa detalhado por página — Seção 6

| Página | Resumo do conteúdo da página |
|---|---|
| 68 | Página de abertura da seção 6. |
| 69 | Explica tipos de conta: Administrador, Usuário Padrão e Convidado. |
| 70 | Mostra net user para listar contas e whoami para identificar o usuário atual. |
| 71 | Mostra net user <usuário> para consultar informações detalhadas da conta. |
| 72 | Mostra criação de novo usuário com exigência de integridade alta. |
| 73 | Mostra remoção de usuário com exigência de integridade alta. |
| 74 | Mostra alteração de senha de usuário com exigência de integridade alta. |
| 75 | Mostra ativação/desativação de conta com exigência de integridade alta. |
| 76 | Mostra net localgroup para listar grupos e comenta idioma do sistema e limitações do usuário SYSTEM. |
| 77 | Mostra net localgroup <grupo> para listar membros. |
| 78 | Mostra adição de usuário a grupo com exigência de integridade alta. |
| 79 | Mostra remoção de usuário de grupo com exigência de integridade alta. |

## 10. Seção 7 — Gerenciamento de redes

| Campo | Conteúdo |
|---|---|
| Título da seção | Gerenciamento de redes |
| Páginas | 80–89 |
| Objetivo | Mostrar comandos para inspecionar e alterar parâmetros de rede no Windows. |
| Subtemas centrais | Interfaces; endereços IP; detalhes da configuração; conexões ativas; TCP; UDP; IP estático; DHCP; DNS. |
| Comandos / ferramentas / recursos | netsh interface show interface, ipconfig, ipconfig /all, netstat -ano, netsh interface ip show tcpconnections, netsh interface ip show udpconnections, netsh interface ip set address, netsh interface ip set dns. |
| Pontos-chave para revisão | Combina visualização de interfaces, conexões e parametrização de IP/DNS. |

### 10.1 Mapa detalhado por página — Seção 7

| Página | Resumo do conteúdo da página |
|---|---|
| 80 | Página de abertura da seção 7. |
| 81 | Mostra netsh interface show interface para listar interfaces de rede. |
| 82 | Mostra ipconfig e netsh interface ip show address para visualizar endereços IP. |
| 83 | Mostra ipconfig /all para visualizar informações detalhadas de rede. |
| 84 | Mostra netstat -ano para conexões, portas ativas e PIDs. |
| 85 | Mostra netsh interface ip show tcpconnections para conexões TCP. |
| 86 | Mostra netsh interface ip show udpconnections para conexões UDP. |
| 87 | Mostra configuração manual de IP estático com netsh interface ip set address. |
| 88 | Mostra retorno ao uso de DHCP com netsh interface ip set address source=dhcp. |
| 89 | Mostra configuração de DNS com netsh interface ip set dns. |

## 11. Seção 8 — Gerenciamento de firewall

| Campo | Conteúdo |
|---|---|
| Título da seção | Gerenciamento de firewall |
| Páginas | 90–99 |
| Objetivo | Introduzir consulta do status do firewall e gerenciamento básico de regras. |
| Subtemas centrais | Todos os perfis; perfil atual; habilitar/desabilitar; listar regras; consultar regra específica; criar regras. |
| Comandos / ferramentas / recursos | netsh advfirewall show allprofiles/currentprofile; netsh advfirewall set allprofiles state on/off; netsh advfirewall firewall show/add rule. |
| Pontos-chave para revisão | Visibilidade por perfil e manipulação de regras; observação prática sobre portas 80 e 443. |

### 11.1 Mapa detalhado por página — Seção 8

| Página | Resumo do conteúdo da página |
|---|---|
| 90 | Página de abertura da seção 8. |
| 91 | Mostra netsh advfirewall show allprofiles para estado de todos os perfis. |
| 92 | Mostra netsh advfirewall show currentprofile para o perfil ativo. |
| 93 | Mostra habilitação do firewall em todos os perfis. |
| 94 | Mostra desabilitação do firewall em todos os perfis. |
| 95 | Mostra listagem de todas as regras de firewall. |
| 96 | Mostra consulta de regra específica de firewall. |
| 97 | Mostra criação de regra de firewall (parte 1). |
| 98 | Mostra criação de regra de firewall (parte 2). |
| 99 | Observação prática sobre portas 80 e 443 e seu uso recorrente. |

## 12. Seção 9 — Gerenciamento de programas, processos e serviços

| Campo | Conteúdo |
|---|---|
| Título da seção | Gerenciamento de programas, processos e serviços |
| Páginas | 100–116 |
| Objetivo | Diferenciar programas, processos e serviços e mostrar sua administração básica. |
| Subtemas centrais | Inventário de programas instalados; alternativas no Windows 11; listagem de processos; módulos DLL; serviços associados; encerramento de processos; comparação serviço × processo; consulta, configuração e criação de serviços. |
| Comandos / ferramentas / recursos | wmic product; Get-CimInstance; reg query; winget list; tasklist; Get-Process; taskkill; sc query/qc/start/stop/config/create; net start; Get-Service. |
| Pontos-chave para revisão | tasklist /M, /SVC e /V; serviços podem executar em contas especiais; o material faz alerta sobre impacto de binários/serviços mal configurados. |

### 12.1 Mapa detalhado por página — Seção 9

| Página | Resumo do conteúdo da página |
|---|---|
| 100 | Página de abertura da seção 9. |
| 101 | Lista programas instalados com wmic product get name, version e installlocation. |
| 102 | Apresenta alternativas no Windows 11: Get-CimInstance, reg query e winget list. |
| 103 | Define processo e mostra tasklist/Get-Process para listar processos. |
| 104 | Mostra tasklist /M para módulos DLL carregados por processo. |
| 105 | Mostra tasklist /SVC para relacionar processos e serviços. |
| 106 | Mostra tasklist /V em terminal com integridade média. |
| 107 | Mostra tasklist /V em terminal com integridade alta. |
| 108 | Mostra taskkill por PID ou nome e comenta encerramento de filhos e necessidade de integridade alta em alguns casos. |
| 109 | Compara conceitualmente serviço e processo. |
| 110 | Mostra sc query, sc query state= all e net start para listar serviços. |
| 111 | Mostra sc qc <serviço> para configurações detalhadas. |
| 112 | Mostra wmic service / Get-Service para listar serviços com filtros. |
| 113 | Mostra sc stop e sc start para parar/iniciar serviços. |
| 114 | Mostra sc config ... binPath= para alterar caminho do executável de um serviço. |
| 115 | Mostra sc create para criar um novo serviço executado como LocalSystem. |
| 116 | Alerta prático do curso: serviços editáveis ou binários substituíveis podem impactar privilégios do sistema. |

## 13. Seção 10 — Gerenciamento de tarefas agendadas

| Campo | Conteúdo |
|---|---|
| Título da seção | Gerenciamento de tarefas agendadas |
| Páginas | 117–124 |
| Objetivo | Apresentar automação por tarefas agendadas e seus diferentes contextos de execução. |
| Subtemas centrais | Periodicidades; criação de tarefa padrão; teste de integridade; criação com integridade alta; criação como SYSTEM; consulta; execução imediata; exclusão. |
| Comandos / ferramentas / recursos | schtasks /create, /query, /run, /delete. |
| Pontos-chave para revisão | Diferença entre tarefa padrão, /RL HIGHEST e execução como SYSTEM; uso de períodos como minute, hourly, daily, weekly, monthly, once, onstart, onlogon e onidle. |

### 13.1 Mapa detalhado por página — Seção 10

| Página | Resumo do conteúdo da página |
|---|---|
| 117 | Página de abertura da seção 10. |
| 118 | Lista os tipos de agendamento do schtasks: minute, hourly, daily, weekly, monthly, once, onstart, onlogon e onidle. |
| 119 | Explica criação de tarefa agendada padrão com integridade média. |
| 120 | Propõe teste prático para comparar nível de integridade de terminais abertos por tarefas distintas. |
| 121 | Mostra criação de tarefa com /RL HIGHEST para integridade alta em contas administrativas. |
| 122 | Mostra criação de tarefa executada como SYSTEM. |
| 123 | Mostra schtasks /query /v /fo list para listar tarefas detalhadamente. |
| 124 | Mostra schtasks /run, /delete e /query para executar, apagar e consultar tarefa específica. |

## 14. Seção 11 — Gerenciamento de antivírus

| Campo | Conteúdo |
|---|---|
| Título da seção | Gerenciamento de antivírus |
| Páginas | 125–128 |
| Objetivo | Abordar o gerenciamento do Windows Defender e a verificação do estado de proteção. |
| Subtemas centrais | Preferências do Defender; status do antivírus; tamper protection; chaves de registro; consulta a produtos/serviços antivírus instalados. |
| Comandos / ferramentas / recursos | Set-MpPreference; Get-MpComputerStatus; reg add; wmic product; net start/net stop (citados no material). |
| Pontos-chave para revisão | O material mostra verificações de proteção contra violações e diferentes vias de administração do antivírus. |

### 14.1 Mapa detalhado por página — Seção 11

| Página | Resumo do conteúdo da página |
|---|---|
| 125 | Página de abertura da seção 11. |
| 126 | Apresenta gerenciamento do Windows Defender, incluindo verificação de tamper protection e comandos de preferência/estado no PowerShell. |
| 127 | Apresenta tentativa de gestão do Defender via chaves de registro, com necessidade de reinicialização. |
| 128 | Apresenta consulta a programas/serviços de antivírus instalados e ações de serviço/remoção tratadas pelo material. |

## 15. Seção 12 — Registro do Windows

| Campo | Conteúdo |
|---|---|
| Título da seção | Registro do Windows |
| Páginas | 129–142 |
| Objetivo | Introduzir a estrutura do Registro do Windows e as operações básicas sobre chaves e valores. |
| Subtemas centrais | Definição do registro; armazenamento; regedit; chaves-raiz; caminho completo; tipos de dados; consulta; criação; edição; exclusão. |
| Comandos / ferramentas / recursos | regedit; reg query; reg add; reg delete. |
| Pontos-chave para revisão | Estrutura hierárquica; chaves como HKCR/HKCU/HKLM; tipos de valor como REG_BINARY; distinção entre valor e subchave. |

### 15.1 Mapa detalhado por página — Seção 12

| Página | Resumo do conteúdo da página |
|---|---|
| 129 | Página de abertura da seção 12. |
| 130 | Define o Registro do Windows como banco de dados hierárquico de configurações do sistema e aplicativos. |
| 131 | Mostra o armazenamento principal em C:\Windows\System32\config e diferencia chaves de arquivos físicos. |
| 132 | Mostra a visão do regedit e sua organização em chaves/subchaves. |
| 133 | Explica a analogia do registro com árvore de diretórios e elementos como chave, subchave e valor. |
| 134 | Apresenta chaves-raiz, com destaque para HKCR e HKCU/HKLM. |
| 135 | Exemplifica caminho completo de chave no registro com RegisteredApplications. |
| 136 | Mostra tipos de dados do registro, como REG_BINARY e demais formatos. |
| 137 | Mostra reg query para consultar valores/chaves. |
| 138 | Mostra reg add para adicionar subchaves. |
| 139 | Mostra reg add com parâmetros /v, /t e /d para adicionar valores. |
| 140 | Continua exemplos de criação/edição de valores no registro. |
| 141 | Mostra reg delete ... /v para remover um valor. |
| 142 | Mostra reg delete para remover subchave ou chave. |

## 16. Seção 13 — Log e eventos

| Campo | Conteúdo |
|---|---|
| Título da seção | Log e eventos |
| Páginas | 143–150 |
| Objetivo | Mostrar noções básicas de registro e consulta de eventos do Windows. |
| Subtemas centrais | Elementos do evento; Event Viewer; acesso por GUI e eventvwr.msc; cinco áreas principais; busca prática por string em eventos. |
| Comandos / ferramentas / recursos | Event Viewer; eventvwr.msc. |
| Pontos-chave para revisão | Aplicativo, Segurança, Instalação, Sistema e Eventos Encaminhados; exemplo de identificação de data e usuário responsável por instalação. |

### 16.1 Mapa detalhado por página — Seção 13

| Página | Resumo do conteúdo da página |
|---|---|
| 143 | Página de abertura da seção 13. |
| 144 | Introdução simplificada ao tema de logs e eventos no Windows. |
| 145 | Lista os elementos básicos de um evento: Event ID, origem, data/hora, usuário e nível. |
| 146 | Apresenta o Event Viewer e o atalho eventvwr.msc. |
| 147 | Mostra as cinco áreas básicas: Aplicativo, Segurança, Instalação, Sistema e Eventos Encaminhados. |
| 148 | Exemplo prático de busca por uma string ('michel.exe') nos logs. |
| 149 | Continuação visual do exemplo no Event Viewer. |
| 150 | Conclusão do exemplo, identificando data de instalação e usuário responsável. |

## 17. Seção 14 — Dump de memória RAM

| Campo | Conteúdo |
|---|---|
| Título da seção | Dump de memória RAM |
| Páginas | 151–166 |
| Objetivo | Explicar a relevância da memória volátil e demonstrar um fluxo básico de aquisição com FTK Imager. |
| Subtemas centrais | Conceito de dump; conceito de RAM; dados voláteis; orientações de preservação; FTK Imager; preparação de pendrive; cópia de DLLs; capacidade de armazenamento; execução da coleta; pós-coleta. |
| Comandos / ferramentas / recursos | FTK Imager. |
| Pontos-chave para revisão | Não desligar/reiniciar antes da coleta; a RAM pode conter sessões, processos, conexões, chaves e senhas; preservar a evidência e isolar o equipamento de redes. |

### 17.1 Mapa detalhado por página — Seção 14

| Página | Resumo do conteúdo da página |
|---|---|
| 151 | Página de abertura da seção 14. |
| 152 | Define dump de memória e explica utilidade em forense e recuperação de dados. |
| 153 | Define memória RAM e alerta para não desligar/reiniciar o sistema antes da coleta. |
| 154 | Lista dados que podem existir apenas na RAM: sessões, processos, conexões, chaves, senhas, documentos e chats. |
| 155 | Apresenta orientações de campo para preservar o equipamento e tentar acesso antes de desligar. |
| 156 | Reforça o valor do dump para a equipe de segurança cibernética em caso de suspeita de incidente. |
| 157 | Apresenta o FTK Imager como ferramenta utilizada para coleta de memória. |
| 158 | Inicia a preparação de um pendrive para usar a ferramenta. |
| 159 | Mostra a cópia da pasta de instalação do FTK Imager para o pendrive. |
| 160 | Mostra a necessidade de copiar DLLs mfc*.dll do System32 para o pendrive (com exceção indicada no material). |
| 161 | Orienta sobre a capacidade de armazenamento necessária para salvar o dump. |
| 162 | Mostra a execução do FTK Imager a partir do pendrive no computador-alvo. |
| 163 | Continuação visual do procedimento de dump no FTK Imager. |
| 164 | Conclusão visual do processo de dump de memória. |
| 165 | Orienta a preservar o dispositivo com o dump para análise especializada. |
| 166 | Orienta a desconectar o computador de Wi‑Fi, rede, Bluetooth etc. durante a preservação. |

## 18. Seção 15 — Realizar cópia de disco do S.O. Windows

| Campo | Conteúdo |
|---|---|
| Título da seção | Realizar cópia de disco do S.O. Windows |
| Páginas | 167–173 |
| Objetivo | Apresentar o conceito de imagem/clonagem de disco e sua conversão para uso em ambientes virtualizados. |
| Subtemas centrais | Imagem/clonagem; P2V; Disk2vhd; uso portátil; Volume Shadow Copy; seleção do disco; progresso e conclusão. |
| Comandos / ferramentas / recursos | Disk2vhd. |
| Pontos-chave para revisão | Copia o disco e converte para VHD em fluxo único; pode ser executado com o sistema online. |

### 18.1 Mapa detalhado por página — Seção 15

| Página | Resumo do conteúdo da página |
|---|---|
| 167 | Página de abertura da seção 15. |
| 168 | Define imagem/clonagem de disco e contextualiza a conversão Physical-to-Virtual (P2V). |
| 169 | Apresenta o Disk2vhd como ferramenta para copiar disco físico para VHD online. |
| 170 | Mostra a extração do Disk2vhd e o uso do executável portátil, preferencialmente 64 bits. |
| 171 | Mostra a seleção de opções: Use Volume Shadow Copy, local de saída, disco do Windows e início do processo. |
| 172 | Mostra barra de progresso, tempo restante e conclusão da cópia/conversão. |
| 173 | Resume os ganhos: cópia do disco e conversão para disco virtual no mesmo fluxo. |

## 19. Seção 16 — Recuperar arquivos apagados em dispositivos

| Campo | Conteúdo |
|---|---|
| Título da seção | Recuperar arquivos apagados em dispositivos |
| Páginas | 174–187 |
| Objetivo | Apresentar o princípio da recuperação de arquivos excluídos e o uso básico do Recuva. |
| Subtemas centrais | Recuperação lógica; instalação; uso portátil em pendrive; abertura do Recuva; seleção da origem; leitura do dispositivo; filtro por tipo; seleção de arquivos; recuperação; validação de legibilidade. |
| Comandos / ferramentas / recursos | Recuva. |
| Pontos-chave para revisão | Arquivos apagados podem persistir até sobrescrita; buscar a partir da raiz do dispositivo; 'bola verde' não garante legibilidade. |

### 19.1 Mapa detalhado por página — Seção 16

| Página | Resumo do conteúdo da página |
|---|---|
| 174 | Página de abertura da seção 16. |
| 175 | Explica o princípio da recuperação de arquivos apagados e apresenta o Recuva. |
| 176 | Mostra a instalação inicial do Recuva em um computador auxiliar. |
| 177 | Mostra a cópia da pasta do Recuva para pendrive e seu uso portátil em diversos dispositivos. |
| 178 | Mostra como iniciar o Recuva pelo sistema local ou pelo pendrive. |
| 179 | Tela/etapa visual intermediária do assistente do Recuva. |
| 180 | Mostra a seleção da origem da busca, recomendando iniciar pela raiz do dispositivo. |
| 181 | Mostra a leitura do dispositivo e a listagem dos arquivos encontrados. |
| 182 | Mostra a filtragem por tipo de arquivo e o significado visual de integridade (vermelho/verde). |
| 183 | Mostra a seleção dos arquivos e o início do processo de recuperação/salvamento. |
| 184 | Mostra a confirmação de arquivos salvos e possibilidade de repetir o processo. |
| 185 | Mostra a etapa final, destacando que arquivo salvo nem sempre estará legível. |
| 186 | Tela final/ilustrativa do procedimento de recuperação. |
| 187 | Tela final/ilustrativa do procedimento de recuperação. |

## 20. Tabela consolidada de comandos, ferramentas e utilitários mencionados

| Categoria | Itens |
|---|---|
| Linha de comando / shell | CMD, PowerShell |
| Navegação e arquivos | help, dir, cd, md/mkdir, rd, type, ren, xcopy, del, tree, attrib, findstr, echo, sort, redirecionadores e pipes |
| Identidade / contexto | whoami, whoami /priv, whoami /groups |
| Informações do sistema | hostname, getmac /v, date, driverquery, doskey /history, ver, systeminfo |
| Usuários e grupos | net user, net localgroup |
| Rede | ipconfig, netstat -ano, netsh interface ... |
| Firewall | netsh advfirewall ... show/set/firewall show rule/add rule |
| Processos e programas | wmic product, Get-CimInstance, reg query, winget list, tasklist, Get-Process, taskkill |
| Serviços | sc query, sc qc, sc start, sc stop, sc config, sc create, net start, Get-Service |
| Tarefas agendadas | schtasks /create, /query, /run, /delete |
| Antivírus | Set-MpPreference, Get-MpComputerStatus, referências a reg add, wmic product e serviços |
| Registro | regedit, reg query, reg add, reg delete |
| Eventos | Event Viewer, eventvwr.msc |
| Coleta forense / imagem / recuperação | FTK Imager, Disk2vhd, Recuva |

## 21. Síntese final do conteúdo do PDF

| Eixo | Síntese |
|---|---|
| Fundamentos do Windows | Estrutura do disco, diretórios do sistema, perfis de usuário e organização lógica do Windows. |
| Identificação de arquivos | Extensões, arquivos ocultos, assinaturas (magic numbers) e validação do tipo real do arquivo. |
| Operação em CLI | Uso de CMD e PowerShell para navegação, consulta, busca, filtragem, redirecionamento e análise do contexto do usuário. |
| Controle de acesso | ACL, ACE, DACL, permissões básicas e avançadas, heranças, grupos internos e níveis de integridade. |
| Administração local | Coleta de informações do sistema, gestão de usuários, grupos, interfaces de rede, firewall, programas, processos, serviços e tarefas agendadas. |
| Observabilidade do sistema | Consulta ao registro do Windows, Event Viewer e interpretação básica de logs e eventos. |
| Introdução à coleta e resposta | Dump de memória RAM, cópia de disco com conversão para VHD e recuperação de arquivos apagados. |
| Caráter do material | Curso essencialmente operacional, com foco em familiarização, administração básica e noções iniciais de preservação/análise técnica em Windows. |
