#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Lê e exibe o conteúdo de um arquivo de texto de forma segura.
"""

import sys
from pathlib import Path


def ler_arquivo(caminho: str) -> None:
    """Lê e exibe o conteúdo de um arquivo textual."""
    arquivo = Path(caminho)
    print(f"[*] Verificando arquivo: {arquivo.resolve()}")

    if not arquivo.exists():
        print(f"[-] O arquivo '{arquivo.name}' não existe.")
        sys.exit(1)

    if not arquivo.is_file():
        print(f"[-] '{arquivo.name}' não é um arquivo regular.")
        sys.exit(1)

    try:
        with arquivo.open("r", encoding="utf-8", errors="ignore") as conteudo:
            texto = conteudo.read()

        print("-" * 40)
        if texto.strip():
            print(texto)
        else:
            print("[!] O arquivo está vazio.")
        print("-" * 40)

    except PermissionError:
        print(f"[-] Sem permissão para ler '{arquivo.name}'.")
        sys.exit(1)
    except Exception as erro:
        print(f"[-] Erro ao processar o arquivo: {erro}")
        sys.exit(1)


def main() -> None:
    """Ponto de entrada do script."""
    arquivo_alvo = sys.argv[1] if len(sys.argv) > 1 else "brasil.txt"

    try:
        ler_arquivo(arquivo_alvo)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)


if __name__ == "__main__":
    main()
