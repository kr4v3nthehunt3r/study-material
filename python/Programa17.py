# Programa17.py
import os

CAMINHO = "exemplo.txt"

def estatisticas_arquivo(caminho: str):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    linhas = 0
    caracteres = 0
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            linhas += 1
            caracteres += len(linha)  # inclui espaços e '\n'
    return linhas, caracteres

if __name__ == "__main__":
    try:
        linhas, caracteres = estatisticas_arquivo(CAMINHO)
        print(f"Quantidade de linhas: {linhas}")
        print(f"Quantidade total de caracteres: {caracteres}")
    except FileNotFoundError as e:
        print(e)

