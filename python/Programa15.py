# Programa15.py
import re

def encontra_padrao(texto: str):
    # \b indica borda de palavra; [A-ZÁÀÂÃÉÈÍÓÔÕÚÇÑ] inclui letras maiúsculas com acento; \w* permite letras/dígitos/underscore; \d$ garante termina em dígito
    padrao = re.compile(r'\b[A-ZÁÀÂÃÉÈÍÓÔÕÚÇÑ][\w\-]*\d\b')
    return padrao.findall(texto)

if __name__ == "__main__":
    texto = input("Digite o texto: ")
    resultados = encontra_padrao(texto)
    if resultados:
        print(", ".join(resultados))
    else:
        print("Nenhuma palavra encontrada")
