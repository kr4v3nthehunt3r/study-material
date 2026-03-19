"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 03_media_de_notas.py
Descrição: Lê duas notas digitadas pelo usuário, calcula e exibe a média.
"""

# Autor: Kr4v3n


def calcular_media(nota1, nota2):
    """Retorna a média aritmética entre duas notas."""
    # Soma as notas e divide por 2.
    return (nota1 + nota2) / 2


def main():
    """Função principal do programa."""
    # Solicita a primeira nota ao usuário.
    nota1 = float(input("Digite a primeira nota: "))

    # Solicita a segunda nota ao usuário.
    nota2 = float(input("Digite a segunda nota: "))

    # Calcula a média final das duas notas.
    media = calcular_media(nota1, nota2)

    # Exibe o resultado calculado.
    print(f"Média: {media}")


# Executa o programa somente quando chamado diretamente.
if __name__ == "__main__":
    main()
