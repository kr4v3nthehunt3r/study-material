"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 09_contador_case.py
Descrição: Conta quantas letras maiúsculas e minúsculas existem em uma sentença.
"""


def contar_case(sentenca):
    """Conta letras maiúsculas e minúsculas em uma sentença."""
    # Conta apenas caracteres alfabéticos maiúsculos.
    maiusculas = sum(1 for caractere in sentenca if caractere.isalpha() and caractere.isupper())

    # Conta apenas caracteres alfabéticos minúsculos.
    minusculas = sum(1 for caractere in sentenca if caractere.isalpha() and caractere.islower())

    # Retorna as duas contagens.
    return maiusculas, minusculas


def main():
    """Função principal do programa."""
    # Recebe a sentença que será analisada.
    sentenca = input("Entrada: ")

    # Obtém a contagem de letras maiúsculas e minúsculas.
    upper, lower = contar_case(sentenca)

    # Exibe os resultados no formato solicitado.
    print("\nSaída:")
    print(f"UPPER: {upper}")
    print(f"LOWER: {lower}")


# Executa o script se ele for chamado diretamente.
if __name__ == "__main__":
    main()
