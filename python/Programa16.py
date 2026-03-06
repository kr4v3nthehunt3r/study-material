# Programa16.py
import os

CAMINHO = "exemplo.txt"

def criar_exemplo_se_nao_existir(caminho: str):
    if not os.path.exists(caminho):
        conteudo = [
            "Linha 1: Este é um arquivo de exemplo.\n",
            "Linha 2: Use este arquivo para testar a leitura.\n",
            "Linha 3: Fim do arquivo.\n"
        ]
        with open(caminho, "w", encoding="utf-8") as f:
            f.writelines(conteudo)

def ler_e_imprimir(caminho: str):
    with open(caminho, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f, start=1):
            print(f"{i}: {linha.rstrip()}")

if __name__ == "__main__":
    criar_exemplo_se_nao_existir(CAMINHO)
    print(f"Lendo arquivo: {CAMINHO}")
    ler_e_imprimir(CAMINHO)
