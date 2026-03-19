#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: sucessor_antecessor_int.py
Descrição do módulo:
    Calcula o sucessor e o antecessor de um número inteiro informado.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import sys

def main() -> None:
    """Função principal."""
    print("--- Sucessor e Antecessor ---")
    try:
        entrada = input("Digite um número inteiro: ").strip()
        if not entrada:
            raise ValueError("Nenhum número foi informado.")
        numero = int(entrada)
        print("-" * 35)
        print(f"[*] Número:     {numero}")
        print(f"[*] Sucessor:   {numero + 1}")
        print(f"[*] Antecessor: {numero - 1}")
        print("-" * 35)
    except ValueError as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
