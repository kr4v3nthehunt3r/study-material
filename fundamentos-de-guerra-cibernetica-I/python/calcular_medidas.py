#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: calcular_medidas.py
Descrição do módulo:
    Calcula o dobro, o triplo e a raiz quadrada de um número.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import math
import sys

def main() -> None:
    """Lê um número e exibe medidas matemáticas básicas."""
    print("--- Dobro, Triplo e Raiz Quadrada ---")
    try:
        entrada = input("Digite um número: ").strip().replace(",", ".")
        if not entrada:
            raise ValueError("Nenhum valor foi informado.")

        numero = float(entrada)
        print("-" * 45)
        print(f"[*] Número:  {numero}")
        print(f"[*] Dobro:   {numero * 2}")
        print(f"[*] Triplo:  {numero * 3}")

        if numero < 0:
            print("[*] Raiz:    não definida nos reais para número negativo.")
        else:
            print(f"[*] Raiz:    {math.sqrt(numero):.2f}")
        print("-" * 45)
    except ValueError as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
