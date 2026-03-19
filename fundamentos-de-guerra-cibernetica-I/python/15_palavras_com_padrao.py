"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 15_palavras_com_padrao.py
Descrição: Encontra palavras que começam com letra maiúscula e terminam com número.
"""

import re


def encontrar_palavras(texto):
    """Retorna as palavras que começam com maiúscula e terminam com número."""
    # Define um padrão que aceita letras acentuadas e termina obrigatoriamente com dígito.
    padrao = r"[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][A-Za-zÁÀÂÃÉÊÍÓÔÕÚÇáàâãéêíóôõúç]*\d"

    # Retorna todas as ocorrências encontradas no texto.
    return re.findall(padrao, texto)


def main():
    """Função principal do programa."""
    # Recebe o texto que será analisado.
    texto = input("Texto: ")

    # Procura as palavras que atendem ao padrão.
    palavras = encontrar_palavras(texto)

    # Exibe o resultado final.
    if palavras:
        print("Saída:", ", ".join(palavras))
    else:
        print("Saída: Nenhuma palavra encontrada")


# Executa o programa diretamente.
if __name__ == "__main__":
    main()
