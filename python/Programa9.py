# Programa9.py
def contar_case(s: str):
    upper = sum(1 for ch in s if ch.isalpha() and ch.isupper())
    lower = sum(1 for ch in s if ch.isalpha() and ch.islower())
    return upper, lower

if __name__ == "__main__":
    frase = input("Digite uma sentença: ")
    up, low = contar_case(frase)
    print(f"UPPER: {up}")
    print(f"LOWER: {low}")
