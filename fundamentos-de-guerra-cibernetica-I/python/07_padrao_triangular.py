"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 07_padrao_triangular.py
Descrição: Imprime um padrão triangular numérico até a n-ésima linha.
"""


def imprimir_padrao(n):
    """Imprime o padrão triangular de 1 até n."""
    # Percorre as linhas de 1 até n.
    for linha in range(1, n + 1):
        # Gera os números da linha atual em formato de texto.
        conteudo_linha = " ".join(str(numero) for numero in range(1, linha + 1))

        # Exibe a linha formatada.
        print(conteudo_linha)


def main():
    """Função principal do programa."""
    # Solicita ao usuário o número de linhas do padrão.
    n = int(input("Digite o valor de n: "))

    # Chama a função responsável por imprimir o padrão.
    imprimir_padrao(n)


# Executa o script diretamente.
if __name__ == "__main__":
    main()
