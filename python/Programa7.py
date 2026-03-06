"""
Exercício 7: Padrão Triangular
"""

def imprimir_padrao_triangular(n: int):
    """
    Imprime um padrão triangular de números até a n-ésima linha.

    Args:
        n (int): O número de linhas a serem impressas.
    """
    if n < 1:
        print("O número de linhas deve ser pelo menos 1.")
        return

    # Itera sobre cada linha de 1 até n
    for i in range(1, n + 1):
        # Para cada linha 'i', cria uma lista de números de 1 até 'i'
        numeros_da_linha = [str(j) for j in range(1, i + 1)]
        # Junta os números com espaço e imprime
        print(" ".join(numeros_da_linha))

def main():
    """
    Função principal que solicita o número ao usuário e chama a impressão.
    """
    try:
        n_usuario = int(input("Digite o número de linhas para o padrão: "))
        imprimir_padrao_triangular(n_usuario)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()

