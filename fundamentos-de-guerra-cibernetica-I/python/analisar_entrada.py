#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: analisar_entrada.py
Descrição do módulo:
    Analisa uma entrada textual e exibe propriedades booleanas da string.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import sys

def main() -> None:
    """Função principal."""
    print("--- Analisador de Entrada ---")
    try:
        valor = input("Digite algo para análise: ")
        print("-" * 50)
        print(f"[*] Tipo primitivo:         {type(valor).__name__}")
        print(f"[*] Só espaços?            {valor.isspace()}")
        print(f"[*] É numérico?            {valor.isnumeric()}")
        print(f"[*] É alfanumérico?        {valor.isalnum()}")
        print(f"[*] É alfabético?          {valor.isalpha()}")
        print(f"[*] Está em maiúsculas?    {valor.isupper()}")
        print(f"[*] Está em minúsculas?    {valor.islower()}")
        print(f"[*] Quantidade de chars:   {len(valor)}")
        print("-" * 50)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
