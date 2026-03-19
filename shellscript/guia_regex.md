# Guia organizado — AWK, SED, CUT, GREP, FIND, SORT, Regex e Bash

## 1) AWK

### Linhas que começam com `A` e terminam com `.`
```bash
awk '/^A.*\.$/' ~/dados.txt
```

### Extrair conteúdo entre `<=` e `=>`
```bash
awk -F '<=|=>' '{print $2}' /home/gciber12/dados.txt
```

### Exibir a terceira coluna
```bash
awk '{print $3}' teste_access.log
```

### Exibir múltiplas colunas
```bash
ps u | awk '{print $1, $2, $3}'
```

### Exibir colunas separadas por TAB
```bash
ps u | awk '{print $1 "\t" $2 "\t" $3}'
```

### Remover a primeira linha da saída
```bash
ps u | awk 'NR != 1'
```

### Substituir texto com `sub()`
```bash
ps u | awk '{ sub(/debian/, "outro-usuario"); print }'
```

### Imprimir a última coluna de `/etc/passwd`
```bash
awk -F ':' '{print $7}' /etc/passwd
```

### Exibir linhas de `/etc/passwd` onde a terceira coluna é maior que 100
```bash
awk -F ':' '$3 > 100' /etc/passwd
```

### Somar a quarta coluna de `/etc/passwd`
```bash
awk -F ':' '{sum += $4} END {print sum}' /etc/passwd
```

### Exibir linhas que contenham `Debian`
```bash
awk '/Debian/' arquivo.txt
```

### Exibir linhas que comecem com `A`
```bash
awk '/^A/' arquivo.txt
```

### Procurar telefone no formato `(12) 3456-7890`
```bash
awk '/\([[:digit:]]{2}\)[[:space:]][[:digit:]]{4}-[[:digit:]]{4}/' arquivo.txt
```

### Procurar e-mails
```bash
awk '/[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}/' arquivo.txt
```

---

## 2) SED

### Imprimir a linha 10
```bash
sed -n '10p' texto.txt
```

### Imprimir da linha 1 à 5
```bash
sed -n '1,5p' texto.txt
```

### Substituir `user` por `usuario` no arquivo
```bash
sed -i 's/user/usuario/g' teste_access.log
```

### Imprimir a última linha
```bash
sed -n '$p' texto.txt
```

### Apagar a linha 5 apenas na saída
```bash
sed '5d' texto.txt
```

### Apagar a linha 5 em definitivo
```bash
sed -i '5d' texto.txt
```

### Exibir linhas entre `Cybersecurity` e `extorting`
```bash
sed -n '/Cybersecurity/,/extorting/p' cybersecurity.txt
```

### Remover linhas em branco
```bash
sed '/^[[:space:]]*$/d' arquivo.txt
```

### Converter maiúsculas em minúsculas sem alterar o arquivo
```bash
sed 's/.*/\L&/' arquivo.txt
```

### Selecionar linhas entre duas palavras-chave
```bash
sed -n '/joseramos/,/albertemortensen/p' arquivo.txt
```

### Substituir todas as ocorrências de `velho` por `novo`
```bash
sed 's/velho/novo/g' arquivo.txt
```

### Substituir apenas a primeira ocorrência por linha
```bash
sed 's/velho/novo/' arquivo.txt
```

### Substituir no próprio arquivo
```bash
sed -i 's/velho/novo/g' arquivo.txt
```

### Inserir texto no início de cada linha
```bash
sed 's/^/Novo texto: /' arquivo.txt
```

### Inserir texto no final de cada linha
```bash
sed 's/$/ - Fim/' arquivo.txt
```

### Usar múltiplas substituições
```bash
sed -e 's/velho/novo/g' -e 's/antigo/moderno/g' arquivo.txt
```

---

## 3) CUT

### Imprimir os campos 1 e 7 de `/etc/passwd`
```bash
cut -d ':' -f 1,7 /etc/passwd
```

### Imprimir caracteres de 1 a 5
```bash
cut -c 1-5 /etc/passwd
```

### Extrair o primeiro campo de CSV
```bash
cut -d ',' -f 1 arquivo.csv
```

### Extrair o terceiro campo de CSV
```bash
cut -d ',' -f 3 arquivo.csv
```

### Extrair os campos 2 e 4
```bash
cut -d ',' -f 2,4 arquivo.csv
```

