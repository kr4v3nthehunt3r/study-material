#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Valida a força de senhas e gera hashes seguros usando PBKDF2-HMAC com SHA-256.

Melhorias aplicadas:
    - Interface mais clara;
    - Validação centralizada da senha;
    - Saída padronizada;
    - Código documentado em PT-BR.
"""

import argparse
import getpass
import os
import re
import sys
import time
from hashlib import pbkdf2_hmac


REGEX_SENHA_FORTE = re.compile(
    r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)


def validar_senha(senha: str) -> bool:
    """Retorna True se a senha atender aos critérios mínimos de segurança."""
    return bool(REGEX_SENHA_FORTE.fullmatch(senha))


def gerar_hash(senha: str, iteracoes: int = 100_000) -> str:
    """Gera um hash PBKDF2-HMAC-SHA256 com salt aleatório."""
    salt = os.urandom(16)
    hash_senha = pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, iteracoes)
    return f"{salt.hex()}:{hash_senha.hex()}"


def cadastrar_senhas(arquivo_saida: str) -> None:
    """Solicita senhas ao usuário, valida e salva os hashes no arquivo de saída."""
    print(f"[*] Os hashes serão armazenados em: {arquivo_saida}")
    print("[*] Digite 'sair' para encerrar.")
    print("-" * 60)

    while True:
        try:
            senha = getpass.getpass("Digite uma senha forte: ")
            if senha.lower() == "sair":
                print("[*] Encerrando cadastro.")
                break

            if not validar_senha(senha):
                print("[!] Senha fraca. Critérios mínimos:")
                print("    - 8 caracteres ou mais")
                print("    - Letra maiúscula e minúscula")
                print("    - Pelo menos um número")
                print("    - Pelo menos um símbolo: @$!%*?&")
                continue

            confirmacao = getpass.getpass("Confirme a senha: ")
            if senha != confirmacao:
                print("[!] As senhas não coincidem.")
                continue

            with open(arquivo_saida, "a", encoding="utf-8") as arquivo:
                arquivo.write(gerar_hash(senha) + "\n")

            print("[+] Hash gerado e armazenado com sucesso.")
            time.sleep(0.3)

        except KeyboardInterrupt:
            print("\n[!] Operação cancelada pelo usuário.")
            break
        except Exception as erro:
            print(f"[!] Erro inesperado: {erro}")
            break


def main() -> None:
    """Ponto de entrada principal."""
    parser = argparse.ArgumentParser(description="Validador de senha e gerador de hash")
    parser.add_argument(
        "-o",
        "--saida",
        default="senhas_hash.txt",
        help="Arquivo de saída para os hashes gerados",
    )
    args = parser.parse_args()

    print("--- Gerador de Hash de Senhas ---")
    cadastrar_senhas(args.saida)


if __name__ == "__main__":
    main()
