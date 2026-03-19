"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 11_copiador_csv.py
Descrição: Procura arquivos CSV em uma árvore de diretórios, copia e renomeia sequencialmente.
"""

import os
import shutil


def copiar_csv(caminho_inicial, pasta_destino):
    """Copia arquivos CSV encontrados e renomeia sequencialmente."""
    # Garante a existência da pasta de destino.
    os.makedirs(pasta_destino, exist_ok=True)

    # Inicializa o contador usado no nome dos arquivos copiados.
    contador = 1

    # Percorre toda a árvore de diretórios a partir do caminho inicial.
    for raiz, _, arquivos in os.walk(caminho_inicial):
        for arquivo in arquivos:
            # Verifica se o arquivo atual possui a extensão .csv.
            if arquivo.lower().endswith('.csv'):
                origem = os.path.join(raiz, arquivo)
                destino = os.path.join(pasta_destino, f"arquivo_{contador:03d}.csv")

                # Copia o arquivo preservando os metadados principais.
                shutil.copy2(origem, destino)
                print(f"Copiado: {origem} -> {destino}")
                contador += 1

    # Retorna a quantidade total de arquivos copiados.
    return contador - 1


def main():
    """Função principal do programa."""
    # Lê o caminho inicial onde será feita a busca.
    caminho_inicial = input("Digite o caminho inicial para busca: ").strip()

    # Lê o caminho da pasta onde os arquivos copiados serão salvos.
    pasta_destino = input("Digite o caminho da pasta de destino: ").strip()

    # Executa a cópia dos arquivos CSV encontrados.
    total = copiar_csv(caminho_inicial, pasta_destino)

    # Exibe a mensagem final conforme o resultado obtido.
    if total == 0:
        print("Nenhum arquivo CSV foi encontrado.")
    else:
        print(f"Cópia concluída com sucesso. Total de arquivos copiados: {total}")


# Inicia a execução do script.
if __name__ == "__main__":
    main()
