"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 16_leitor_arquivo.py
Descrição: Abre um arquivo de texto, cria um exemplo se ele não existir e imprime o conteúdo linha por linha.
"""

from pathlib import Path


def garantir_arquivo(caminho_arquivo):
    """Cria um arquivo de exemplo caso ele ainda não exista."""
    arquivo = Path(caminho_arquivo)

    # Cria o arquivo apenas se ele ainda não existir.
    if not arquivo.exists():
        arquivo.write_text(
            "Linha 1: Exemplo de conteúdo.\nLinha 2: Arquivo criado automaticamente.\n",
            encoding="utf-8",
        )

    # Retorna o objeto de caminho do arquivo.
    return arquivo


def ler_linhas(caminho_arquivo):
    """Lê e imprime o conteúdo do arquivo linha por linha."""
    # Abre o arquivo em modo leitura com codificação UTF-8.
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # Remove a quebra de linha final para evitar linhas em branco extras.
            print(linha.rstrip('\n'))


def main():
    """Função principal do programa."""
    # Define o nome do arquivo usado no exercício.
    caminho_arquivo = 'exemplo.txt'

    # Garante que o arquivo exista antes da leitura.
    arquivo = garantir_arquivo(caminho_arquivo)

    # Lê e exibe o conteúdo do arquivo.
    ler_linhas(arquivo)


# Ponto de entrada do script.
if __name__ == '__main__':
    main()
