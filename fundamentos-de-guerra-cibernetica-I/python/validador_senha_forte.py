#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Valida a complexidade de uma senha conforme critérios mínimos definidos.
"""

import getpass
import re
import sys


PADRAO_SENHA = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$"
)


def main() -> None:
    """Solicita uma senha ao usuário e valida sua complexidade."""
    print("--- Validador de Senha Forte ---")
    print("Critérios:")
    print(" - 6 a 12 caracteres")
    print(" - Pelo menos uma letra minúscula")
    print(" - Pelo menos uma letra maiúscula")
    print(" - Pelo menos um número")
    print(" - Pelo menos um símbolo entre: $ # @")
    print("-" * 40)

    try:
        senha = getpass.getpass("Digite a senha para validação: ")

        if PADRAO_SENHA.fullmatch(senha):
            print("[+] Senha válida.")
        else:
            print("[-] Senha fora dos critérios estabelecidos.")
            print("    Revise tamanho, letras, número e símbolo especial.")

    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)


if __name__ == "__main__":
    main()