### Extrair da posição 5 até o final
```bash
cut -c 5- arquivo.txt
```

### Extrair usuário de e-mail
```bash
grep -Eo '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' arquivo.txt | cut -d '@' -f 1
```

### Extrair os últimos 4 caracteres
```bash
rev arquivo.txt | cut -c 1-4 | rev
```

---

## 4) GREP / GREP -E

> Observação: prefira `grep -E` no lugar de `egrep`, pois `egrep` é obsoleto em muitos ambientes.

### Monitorar tentativas de login em tempo real
```bash
tail -f /var/log/auth.log | grep "Failed password"
```

### Linhas que começam com `u`
```bash
grep '^u' /etc/passwd
```

### Linhas que terminam com `false`
```bash
grep 'false$' /etc/passwd
```

### Linhas com pelo menos 4 números consecutivos
```bash
grep '[0-9][0-9][0-9][0-9]' /etc/passwd
```

### Procurar palavra em todos os arquivos do diretório atual
```bash
grep 'ator' *
```

### Procurar recursivamente
```bash
grep -r 'ator' .
```

### Procurar `ator` ou `dentista`
```bash
grep -E 'ator|dentista' arquivo.txt
```

### Ignorar maiúsculas/minúsculas
```bash
grep -i 'DeNtIsTa' *
```

### Mostrar número da linha
```bash
grep -n 'piloto' arquivo.txt
```

### Contar acessos de um IP
```bash
grep '192.168.0.1' access.log | wc -l
```

### Procurar `Carlos` ou `carlos`
```bash
grep '[Cc]arlos' /etc/passwd
```

### Linhas que começam com vogais
```bash
grep '^[aeiouAEIOU]' /etc/passwd
```

### Linhas que NÃO começam com vogais
```bash
grep '^[^aeiouAEIOU]' /etc/passwd
```

### Extrair IPs
```bash
grep -oP '\b(?:\d{1,3}\.){3}\d{1,3}\b' arquivo.txt
```

### Buscar telefone no formato `(xx)xxxxx-xxxx`
```bash
grep -Eo '\([0-9]{2}\)[0-9]{5}-[0-9]{4}' arquivo.txt
```

### Buscar números inteiros de 3 dígitos
```bash
grep -Ewo '[0-9]{3}' arquivo.txt
```

### Linhas que começam com letras maiúsculas
```bash
grep -E '^[A-Z]+' arquivo.txt
```

### Linhas que terminam com letras minúsculas
```bash
grep -E '[a-z]+$' arquivo.txt
```

### Buscar `success` ou `failure`
```bash
grep -E 'success|failure' arquivo.txt
```

---

## 5) FIND

### Procurar arquivo por nome
```bash
find /caminho/diretorio -name 'arquivo.txt'
```

### Ignorar maiúsculas/minúsculas
```bash
find /caminho/diretorio -iname 'arquivo.txt'
```

### Procurar diretórios
```bash
find /caminho/diretorio -type d -name 'meu_diretorio'
```

### Procurar arquivos maiores que 100 MB
```bash
find /caminho/diretorio -type f -size +100M
```

### Arquivos modificados nos últimos 7 dias
```bash
find /caminho/diretorio -type f -mtime -7
```

### Procurar arquivos que contenham IP
```bash
find /caminho/diretorio -type f -exec grep -lE '([0-9]{1,3}\.){3}[0-9]{1,3}' {} \;
```

### Procurar arquivos que contenham data específica
```bash
find /caminho/diretorio -type f -exec grep -l '2024-03-10' {} \;
```

### Procurar arquivos que contenham uma frase
```bash
find /caminho/diretorio -type f -exec grep -l 'minha frase aqui' {} \;
```

### Executar comando para cada arquivo encontrado
```bash
find /caminho/diretorio -type f -name '*.log' -exec rm {} \;
```

### Alterar permissões de arquivos `.sh`
```bash
find /caminho/diretorio -type f -name '*.sh' -exec chmod +x {} \;
```

### Procurar apenas `.txt`
```bash
find /caminho/diretorio -type f -name '*.txt'
```

### Procurar múltiplas extensões
```bash
find /caminho/diretorio -type f \( -name '*.txt' -o -name '*.log' \)
```

### Procurar por regex
```bash
find /caminho/diretorio -type f -regex '.*\.\(txt\|log\|csv\)$'
```

