#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: contar_linhas_caracteres.py
Descrição do módulo:
    Conta linhas, caracteres e caracteres sem espaços de um arquivo texto.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import sys
from pathlib import Path

def analisar_arquivo(caminho: Path) -> tuple[int, int, int]:
    """Retorna total de linhas, caracteres e caracteres sem espaços."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    if not caminho.is_file():
        raise ValueError(f"O caminho informado não é um arquivo: {caminho}")

    conteudo = caminho.read_text(encoding="utf-8", errors="ignore")
    total_linhas = len(conteudo.splitlines())
    total_caracteres = len(conteudo)
    caracteres_sem_espaco = len("".join(conteudo.split()))
    return total_linhas, total_caracteres, caracteres_sem_espaco

def main() -> None:
    """Executa a análise do arquivo."""
    parser = argparse.ArgumentParser(description="Contador de linhas e caracteres")
    parser.add_argument("arquivo", help="Arquivo a ser analisado")
    args = parser.parse_args()

    try:
        linhas, caracteres, sem_espaco = analisar_arquivo(Path(args.arquivo))
        print("-" * 40)
        print(f"[*] Linhas:                 {linhas}")
        print(f"[*] Caracteres totais:     {caracteres}")
        print(f"[*] Caracteres sem espaço: {sem_espaco}")
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
