# Programa12.py
def valida_alfanumerico(s: str) -> bool:
    return s.isalnum()

if __name__ == "__main__":
    entrada = input("Digite a string: ")
    if valida_alfanumerico(entrada):
        print("Válida")
    else:
        print("Inválida")
