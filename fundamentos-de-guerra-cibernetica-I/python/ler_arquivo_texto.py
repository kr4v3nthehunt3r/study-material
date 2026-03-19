#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: ler_arquivo_texto.py
Descrição do módulo:
    Lê um arquivo texto com pathlib e mostra seu conteúdo de forma segura.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import sys
from pathlib import Path

def ler_arquivo(caminho: Path) -> str:
    """Lê o conteúdo de um arquivo texto."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    if not caminho.is_file():
        raise ValueError(f"O caminho informado não é um arquivo regular: {caminho}")
    return caminho.read_text(encoding="utf-8", errors="ignore")

def main() -> None:
    """Executa a leitura do arquivo."""
    parser = argparse.ArgumentParser(description="Leitor de arquivo texto")
    parser.add_argument("arquivo", nargs="?", default="brasil.txt", help="Arquivo a ser lido")
    args = parser.parse_args()

    try:
        conteudo = ler_arquivo(Path(args.arquivo))
        print("-" * 40)
        print(conteudo if conteudo.strip() else "[!] O arquivo está vazio.")
        print("-" * 40)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
