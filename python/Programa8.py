# Programa8.py
import re

def eh_palindromo(s: str) -> bool:
    # Remove tudo que não for letra ou número e transforma em minúsculas
    s_limpa = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s_limpa == s_limpa[::-1]

if __name__ == "__main__":
    texto = input("Digite uma string: ")
    if eh_palindromo(texto):
        print("Palíndromo")
    else:
        print("Não é palíndromo")
