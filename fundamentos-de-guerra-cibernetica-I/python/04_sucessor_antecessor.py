"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 04_sucessor_antecessor.py
Descrição: Recebe um número inteiro e exibe seu antecessor, o número e seu sucessor.
"""


def obter_vizinhos(numero):
    """Retorna antecessor e sucessor de um número inteiro."""
    # Calcula o antecessor subtraindo 1.
    antecessor = numero - 1

    # Calcula o sucessor somando 1.
    sucessor = numero + 1

    # Retorna os dois valores calculados.
    return antecessor, sucessor


def main():
    """Função principal do programa."""
    # Solicita ao usuário um número inteiro.
    numero = int(input("Digite um número inteiro: "))

    # Obtém o antecessor e o sucessor do número informado.
    antecessor, sucessor = obter_vizinhos(numero)

    # Exibe os resultados na tela.
    print(f"Antecessor: {antecessor}")
    print(f"Número: {numero}")
    print(f"Sucessor: {sucessor}")


# Inicia a execução do script.
if __name__ == "__main__":
    main()
