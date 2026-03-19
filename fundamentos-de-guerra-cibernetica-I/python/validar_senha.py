#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: validar_senha.py
Descrição do módulo:
    Valida a força de uma senha com base em regras de complexidade.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import getpass
import re
import sys

# Importações utilizadas por este módulo.

PADRAO_SENHA = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$')

def senha_valida(senha: str) -> bool:
    """Verifica se a senha atende ao padrão configurado."""
    return bool(PADRAO_SENHA.fullmatch(senha))

def main() -> None:
    """Função principal."""
    print("--- Validador de Senha ---")
    print("Critérios: 6 a 12 caracteres, maiúsculas, minúsculas, números e símbolos $ # @")
    try:
        senha = getpass.getpass("Digite a senha para validação: ")
        if senha_valida(senha):
            print("[+] Senha válida conforme os critérios definidos.")
        else:
            print("[-] Senha fora do padrão exigido.")
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
