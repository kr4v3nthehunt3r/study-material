"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 02_media_simples.py
Descrição: Calcula e exibe a média simples entre três números.
"""


def calcular_media(numero1, numero2, numero3):
    """Retorna a média aritmética de três números."""
    # Soma os três valores e divide pela quantidade de números.
    return (numero1 + numero2 + numero3) / 3


def main():
    """Função principal do programa."""
    # Define três números diretamente no código, conforme permitido pelo exercício.
    numero1 = 10
    numero2 = 20
    numero3 = 30

    # Calcula a média dos valores definidos.
    media = calcular_media(numero1, numero2, numero3)

    # Exibe o resultado final no formato esperado.
    print(f"Média de {numero1}, {numero2} e {numero3} = {media}")


# Ponto de entrada do script.
if __name__ == "__main__":
    main()
