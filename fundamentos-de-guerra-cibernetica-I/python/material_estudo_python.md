# Material de estudo — Introdução à Linguagem Python

## 1. Entender as particularidades da linguagem Python

### Conceito
Python é uma linguagem de programação:
- interpretada;
- de alto nível;
- multiparadigma;
- com sintaxe simples e legível;
- muito usada em automação, análise de dados, desenvolvimento web, segurança e IA.

### Características principais
- usa **indentação obrigatória** para definir blocos;
- não exige declaração prévia de tipo;
- possui grande biblioteca padrão;
- permite escrever menos código para resolver problemas;
- é portátil, funcionando em vários sistemas operacionais.

### Exemplo básico
```python
print("Olá, mundo!")
```

### Indentação
Em Python, a indentação substitui chaves `{}`.

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### Comentários
```python
# Comentário de uma linha
```

```python
"""
Comentário ou docstring
de várias linhas
"""
```

### Executando scripts
```bash
python3 arquivo.py
```

### Flags úteis
```bash
python3 --version
python3 -V
python3 -m pip --version
python3 -i arquivo.py
```

#### Significado
- `--version` ou `-V` → mostra a versão
- `-m` → executa um módulo como programa
- `-i` → entra no modo interativo após rodar o script

### O que memorizar
- Python é interpretada;
- blocos dependem de indentação;
- sintaxe é simples e legível;
- pode ser usada tanto interativamente quanto em arquivos `.py`.

---

## 2. Utilizar variáveis

### Conceito
Variáveis armazenam valores para uso posterior no programa.

### Exemplo
```python
nome = "Marcus"
idade = 30
altura = 1.75
ativo = True
```

### Tipos básicos
- `str` → texto
- `int` → inteiro
- `float` → decimal
- `bool` → verdadeiro/falso

### Verificando tipo
```python
x = 10
print(type(x))
```

### Conversão de tipos
```python
idade = "25"
idade_int = int(idade)

altura = "1.80"
altura_float = float(altura)

numero = 100
numero_texto = str(numero)
```

### Entrada de dados
```python
nome = input("Digite seu nome: ")
print(nome)
```

#### Atenção
`input()` retorna texto. Para número:

```python
idade = int(input("Digite sua idade: "))
```

### Atribuição múltipla
```python
a, b, c = 1, 2, 3
```

### O que memorizar
- Python não exige declarar tipo explicitamente;
- `input()` retorna `str`;
- conversões comuns: `int()`, `float()`, `str()`, `bool()`.

---

## 3. Utilizar funções

### Conceito
Funções agrupam instruções reutilizáveis.

### Sintaxe
```python
def saudacao():
    print("Olá!")
```

### Chamando função
```python
saudacao()
```

### Função com parâmetro
```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

### Função com retorno
```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)
print(resultado)
```

### Parâmetros com valor padrão
```python
def apresentar(nome, cidade="Brasília"):
    print(f"{nome} mora em {cidade}")
```

### Função com vários retornos
```python
def calcular(a, b):
    soma = a + b
    produto = a * b
    return soma, produto
```

### Escopo
Variáveis criadas dentro da função são locais.

```python
def teste():
    x = 10
    print(x)
```

### O que memorizar
- `def` define função;
- `return` devolve valor;
- parâmetros recebem dados;
- variáveis internas têm escopo local.

---

## 4. Utilizar estruturas de repetição

### Conceito
Estruturas de repetição executam blocos várias vezes.

### `for`
Usado quando se conhece a sequência ou intervalo.

```python
for i in range(5):
    print(i)
```

### `range()`
```python
range(5)         # 0 até 4
range(1, 6)      # 1 até 5
range(0, 10, 2)  # de 2 em 2
```

### `while`
Executa enquanto a condição for verdadeira.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

### `break`
Interrompe o laço.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue`
Pula para a próxima iteração.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### O que memorizar
- `for` percorre sequências;
- `while` depende de condição;
- `break` interrompe;
- `continue` pula a iteração atual.

---

## 5. Interagir com strings

### Conceito
Strings são sequências de caracteres.

### Criação
```python
nome = "Python"
```

### Concatenação
```python
primeiro = "Olá"
segundo = "mundo"
print(primeiro + " " + segundo)
```

### Repetição
```python
print("ha" * 3)
```

### Acesso por índice
```python
texto = "Python"
print(texto[0])   # P
print(texto[-1])  # n
```

### Fatiamento
```python
texto = "Python"
print(texto[0:3])  # Pyt
print(texto[2:])   # thon
print(texto[:4])   # Pyth
```

### Métodos úteis
```python
texto = "  Olá Mundo  "

print(texto.lower())
print(texto.upper())
print(texto.strip())
print(texto.replace("Mundo", "Python"))
print(texto.split())
```

