# SO Windows — Resumo fácil para estudo

## 1. Ideia geral do conteúdo
O material apresenta a base do Windows e prepara o caminho para estudos de exploração Windows e Active Directory.

Temas principais:
- Estrutura de arquivos
- Extensões de arquivos
- Comandos básicos
- Permissões
- Administração do sistema
- Rede, firewall, serviços, tarefas agendadas, antivírus, registro e logs

## 2. Estrutura de arquivos — pense assim
**`C:\` é a raiz do sistema.**

Pastas principais:
- **`C:\Program Files`** → programas
- **`C:\Program Files (x86)`** → programas 32 bits
- **`C:\Users`** → perfis dos usuários
- **`C:\ProgramData`** → dados usados por todos os usuários
- **`C:\Windows`** → arquivos do sistema operacional

Dentro de **`C:\Windows`**, as mais importantes são:
- **`System32`** → arquivos essenciais do sistema
- **`SysWOW64`** → compatibilidade 32 bits
- **`Temp`** → arquivos temporários
- **`Logs`** → registros de eventos e erros
- **`Installer`** → instalação e desinstalação
- **`SoftwareDistribution`** → atualizações do Windows
- **`Prefetch`** → acelera abertura de programas

Dentro de **`C:\Users`**, destaque para:
- Desktop
- Documents
- Downloads
- Music
- Pictures
- Videos
- AppData

### Macete
- **`C:\` = casa principal**
- **Windows = sistema**
- **Users = pessoas**
- **Program Files = programas**

## 3. Extensões de arquivo — regra principal
A extensão ajuda o Windows a entender:
- qual é o tipo do arquivo
- qual programa deve abri-lo

Exemplos:
- `.docx`
- `.jpg`
- `.pdf`

### Ponto mais importante
**Mudar a extensão não muda o arquivo por dentro.**

Exemplo:
Renomear `arquivo.txt` para `arquivo.docx` não transforma o conteúdo em um arquivo do Word.

O Windows também pode ocultar:
- extensões
- arquivos do sistema
- itens ocultos

## 4. Magic Numbers — a identidade real do arquivo
Os **magic numbers** são os primeiros bytes do arquivo e mostram seu tipo verdadeiro.

Exemplos:
- **PNG** → `89504E470D0A1A0A`
- **PDF** → `255044462D`
- **ZIP** → `504B0304`
- **EXE / DLL** → `4D5A`

### Macete
- **Extensão = etiqueta**
- **Magic number = identidade verdadeira**

## 5. CMD e PowerShell — diferença simples
No Windows, existem duas CLIs principais:

- **CMD** → mais antigo, estilo MS-DOS
- **PowerShell** → mais moderno, voltado para automação e administração

### Macete
- **CMD = clássico**
- **PowerShell = automação**

## 6. Comandos básicos — decore por função

### Navegação
- **`dir`** → lista arquivos
- **`cd`** → entra ou sai de diretórios
- **`md` / `mkdir`** → cria diretório
- **`rd`** → remove diretório

### Arquivos
- **`type`** → mostra conteúdo de arquivo texto
- **`ren`** → renomeia
- **`xcopy`** → copia
- **`del`** → apaga
- **`move`** → move arquivos ou pastas

### Identidade do usuário
- **`whoami`** → mostra o usuário atual
- **`whoami /priv`** → mostra privilégios
- **`whoami /groups`** → mostra grupos e nível de integridade

### Visualização e desligamento
- **`tree`** → mostra árvore de diretórios
- **`shutdown`** → desliga, reinicia ou faz logoff

### Saída e encadeamento
- **`echo`** → imprime texto
- **`>`** → sobrescreve em arquivo
- **`>>`** → adiciona em arquivo
- **`|`** → envia a saída de um comando para outro
- **`2>nul`** → oculta erros

### Busca e atributos
- **`attrib`** → mostra ou ajusta atributos
- **`findstr`** → busca texto em arquivos

### Macete de memorização
- **`dir / cd`** = ver e entrar
- **`md / rd`** = criar e remover
- **`type / ren / move / del`** = ler, renomear, mover, apagar
- **`whoami`** = quem sou eu
- **`findstr`** = procurar texto

## 7. Permissões — ideia central
O Windows usa **DACL** para controle de acesso.

Dentro da DACL existem as **ACE**, que são as regras individuais que definem quem pode fazer o quê.

Também existe a **herança de permissões**, em que o objeto filho pode receber permissões do objeto pai.

### Macete
- **DACL = lista geral**
- **ACE = regra individual**
- **Herança = filho recebe do pai**

## 8. Resumo relâmpago
### Estrutura
- `C:\` → raiz
- `Program Files` → programas
- `Users` → usuários
- `Windows` → sistema

### Extensão
Extensão ajuda a identificar, mas **não prova** o tipo real do arquivo.

### Magic number
É a assinatura real do arquivo.

### Terminais
- CMD = tradicional
- PowerShell = automação

### Comandos mais importantes
- `dir`
- `cd`
- `md`
- `rd`
- `type`
- `xcopy`
- `del`
- `move`
- `whoami`
- `tree`
- `attrib`
- `findstr`

### Permissões
- **DACL** controla acesso
- **ACE** é a regra
- **Herança** repassa permissões
