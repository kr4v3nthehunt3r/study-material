"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 21_remove_duplicatas.py
Descrição: Remove itens duplicados de lista.txt mantendo a primeira ocorrência e grava em lista3.txt.
"""

from pathlib import Path


def ler_itens(caminho_arquivo):
    """Lê os itens de um arquivo texto e os retorna em lista."""
    # Lê cada linha do arquivo removendo a quebra de linha final.
    return Path(caminho_arquivo).read_text(encoding='utf-8').splitlines()


def remover_duplicatas(itens):
    """Remove duplicatas preservando a ordem da primeira ocorrência."""
    # Cria um conjunto para controlar os itens já vistos.
    vistos = set()

    # Cria a lista que armazenará apenas os itens únicos.
    itens_unicos = []

    # Percorre todos os itens originais.
    for item in itens:
        # Adiciona somente itens que ainda não apareceram.
        if item not in vistos:
            vistos.add(item)
            itens_unicos.append(item)

    # Retorna a lista final sem duplicatas.
    return itens_unicos


def gravar_itens(caminho_arquivo, itens):
    """Grava uma lista de itens em um arquivo texto."""
    # Escreve cada item em uma linha do arquivo de saída.
    Path(caminho_arquivo).write_text('\n'.join(itens) + '\n', encoding='utf-8')


def main():
    """Função principal do programa."""
    # Define os arquivos utilizados neste exercício.
    arquivo_entrada = Path('lista.txt')
    arquivo_saida = 'lista3.txt'

    # Valida a existência do arquivo de entrada.
    if not arquivo_entrada.exists():
        print("O arquivo 'lista.txt' não existe. Execute primeiro o Programa19.py.")
        return

    # Lê os itens do arquivo original.
    itens = ler_itens(arquivo_entrada)

    # Remove as duplicatas mantendo a primeira ocorrência.
    itens_unicos = remover_duplicatas(itens)

    # Grava o resultado em um novo arquivo.
    gravar_itens(arquivo_saida, itens_unicos)

    # Exibe mensagem de confirmação.
    print(f"Lista sem duplicatas gravada em '{arquivo_saida}'.")


# Executa o script diretamente.
if __name__ == '__main__':
    main()
