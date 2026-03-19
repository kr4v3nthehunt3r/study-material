"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 17_estatisticas_arquivo.py
Descrição: Exibe a quantidade de linhas e a quantidade total de caracteres de um arquivo de texto.
"""

from pathlib import Path


def garantir_arquivo(caminho_arquivo):
    """Cria um arquivo de exemplo caso ele ainda não exista."""
    arquivo = Path(caminho_arquivo)

    # Cria o arquivo somente se ele não existir.
    if not arquivo.exists():
        arquivo.write_text(
            "Linha 1: Exemplo de conteúdo.\nLinha 2: Arquivo criado automaticamente.\n",
            encoding='utf-8',
        )

    # Retorna o caminho do arquivo pronto para uso.
    return arquivo


def calcular_estatisticas(caminho_arquivo):
    """Calcula a quantidade de linhas e caracteres do arquivo."""
    # Lê todo o conteúdo do arquivo de uma vez.
    conteudo = Path(caminho_arquivo).read_text(encoding='utf-8')

    # Conta as linhas separando o texto pelas quebras de linha.
    quantidade_linhas = len(conteudo.splitlines())

    # Conta todos os caracteres, incluindo espaços e quebras de linha.
    quantidade_caracteres = len(conteudo)

    # Retorna as estatísticas calculadas.
    return quantidade_linhas, quantidade_caracteres


def main():
    """Função principal do programa."""
    # Define o arquivo usado no exercício.
    caminho_arquivo = 'exemplo.txt'

    # Garante a existência do arquivo antes do processamento.
    arquivo = garantir_arquivo(caminho_arquivo)

    # Obtém as estatísticas do arquivo informado.
    linhas, caracteres = calcular_estatisticas(arquivo)

    # Exibe os resultados na tela.
    print(f"Quantidade de linhas: {linhas}")
    print(f"Quantidade total de caracteres: {caracteres}")


# Executa o programa quando chamado diretamente.
if __name__ == '__main__':
    main()
