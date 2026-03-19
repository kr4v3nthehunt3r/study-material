#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Analisa propriedades básicas de uma string informada pelo usuário.
"""

import sys


def main() -> None:
    """Lê uma entrada textual e exibe características da string."""
    print("--- Analisador de Propriedades de Texto ---")

    try:
        valor = input("Digite algo para análise: ")

        print("-" * 50)
        print(f"Tipo primitivo:            {type(valor).__name__}")
        print(f"Só possui espaços?         {valor.isspace()}")
        print(f"É alfanumérico?            {valor.isalnum()}")
        print(f"É alfabético?              {valor.isalpha()}")
        print(f"Está em caixa alta?        {valor.isupper()}")
        print(f"Está em caixa baixa?       {valor.islower()}")
        print(f"Quantidade de caracteres:  {len(valor)}")
        print("-" * 50)

    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)


if __name__ == "__main__":
    main()
