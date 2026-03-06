# Programa19.py
ARQUIVO = "lista.txt"
VEICULOS = [
    "Gol",
    "Uno",
    "Palio",
    "EcoSport",
    "Clio",
    "Strada",
    "Gol",
    "Uno",
    "Palio",
    "Golf"
]

def gravar_lista(caminho: str, itens):
    with open(caminho, "w", encoding="utf-8") as f:
        for item in itens:
            f.write(item + "\n")

if __name__ == "__main__":
    gravar_lista(ARQUIVO, VEICULOS)
    print(f"Lista gravada em {ARQUIVO}")