### Listar arquivos ASCII
```bash
find /caminho/desejado -type f -exec file --mime {} + | grep 'charset=us-ascii'
```

### Procurar arquivos com tamanho exato
```bash
find . -type f -size 1033c
```

---

## 6) SORT / UNIQ

### Listar IPs únicos
```bash
cut -d ' ' -f 1 access.log | sort -u
```

### Contar ocorrências por IP
```bash
cut -d ' ' -f 1 access.log | sort | uniq -c
```

### Ordenar do menor para o maior número de ocorrências
```bash
cut -d ' ' -f 1 access.log | sort | uniq -c | sort -n
```

### Ordenar do maior para o menor número de ocorrências
```bash
cut -d ' ' -f 1 access.log | sort | uniq -c | sort -nr
```

### Top 5 IPs com mais tentativas
```bash
awk '{print $1}' "$logfile" | sort | uniq -c | sort -nr | head -5
```

---

## 7) Expressões Regulares úteis

### CPF
```regex
^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}-?[0-9]{2}$
```

### Inteiro
```regex
^[0-9]+$
```

### Inteiro positivo
```regex
^[1-9][0-9]*$
```

### Data `dd/mm/aaaa`
```regex
\b\d{2}/\d{2}/\d{4}\b
```

### Valor monetário no formato `$10.99`
```regex
\$\d+\.\d{2}
```

### Telefone `(xx)xxxxx-xxxx`
```regex
\([0-9]{2}\)[0-9]{5}-[0-9]{4}
```

### E-mail
```regex
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
```

### URL simples
```regex
https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}([/\w._-]*)?
```

---

## 8) IF de erro em Bash

### Exigir 1 parâmetro
```bash
#!/bin/bash
if [[ $# -eq 0 ]]; then
    echo "Erro: Você deve fornecer um parâmetro."
    echo "Uso: $0 <parametro>"
    exit 1
fi

echo "Parâmetro informado: $1"
```

### Exigir 2 parâmetros
```bash
#!/bin/bash
if [[ $# -lt 2 ]]; then
    echo "Erro: Você deve fornecer dois parâmetros."
    echo "Uso: $0 <parametro1> <parametro2>"
    exit 1
fi

echo "Parâmetro 1: $1"
echo "Parâmetro 2: $2"
```

### Verificar se parâmetros estão vazios
```bash
#!/bin/bash
if [[ -z "$1" || -z "$2" ]]; then
    echo "Erro: Nenhum dos parâmetros pode estar vazio."
    echo "Uso: $0 <parametro1> <parametro2>"
    exit 1
fi

echo "Parâmetro 1: $1"
echo "Parâmetro 2: $2"
```

### Verificar se o primeiro parâmetro é número
```bash
#!/bin/bash
if [[ $# -eq 0 || ! "$1" =~ ^[0-9]+$ ]]; then
    echo "Erro: Você deve fornecer um número como parâmetro."
    echo "Uso: $0 <numero>"
    exit 1
fi

echo "Número informado: $1"
```

### Verificar se arquivo existe
```bash
#!/bin/bash
if [[ $# -eq 0 ]]; then
    echo "Erro: Informe o caminho de um arquivo."
    echo "Uso: $0 <caminho_do_arquivo>"
    exit 1
fi

if [[ ! -f "$1" ]]; then
    echo "Erro: O arquivo '$1' não existe."
    exit 1
fi

echo "O arquivo '$1' existe."
```

### Verificar se diretório existe
```bash
#!/bin/bash
DIRETORIO="/caminho/do/diretorio"

if [[ -d "$DIRETORIO" ]]; then
    echo "O diretório $DIRETORIO existe."
else
    echo "O diretório $DIRETORIO não existe."
fi
```

### Verificar se variável não está vazia
```bash
VAR="Texto"

if [[ -n "$VAR" ]]; then
    echo "A variável não está vazia!"
else
    echo "A variável está vazia!"
fi
```

---

## 9) WHILE e FOR

### Ler arquivo linha por linha
```bash
#!/bin/bash
arquivo="lista.txt"

while IFS= read -r linha; do
    echo "Linha: $linha"
done < "$arquivo"
```

### Ler CSV com separador vírgula
```bash
#!/bin/bash
arquivo="dados.csv"

while IFS=, read -r nome idade; do
    echo "Nome: $nome - Idade: $idade"
done < "$arquivo"
```

