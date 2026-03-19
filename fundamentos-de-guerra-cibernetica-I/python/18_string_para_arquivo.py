"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 18_string_para_arquivo.py
Descrição: Divide uma string em palavras e grava cada palavra em uma linha de um arquivo.
"""


def salvar_palavras_em_arquivo(texto, caminho_arquivo):
    """Salva cada palavra do texto em uma linha separada do arquivo."""
    # Divide o texto em palavras usando espaços como separador.
    palavras = texto.split()

    # Abre o arquivo em modo de escrita para gravar as palavras.
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        for palavra in palavras:
            # Grava uma palavra por linha.
            arquivo.write(palavra + '\n')


def main():
    """Função principal do programa."""
    # Define a string solicitada no exercício.
    texto = 'Brasil Acima de Tudo'

    # Define o nome do arquivo de saída.
    caminho_arquivo = 'palavras.txt'

    # Salva cada palavra da string em uma linha do arquivo.
    salvar_palavras_em_arquivo(texto, caminho_arquivo)

    # Informa ao usuário que o arquivo foi criado com sucesso.
    print(f"Palavras salvas em '{caminho_arquivo}'.")


# Ponto de entrada do script.
if __name__ == '__main__':
    main()
