#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Analisa um arquivo de texto e informa quantidade de linhas e de caracteres.
"""

import argparse
import os
import sys


def analisar_arquivo(caminho: str) -> tuple[int, int]:
    """Retorna o total de linhas e caracteres de um arquivo."""
    if not os.path.isfile(caminho):
        raise FileNotFoundError(f"O arquivo '{caminho}' não foi encontrado.")

    with open(caminho, "r", encoding="utf-8", errors="ignore") as arquivo:
        linhas = arquivo.readlines()

    total_linhas = len(linhas)
    total_caracteres = sum(len(linha) for linha in linhas)
    return total_linhas, total_caracteres


def main() -> None:
    """Ponto de entrada do script."""
    parser = argparse.ArgumentParser(description="Analisador de arquivo texto")
    parser.add_argument("arquivo", help="Caminho do arquivo a ser analisado")
    args = parser.parse_args()

    try:
        linhas, caracteres = analisar_arquivo(args.arquivo)

        print("-" * 35)
        print(f"[*] Arquivo: {os.path.basename(args.arquivo)}")
        print(f"    - Linhas:     {linhas}")
        print(f"    - Caracteres: {caracteres}")
        print("-" * 35)

    except FileNotFoundError as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)
    except Exception as erro:
        print(f"[-] Erro ao ler o arquivo: {erro}")
        sys.exit(1)


if __name__ == "__main__":
    main()