### `while` aninhado
```bash
#!/bin/bash
arquivo="hobbies.csv"

while IFS= read -r linha; do
    nome=$(echo "$linha" | cut -d',' -f1)
    hobbies=$(echo "$linha" | cut -d',' -f2-)

    echo "Nome: $nome"
    echo "Hobbies:"

    echo "$hobbies" | tr ',' '\n' | while IFS= read -r hobby; do
        echo "  - $hobby"
    done

    echo
done < "$arquivo"
```

### Ler dois arquivos ao mesmo tempo
```bash
#!/bin/bash
arquivo_nomes="nomes.txt"
arquivo_idades="idades.txt"

paste "$arquivo_nomes" "$arquivo_idades" | while IFS=$'\t' read -r nome idade; do
    echo "$nome tem $idade anos"
done
```

### `for` com sequência
```bash
#!/bin/bash
for i in {1..5}; do
    echo "Número: $i"
done
```

### `for` com arquivos
```bash
#!/bin/bash
for arquivo in *.txt; do
    echo "Arquivo encontrado: $arquivo"
done
```

### `for` com `seq`
```bash
#!/bin/bash
for i in $(seq 0 2 10); do
    echo "Valor: $i"
done
```

### Duplo `for`
```bash
#!/bin/bash
usuarios=("alice" "bob" "charlie")
permissoes=("leitura" "escrita" "execução")

for usuario in "${usuarios[@]}"; do
    for permissao in "${permissoes[@]}"; do
        echo "Atribuindo permissão $permissao ao usuário $usuario"
    done
done
```

### Processar arquivos em vários diretórios
```bash
#!/bin/bash
diretorios=("/var/logs/app1" "/var/logs/app2" "/var/logs/app3")

for dir in "${diretorios[@]}"; do
    echo "Verificando diretório: $dir"
    for arquivo in "$dir"/*.log; do
        if [[ -f "$arquivo" ]]; then
            echo "Compactando $arquivo..."
            gzip "$arquivo"
        fi
    done
done
```

### Testar conectividade entre servidores
```bash
#!/bin/bash
servidores=("server1" "server2" "server3")

for origem in "${servidores[@]}"; do
    for destino in "${servidores[@]}"; do
        if [[ "$origem" != "$destino" ]]; then
            echo "Testando conexão de $origem para $destino..."
            ping -c 1 "$destino" > /dev/null && echo "OK" || echo "Falha"
        fi
    done
done
```

### Esperar até que um arquivo exista
```bash
#!/bin/bash
arquivo="meuarquivo.txt"

while [[ ! -f "$arquivo" ]]; do
    echo "Aguardando a criação de $arquivo..."
    sleep 2
done

echo "O arquivo $arquivo foi encontrado!"
```

---

## 10) Correções importantes

### Aspas incorretas
Em vários exemplos, as aspas tipográficas devem ser substituídas por aspas simples normais:

Errado:
```bash
awk ‘{print $1,$2,$3}’
```

Correto:
```bash
awk '{print $1,$2,$3}'
```

### `egrep`
Prefira:
```bash
grep -E
```
em vez de:
```bash
egrep
```

### `/etc/passwd` com terceira coluna maior que 100
Para exibir a linha inteira:
```bash
awk -F ':' '$3 > 100' /etc/passwd
```

### Regex de e-mail
Uma forma melhor:
```regex
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
```

### Buscar linhas entre dois marcadores
Melhor usar:
```bash
sed -n '/2468/,/4664/p' arquivo.txt
```

ou

```bash
awk '/2468/,/4664/' arquivo.txt
```

---

## 11) Resumo rápido por ferramenta

### AWK
Ideal para:
- trabalhar com colunas
- fazer filtros
- somas e relatórios
- regex com lógica

### SED
Ideal para:
- substituir texto
- editar linhas
- remover linhas
- imprimir intervalos

### CUT
Ideal para:
- extrair campos fixos
- extrair caracteres por posição

### GREP
Ideal para:
- localizar padrões
- buscar palavras
- filtrar linhas com regex

### FIND
Ideal para:
- localizar arquivos
- aplicar ações em lote
- buscar por nome, tamanho, data e conteúdo

### SORT / UNIQ
Ideal para:
- ordenar
- remover duplicatas
- contar ocorrências
