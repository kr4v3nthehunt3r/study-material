"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 20_inversor_lista.py
Descrição: Lê lista.txt, inverte a ordem dos itens e grava o resultado em lista2.txt.
"""

from pathlib import Path


def ler_itens(caminho_arquivo):
    """Lê os itens de um arquivo texto e retorna em formato de lista."""
    # Lê o conteúdo linha por linha removendo quebras de linha.
    return Path(caminho_arquivo).read_text(encoding='utf-8').splitlines()


def gravar_itens(caminho_arquivo, itens):
    """Grava uma lista de itens em um arquivo texto, um por linha."""
    # Junta os itens com quebra de linha e grava no arquivo de destino.
    Path(caminho_arquivo).write_text('\n'.join(itens) + '\n', encoding='utf-8')


def main():
    """Função principal do programa."""
    # Define os arquivos de entrada e saída.
    arquivo_entrada = Path('lista.txt')
    arquivo_saida = 'lista2.txt'

    # Verifica se o arquivo de entrada existe antes de continuar.
    if not arquivo_entrada.exists():
        print("O arquivo 'lista.txt' não existe. Execute primeiro o Programa19.py.")
        return

    # Lê os itens do arquivo original.
    itens = ler_itens(arquivo_entrada)

    # Inverte a ordem dos itens da lista.
    itens_invertidos = list(reversed(itens))

    # Grava o resultado no novo arquivo.
    gravar_itens(arquivo_saida, itens_invertidos)

    # Informa ao usuário que o processo foi concluído.
    print(f"Lista invertida gravada em '{arquivo_saida}'.")


# Ponto de entrada do programa.
if __name__ == '__main__':
    main()
