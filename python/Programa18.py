# Programa18.py
TEXTO = "Brasil Acima de Tudo"
ARQUIVO_SAIDA = "palavras.txt"

def salvar_palavras_em_linhas(texto: str, caminho: str):
    palavras = texto.split()
    with open(caminho, "w", encoding="utf-8") as f:
        for p in palavras:
            f.write(p + "\n")

if __name__ == "__main__":
    salvar_palavras_em_linhas(TEXTO, ARQUIVO_SAIDA)
    print(f"Palavras salvas em {ARQUIVO_SAIDA}")
