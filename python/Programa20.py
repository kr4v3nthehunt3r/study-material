# Programa20.py
ARQUIVO_ORIG = "lista.txt"
ARQUIVO_INV = "lista2.txt"

def inverter_arquivo(origem: str, destino: str):
    with open(origem, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    linhas_invertidas = [l.rstrip("\n") for l in reversed(linhas)]
    with open(destino, "w", encoding="utf-8") as f:
        for l in linhas_invertidas:
            f.write(l + "\n")

if __name__ == "__main__":
    inverter_arquivo(ARQUIVO_ORIG, ARQUIVO_INV)
    print(f"Inversão concluída: {ARQUIVO_INV}")
