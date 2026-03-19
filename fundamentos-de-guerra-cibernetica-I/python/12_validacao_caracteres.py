"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 12_validacao_caracteres.py
Descrição: Verifica se uma string contém apenas caracteres alfanuméricos.
"""


def validar_alfanumerico(texto):
    """Retorna True se a string possuir apenas caracteres alfanuméricos."""
    # Usa o método isalnum para validar a string inteira.
    return texto.isalnum()


def main():
    """Função principal do programa."""
    # Solicita ao usuário a string que será validada.
    texto = input("Entrada: ")

    # Exibe o resultado da validação.
    if validar_alfanumerico(texto):
        print("Saída: Válida")
    else:
        print("Saída: Inválida")


# Ponto de entrada do programa.
if __name__ == "__main__":
    main()
