#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Calcula dobro, triplo e raiz quadrada de um número informado.
"""

import math
import sys


def main() -> None:
    """Lê um número e exibe dobro, triplo e raiz quadrada."""
    print("--- Operações Básicas com Número ---")

    try:
        entrada = input("Digite um número: ").strip().replace(",", ".")
        if not entrada:
            raise ValueError("Nenhum valor foi informado.")

        numero = float(entrada)

        print("-" * 45)
        print(f"[*] Número analisado: {numero}")
        print(f"    - Dobro:  {numero * 2}")
        print(f"    - Triplo: {numero * 3}")

        if numero < 0:
            print("    - Raiz quadrada: não definida no conjunto dos reais.")
        else:
            print(f"    - Raiz quadrada: {math.sqrt(numero):.2f}")
        print("-" * 45)

    except ValueError as erro:
        print(f"[-] Erro de entrada: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)


if __name__ == "__main__":
    main()
