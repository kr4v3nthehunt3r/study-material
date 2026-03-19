#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Calcula o sucessor e o antecessor de um número inteiro informado pelo usuário.
"""

import sys


def main() -> None:
    """Executa a leitura do número e exibe sucessor e antecessor."""
    print("--- Sucessor e Antecessor ---")

    try:
        valor = input("Digite um número inteiro: ").strip()
        if not valor:
            raise ValueError("Nenhum número foi informado.")

        numero = int(valor)

        print("-" * 40)
        print(f"[*] Número informado: {numero}")
        print(f"    - Antecessor: {numero - 1}")
        print(f"    - Sucessor:   {numero + 1}")
        print("-" * 40)

    except ValueError as erro:
        print(f"[-] Erro de entrada: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
