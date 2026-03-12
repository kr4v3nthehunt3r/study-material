#!/bin/bash

# 1. Definição da URL alvo
URL_BASE="https://thehackernews.com"

echo "Coletando notícias de $URL_BASE..."
echo "--------------------------------------------------"

# 2. Extrai os links das matérias
# Filtramos a classe 'story-link' e usamos sed para extrair o valor do href
LINKS=$(lynx -source "$URL_BASE" | grep "class='story-link'" | sed -n "s/.*href='\([^']*\)'.*/\1/p")

# 3. Itera sobre cada link extraído
for LINK in $LINKS; do
    # Obtém o código fonte da página da matéria
    CONTEUDO_MATERIA=$(lynx -source "$LINK")

    # 4. Extrai o Título (Twitter Title)
    # Buscamos a meta tag e limpamos o conteúdo
    TITULO=$(echo "$CONTEUDO_MATERIA" | grep 'name="twitter:title"' | sed -n 's/.*content="\([^"]*\)".*/\1/p')

    # 5. Extrai a Descrição (Twitter Description)
    DESCRICAO=$(echo "$CONTEUDO_MATERIA" | grep 'name="twitter:description"' | sed -n 's/.*content="\([^"]*\)".*/\1/p')

    # 6. Imprime os resultados formatados
    if [ ! -z "$TITULO" ]; then
        echo "Título: $TITULO"
        echo "Descrição: $DESCRICAO"
        echo "Link: $LINK"
        echo "--------------------------------------------------"
    fi
done