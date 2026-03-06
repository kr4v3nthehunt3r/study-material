# Programa10.py
import random
import string

def gerar_senha(tamanho: int = 12) -> str:
    if tamanho < 12:
        raise ValueError("O tamanho mínimo é 12 caracteres.")
    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    digitos = string.digits
    simbolos = "!@#$%"

    # Garante pelo menos um de cada categoria
    senha_chars = [
        random.choice(minusculas),
        random.choice(maiusculas),
        random.choice(digitos),
        random.choice(simbolos),
    ]

    # Preenche o restante com uma mistura de todas as categorias
    todas = minusculas + maiusculas + digitos + simbolos
    senha_chars += [random.choice(todas) for _ in range(tamanho - len(senha_chars))]

    # Embaralha para não deixar os garantidos no começo
    random.shuffle(senha_chars)
    return ''.join(senha_chars)

if __name__ == "__main__":
    try:
        n = int(input("Tamanho da senha (mínimo 12): ") or "12")
    except ValueError:
        n = 12
    senha = gerar_senha(max(12, n))
    print("Senha gerada:", senha)
