#!/bin/bash

# Verifica se o arquivo existe antes de iniciar
if [ ! -f "exercicio8.txt" ]; then
    echo "Erro: O arquivo exercicio8.txt não foi encontrado no diretório atual."
    exit 1
fi

echo "--- Iniciando Tratamento do Arquivo exercicio8.txt ---"
echo ""

# a) Buscar linhas que contenham a palavra "false"
echo "a) Linhas contendo 'false':"
grep "false" exercicio8.txt
echo "----------------------------------------------------"

# b) Extrair o primeiro campo (separador :)
echo "b) Primeiro campo de cada linha (Usuários):"
cut -d ':' -f 1 exercicio8.txt
echo "----------------------------------------------------"

# c) Extrair o terceiro campo e somar os valores
echo "c) Soma do terceiro campo (ex: UIDs):"
awk -F ':' '{ soma += $3 } END { print "Soma Total:", soma }' exercicio8.txt
echo "----------------------------------------------------"

# d) Substituir "nologin" por "semlogin"
# Nota: O sed aqui exibe na tela sem alterar o arquivo original (-i não utilizado)
echo "d) Substituindo 'nologin' por 'semlogin' (exibição):"
sed 's/nologin/semlogin/g' exercicio8.txt
echo "----------------------------------------------------"

# e) Exibir as últimas 3 linhas
echo "e) Últimas 3 linhas do arquivo:"
tail -n 3 exercicio8.txt
echo "----------------------------------------------------"

# f) Exibir as primeiras 5 linhas
echo "f) Primeiras 5 linhas do arquivo:"
head -n 5 exercicio8.txt
echo "----------------------------------------------------"

echo "--- Processamento Concluído ---"