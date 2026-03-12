# Material de estudo — Introdução a Shell Script

## 1. Manipular variáveis e caracteres úteis em scripts em shell

### Conceito
Shell Script é uma forma de automatizar comandos no terminal, geralmente usando **Bash**.

### Estrutura básica
```bash
#!/bin/bash

echo "Olá, mundo"
```

### Dar permissão de execução
```bash
chmod +x script.sh
```

### Executar
```bash
./script.sh
```

### Variáveis
```bash
nome="Marcus"
idade=30

echo "$nome"
echo "$idade"
```

#### Atenção
Em Bash, não se coloca espaço:

```bash
nome="Joao"
```

Errado:

```bash
nome = "Joao"
```

### Uso de variável
```bash
echo "Nome: $nome"
echo "Nome: ${nome}"
```

### Caracteres úteis
- `$` → acessa variável
- `"` → permite expansão de variável
- `'` → trata tudo literalmente
- `\` → escape
- `#` → comentário
- `*` → curinga
- `?` → curinga de um caractere

### Exemplos
```bash
arquivo="dados.txt"
echo "Arquivo: $arquivo"
echo 'Arquivo: $arquivo'
```

No primeiro, expande. No segundo, não.

### O que memorizar
- Bash usa `variavel=valor`;
- `$variavel` acessa o conteúdo;
- aspas duplas expandem variáveis;
- aspas simples preservam literal.

---

## 2. Usar parâmetros em scripts em shell

### Conceito
Parâmetros posicionais permitem passar argumentos ao script.

### Exemplo
```bash
#!/bin/bash

echo "Primeiro argumento: $1"
echo "Segundo argumento: $2"
```

Executando:

```bash
./script.sh ana 25
```

Saída:

```text
Primeiro argumento: ana
Segundo argumento: 25
```

### Parâmetros especiais
- `$0` → nome do script
- `$1`, `$2`, ... → argumentos posicionais
- `$#` → quantidade de argumentos
- `$@` → todos os argumentos
- `$*` → todos os argumentos
- `$$` → PID do script
- `$?` → código de saída do último comando

### Exemplo
```bash
#!/bin/bash

echo "Script: $0"
echo "Quantidade: $#"
echo "Todos: $@"
```

### Verificando quantidade de argumentos
```bash
#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Uso: $0 <nome> <idade>"
    exit 1
fi

echo "Nome: $1"
echo "Idade: $2"
```

### O que memorizar
- `$1`, `$2`, ... representam argumentos;
- `$#` informa quantos argumentos foram passados;
- `$?` mostra se o último comando deu certo.

---

## 3. Utilizar estruturas de repetição

### `for`
```bash
for i in 1 2 3 4 5
do
    echo "$i"
done
```

### `for` com sequência
```bash
for i in {1..5}
do
    echo "$i"
done
```

### `while`
```bash
contador=1

while [ $contador -le 5 ]
do
    echo "$contador"
    contador=$((contador + 1))
done
```

### `until`
Executa até a condição tornar-se verdadeira.

```bash
contador=1

until [ $contador -gt 5 ]
do
    echo "$contador"
    contador=$((contador + 1))
done
```

### `break` e `continue`
```bash
for i in {1..5}
do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "$i"
done
```

### O que memorizar
- `for` percorre itens;
- `while` depende de condição;
- `until` é o oposto lógico do `while`;
- `break` interrompe;
- `continue` pula a iteração.

---

## 4. Usar estruturas de controle de fluxo

### `if`
```bash
idade=20

if [ $idade -ge 18 ]; then
    echo "Maior de idade"
fi
```

### `if/else`
```bash
if [ $idade -ge 18 ]; then
    echo "Maior"
else
    echo "Menor"
fi
```

### `if/elif/else`
```bash
nota=7

if [ $nota -ge 9 ]; then
    echo "Excelente"
elif [ $nota -ge 7 ]; then
    echo "Aprovado"
else
    echo "Reprovado"
fi
```

### Operadores numéricos
- `-eq` → igual
- `-ne` → diferente
- `-gt` → maior que
- `-lt` → menor que
- `-ge` → maior ou igual
- `-le` → menor ou igual

### Comparação de strings
```bash
nome="admin"

if [ "$nome" = "admin" ]; then
    echo "Usuário válido"
fi
```

### Testes de arquivos
- `-f` → arquivo regular existe
- `-d` → diretório existe
- `-r` → permissão de leitura
- `-w` → permissão de escrita
- `-x` → permissão de execução

### Exemplo
```bash
if [ -f "dados.txt" ]; then
    echo "Arquivo encontrado"
else
    echo "Arquivo não encontrado"
fi
```

### `case`
```bash
opcao="start"

case $opcao in
    start)
        echo "Iniciando"
        ;;
    stop)
        echo "Parando"
        ;;
    restart)
        echo "Reiniciando"
        ;;
    *)
        echo "Opção inválida"
        ;;
esac
```

### O que memorizar
- `if`, `elif`, `else`, `fi`;
- operadores numéricos;
- testes com arquivos;
- `case` é útil para múltiplas opções.

---

## 5. Utilizar expressões regulares

