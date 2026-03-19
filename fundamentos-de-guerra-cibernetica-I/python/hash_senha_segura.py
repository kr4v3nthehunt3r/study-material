#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: hash_senha_segura.py
Descrição do módulo:
    Valida uma senha forte e armazena seu hash com PBKDF2-HMAC-SHA256.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import getpass
import os
import sys
from hashlib import pbkdf2_hmac

ITERACOES = 100_000

def validar_senha(senha: str) -> bool:
    """Verifica requisitos mínimos de força da senha."""
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(not c.isalnum() for c in senha):
        return False
    return True

def gerar_hash(senha: str) -> str:
    """Gera um hash PBKDF2 com salt aleatório."""
    salt = os.urandom(16)
    hash_bytes = pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, ITERACOES)
    return f"{salt.hex()}:{hash_bytes.hex()}"

def main() -> None:
    """Função principal."""
    parser = argparse.ArgumentParser(description="Gerador de hash seguro para senhas")
    parser.add_argument("-o", "--saida", default="senhas_hash.txt", help="Arquivo de saída dos hashes")
    args = parser.parse_args()

    print("--- Gerador de Hash Seguro ---")
    try:
        senha = getpass.getpass("Digite uma senha forte: ")
        if not validar_senha(senha):
            print("[-] Senha fraca. Use ao menos 8 caracteres com maiúsculas, minúsculas, números e símbolos.")
            sys.exit(1)

        confirmacao = getpass.getpass("Confirme a senha: ")
        if senha != confirmacao:
            print("[-] As senhas informadas não conferem.")
            sys.exit(1)

        registro = gerar_hash(senha)
        with open(args.saida, "a", encoding="utf-8") as arquivo:
            arquivo.write(registro + "\n")

        print(f"[+] Hash armazenado com sucesso em: {args.saida}")
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
