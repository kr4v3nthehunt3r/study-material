# Programa11.py
import os
import shutil
import glob

def copiar_csvs(caminho_inicial: str, pasta_destino: str):
    os.makedirs(pasta_destino, exist_ok=True)
    contador = 1

    # Usando os.walk para percorrer recursivamente
    for raiz, _, arquivos in os.walk(caminho_inicial):
        for nome in arquivos:
            if nome.lower().endswith('.csv'):
                origem = os.path.join(raiz, nome)
                novo_nome = f"arquivo_{contador:03d}.csv"
                destino = os.path.join(pasta_destino, novo_nome)
                shutil.copy2(origem, destino)
                print(f"Copiado: {origem} -> {destino}")
                contador += 1

if __name__ == "__main__":
    caminho = input("Caminho inicial para buscar .csv: ").strip() or "."
    destino = input("Pasta de destino para copiar os .csv: ").strip() or "./csv_copiados"
    copiar_csvs(caminho, destino)
    print("Concluído.")
