"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 19_gravador_lista.py
Descrição: Grava uma lista de veículos em um arquivo texto, um item por linha.
"""


def gravar_lista(caminho_arquivo, itens):
    """Grava os itens da lista em um arquivo, um por linha."""
    # Abre o arquivo em modo de escrita para sobrescrever seu conteúdo.
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        for item in itens:
            # Remove espaços desnecessários e grava o item em uma nova linha.
            arquivo.write(item.strip() + '\n')


def main():
    """Função principal do programa."""
    # Define a lista solicitada no exercício.
    itens = [
        'Gol',
        'Uno',
        'Palio',
        'EcoSport',
        'Clio',
        'Gol',
        'Strada',
        'Uno',
        'Palio',
        'Golf',
    ]

    # Define o nome do arquivo de saída.
    caminho_arquivo = 'lista.txt'

    # Grava a lista no arquivo texto.
    gravar_lista(caminho_arquivo, itens)

    # Exibe mensagem de confirmação.
    print(f"Lista gravada em '{caminho_arquivo}'.")


# Executa o script diretamente.
if __name__ == '__main__':
    main()
