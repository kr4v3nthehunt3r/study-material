#!/usr/bin/env python3

def main():
    """
    Recebe um número inteiro (via input) e mostra seu antecessor e sucessor.
    """
    # Pede ao usuário para inserir um número e o converte para inteiro.
    numero_str = input("Digite um número inteiro: ")
    numero = int(numero_str)

    # Calcula o antecessor e o sucessor.
    antecessor = numero - 1
    sucessor = numero + 1

    # Exibe os resultados formatados, conforme o exemplo.
    print(f"\nAntecessor: {antecessor}")
    print(f"Número: {numero}")
    print(f"Sucessor: {sucessor}")

if __name__ == "__main__":
    main()


