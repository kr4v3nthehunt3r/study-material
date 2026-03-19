"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 08_verificador_palindromo.py
Descrição: Verifica se uma string é palíndromo.
"""


def eh_palindromo(texto):
    """Retorna True se o texto informado for um palíndromo."""
    # Remove espaços extras nas extremidades e padroniza para minúsculas.
    texto_tratado = texto.strip().lower()

    # Compara o texto com sua versão invertida.
    return texto_tratado == texto_tratado[::-1]


def main():
    """Função principal do programa."""
    # Solicita ao usuário a string que será verificada.
    texto = input("Digite uma palavra ou frase curta: ")

    # Verifica se o texto é palíndromo.
    if eh_palindromo(texto):
        print("Palíndromo")
    else:
        print("Não é palíndromo")


# Ponto de entrada do script.
if __name__ == "__main__":
    main()