### f-strings
```python
nome = "Marcus"
idade = 30
print(f"{nome} tem {idade} anos")
```

### Verificação
```python
email = "teste@email.com"
print("@" in email)
```

### O que memorizar
- strings são imutáveis;
- índices começam em 0;
- `split()`, `strip()`, `lower()`, `upper()`, `replace()` são muito usados;
- `f-string` facilita formatação.

---

## 6. Interagir com arquivos

### Conceito
Python permite abrir, ler, escrever e manipular arquivos.

### Abrindo arquivo
```python
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()
```

### Modos de abertura
- `"r"` → leitura
- `"w"` → escrita, sobrescreve
- `"a"` → adiciona ao final
- `"x"` → cria arquivo novo
- `"b"` → modo binário

### Forma recomendada: `with`
```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

### Escrevendo arquivo
```python
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
```

### Lendo linha por linha
```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

### O que memorizar
- `with open(...)` é mais seguro;
- `"w"` sobrescreve;
- `"a"` acrescenta;
- `read()`, `readline()`, `readlines()` e laço `for` são formas comuns de leitura.

---

## 7. Importação de módulos

### Conceito
Módulos são arquivos ou bibliotecas com funções e recursos reutilizáveis.

### Importação simples
```python
import math
print(math.sqrt(25))
```

### Importação específica
```python
from math import sqrt
print(sqrt(16))
```

### Apelido
```python
import math as m
print(m.pi)
```

### Módulos comuns
- `math`
- `random`
- `os`
- `sys`
- `datetime`

### Exemplos
```python
import random
print(random.randint(1, 10))
```

```python
import os
print(os.getcwd())
```

### Instalação de pacotes externos
```bash
pip install nome_do_pacote
pip3 install nome_do_pacote
python3 -m pip install nome_do_pacote
```

### O que memorizar
- `import modulo`
- `from modulo import item`
- `as` cria alias;
- `pip` instala bibliotecas externas.

---

## 8. Utilizar listas

### Conceito
Lista é uma estrutura que armazena vários valores em sequência.

### Criação
```python
nomes = ["Ana", "Bruno", "Carlos"]
```

### Acesso
```python
print(nomes[0])
print(nomes[-1])
```

### Alteração
```python
nomes[1] = "Beatriz"
```

### Métodos principais
```python
numeros = [1, 2, 3]

numeros.append(4)
numeros.insert(1, 10)
numeros.remove(2)
ultimo = numeros.pop()
numeros.sort()
numeros.reverse()
```

### Percorrendo lista
```python
for item in nomes:
    print(item)
```

### Tamanho
```python
print(len(nomes))
```

### Verificando elemento
```python
print("Ana" in nomes)
```

### Lista de listas
```python
matriz = [
    [1, 2],
    [3, 4]
]
```

### O que memorizar
- listas são mutáveis;
- `append()`, `insert()`, `remove()`, `pop()`, `sort()` são essenciais;
- listas podem ser percorridas com `for`.

---

## Erros comuns em Python
- esquecer indentação correta;
- usar `=` no lugar de `==`;
- não converter `input()` para número;
- tentar acessar índice inexistente;
- esquecer `:` em `if`, `for`, `while`, `def`.

---

## Exercício prático de Python

```python
def cadastrar_nomes():
    nomes = []

    while True:
        nome = input("Digite um nome (ou sair): ")

        if nome.lower() == "sair":
            break

        nomes.append(nome)

    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        for nome in nomes:
            arquivo.write(nome + "\n")

    print("Nomes salvos com sucesso.")

cadastrar_nomes()
```

### O que esse exercício revisa
- função;
- lista;
- repetição;
- string;
- arquivo;
- condição.

---

## Exercício extra de Python

```python
def analisar_texto():
    texto = input("Digite uma frase: ")

    palavras = texto.split()
    quantidade = len(palavras)

    with open("frase.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

    print(f"Quantidade de palavras: {quantidade}")
    print(f"Maiúsculo: {texto.upper()}")
    print(f"Minúsculo: {texto.lower()}")

analisar_texto()
```

### Revisa
- função;
- variável;
- string;
- lista;
- arquivo.

---

## Resumo de memorização rápida

Você precisa dominar:
- sintaxe e indentação;
- variáveis e tipos;
- funções;
- `for` e `while`;
- strings;
- arquivos;
- módulos;
- listas.

---

## Questões de fixação

1. O que diferencia Python de linguagens com chaves?  
2. O que `input()` retorna?  
3. Para que serve `return`?  
4. Qual a diferença entre `for` e `while`?  
5. O que faz `split()` em uma string?  
6. Qual a vantagem de `with open()`?  
7. Como importar apenas uma função de um módulo?  
8. Qual a diferença entre `append()` e `insert()` em listas?