### Conceito
Expressões regulares servem para localizar padrões em textos.

### Com `grep`
```bash
grep "erro" arquivo.log
```

### Flags úteis do `grep`
```bash
grep -i "erro" arquivo.log
grep -n "erro" arquivo.log
grep -r "erro" .
grep -v "erro" arquivo.log
grep -E "erro|falha" arquivo.log
```

#### Significado
- `-i` → ignora maiúsculas/minúsculas
- `-n` → mostra número da linha
- `-r` → busca recursiva
- `-v` → inverte, mostra o que não combina
- `-E` → regex estendida

### Metacaracteres comuns
- `.` → qualquer caractere
- `^` → início da linha
- `$` → final da linha
- `*` → zero ou mais ocorrências
- `+` → uma ou mais ocorrências
- `?` → zero ou uma ocorrência
- `[abc]` → um entre vários caracteres
- `[0-9]` → faixa
- `[^0-9]` → negação

### Exemplos
```bash
grep -E "^[0-9]+$" numeros.txt
grep -E "^[a-zA-Z]+$" nomes.txt
grep -E "erro|falha|critico" log.txt
```

### Regex em Bash com `[[ ]]`
```bash
texto="abc123"

if [[ $texto =~ ^[a-z]+[0-9]+$ ]]; then
    echo "Padrão válido"
fi
```

### `sed`
Substituição simples:

```bash
sed 's/erro/falha/' arquivo.txt
```

Global:

```bash
sed 's/erro/falha/g' arquivo.txt
```

### `awk`
Selecionando colunas:

```bash
awk '{print $1}' arquivo.txt
```

### O que memorizar
- `grep` busca padrões;
- `-E` ativa regex estendida;
- `sed` edita/substitui;
- `awk` trabalha bem com colunas;
- `[[ ... =~ ... ]]` permite regex em condições Bash.

---

## 6. Empregar funções em scripts em shell

### Conceito
Funções ajudam a reaproveitar blocos de comandos.

### Sintaxe
```bash
minha_funcao() {
    echo "Olá da função"
}
```

### Chamada
```bash
minha_funcao
```

### Função com parâmetro
```bash
saudar() {
    echo "Olá, $1"
}

saudar "Marcus"
```

### Retorno em Shell
Shell normalmente retorna **código de saída**, não valor como Python.

```bash
teste_funcao() {
    return 0
}
```

- `0` → sucesso
- diferente de `0` → erro

### Exemplo prático
```bash
verificar_arquivo() {
    if [ -f "$1" ]; then
        echo "Arquivo existe"
    else
        echo "Arquivo não existe"
    fi
}

verificar_arquivo "dados.txt"
```

### O que memorizar
- funções melhoram organização;
- `$1`, `$2` também funcionam dentro da função;
- `return` em Bash geralmente indica status, não texto.

---

## Comandos e flags úteis em Shell Script

### Executar com Bash
```bash
bash script.sh
```

### Verificar sintaxe sem executar
```bash
bash -n script.sh
```

### Modo verboso
```bash
bash -v script.sh
```

### Modo debug
```bash
bash -x script.sh
```

#### Significado
- `-n` → verifica sintaxe
- `-v` → exibe linhas lidas
- `-x` → mostra execução passo a passo

### Boas práticas
```bash
#!/bin/bash
set -e
set -u
set -o pipefail
```

#### Significado
- `set -e` → interrompe em erro
- `set -u` → falha se usar variável não definida
- `set -o pipefail` → considera falha em pipelines

---

## Erros comuns em Shell Script
- colocar espaço em atribuição de variável;
- esquecer `then`, `fi`, `do`, `done`;
- não usar aspas em variáveis com espaços;
- confundir `=` com `-eq` em comparação numérica;
- esquecer permissão de execução.

---

## Exercício prático — Shell Script

```bash
#!/bin/bash

mostrar_menu() {
    echo "1 - Mostrar data"
    echo "2 - Mostrar usuário"
    echo "3 - Verificar arquivo"
}

mostrar_menu

read -p "Escolha uma opção: " opcao

case $opcao in
    1)
        date
        ;;
    2)
        whoami
        ;;
    3)
        read -p "Digite o nome do arquivo: " arquivo
        if [ -f "$arquivo" ]; then
            echo "Arquivo encontrado"
        else
            echo "Arquivo não encontrado"
        fi
        ;;
    *)
        echo "Opção inválida"
        ;;
esac
```

### Revisa
- função;
- `case`;
- `read`;
- variável;
- teste de arquivo.

---

## Resumo de memorização rápida

Você precisa dominar:
- estrutura do script;
- variáveis;
- parâmetros posicionais;
- laços;
- `if` e `case`;
- regex com `grep`;
- funções;
- execução e debug com `bash -n`, `bash -x`.

---

## Questões de fixação

1. Como declarar uma variável em Bash?  
2. O que representa `$1`?  
3. Qual a diferença entre `for` e `while`?  
4. Quando usar `case`?  
5. O que faz `grep -i`?  
6. O que significa `bash -n script.sh`?  
7. Para que serve `set -e`?  
8. Como verificar se um arquivo existe?
