#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: ler_linhas_validas.py
Descrição do módulo:
    Lê um arquivo texto linha a linha, ignora linhas vazias e conta linhas válidas.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import sys
from pathlib import Path

def ler_linhas_validas(caminho: Path) -> int:
    """Exibe apenas linhas não vazias e retorna a quantidade encontrada."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    if not caminho.is_file():
        raise ValueError(f"O caminho informado não é um arquivo: {caminho}")

    contador = 0
    with caminho.open("r", encoding="utf-8", errors="ignore") as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            conteudo = linha.strip()
            if not conteudo:
                continue
            print(f"{numero_linha:>4}: {conteudo}")
            contador += 1
    return contador

def main() -> None:
    """Função principal do script."""
    parser = argparse.ArgumentParser(description="Leitor de linhas não vazias")
    parser.add_argument("arquivo", help="Arquivo de texto para leitura")
    args = parser.parse_args()

    try:
        total = ler_linhas_validas(Path(args.arquivo))
        print("-" * 35)
        print(f"[*] Total de linhas não vazias: {total}")
        print("-" * 35)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
