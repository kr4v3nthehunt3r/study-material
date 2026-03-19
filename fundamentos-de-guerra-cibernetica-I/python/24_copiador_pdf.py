"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 24_copiador_pdf.py
Descrição: Procura arquivos PDF em uma árvore de diretórios, copia e renomeia sequencialmente.
"""

import os
import shutil


def copiar_pdfs(caminho_inicial, pasta_destino):
    """Copia arquivos PDF encontrados e renomeia sequencialmente."""
    # Cria a pasta de destino caso ela ainda não exista.
    os.makedirs(pasta_destino, exist_ok=True)

    # Inicializa o contador dos nomes sequenciais.
    contador = 1

    # Percorre a árvore de diretórios a partir do caminho inicial.
    for raiz, _, arquivos in os.walk(caminho_inicial):
        for arquivo in arquivos:
            # Processa somente arquivos com extensão .pdf.
            if arquivo.lower().endswith('.pdf'):
                origem = os.path.join(raiz, arquivo)
                destino = os.path.join(pasta_destino, f'pdf_{contador:03d}.pdf')

                # Copia o PDF para a pasta de destino.
                shutil.copy2(origem, destino)
                print(f'Copiado: {origem} -> {destino}')
                contador += 1

    # Retorna a quantidade total de PDFs copiados.
    return contador - 1


def main():
    """Função principal do programa."""
    # Solicita ao usuário o diretório inicial da busca.
    caminho_inicial = input('Digite o caminho inicial para busca: ').strip()

    # Solicita ao usuário a pasta de destino dos arquivos copiados.
    pasta_destino = input('Digite o caminho da pasta de destino: ').strip()

    # Realiza a cópia dos arquivos PDF encontrados.
    total = copiar_pdfs(caminho_inicial, pasta_destino)

    # Exibe o resultado final do processamento.
    if total == 0:
        print('Nenhum arquivo PDF foi encontrado.')
    else:
        print(f'Cópia concluída com sucesso. Total de arquivos copiados: {total}')


# Ponto de entrada do script.
if __name__ == '__main__':
    main()
