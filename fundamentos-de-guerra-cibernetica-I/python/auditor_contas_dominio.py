#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Analisa um arquivo no formato email:senha de forma defensiva, filtrando contas
    por domínio e avaliando apenas se a senha segue um padrão simples.

Importante:
    - O script mascara as senhas por padrão;
    - O foco é auditoria defensiva e higiene de dados;
    - Não realiza qualquer tentativa de exploração.
"""

import argparse
import os
import re
import sys


REGEX_EMAIL = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
REGEX_SENHA_SIMPLES = re.compile(r"^[A-Z].*[0-9]$")


def pertence_ao_dominio(email: str, dominio: str) -> bool:
    """Verifica se o e-mail pertence ao domínio informado."""
    return email.lower().endswith(f"@{dominio.lower()}")


def senha_em_padrao_simples(senha: str) -> bool:
    """Retorna True se a senha seguir o padrão simples definido."""
    return bool(REGEX_SENHA_SIMPLES.fullmatch(senha))


def mascarar_senha(senha: str) -> str:
    """Retorna uma versão mascarada da senha."""
    if len(senha) <= 2:
        return "*" * len(senha)
    return senha[0] + "*" * (len(senha) - 2) + senha[-1]


def processar_arquivo(caminho_arquivo: str, dominio: str) -> dict[str, str]:
    """
    Processa o arquivo e retorna contas únicas do domínio cuja senha segue o padrão simples.

    Observação:
        O uso desse filtro ajuda a localizar padrões fracos e previsíveis de credenciais.
    """
    resultados: dict[str, str] = {}

    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo '{caminho_arquivo}' não foi encontrado.")

    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as arquivo:
        for numero_linha, linha in enumerate(arquivo, 1):
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split(":", 1)
            if len(partes) != 2:
                continue

            email, senha = partes[0].strip(), partes[1].strip()
            if not REGEX_EMAIL.fullmatch(email):
                continue

            if pertence_ao_dominio(email, dominio) and senha_em_padrao_simples(senha):
                resultados.setdefault(email, senha)

    return resultados


def main() -> None:
    """Ponto de entrada do script."""
    parser = argparse.ArgumentParser(description="Auditoria defensiva de contas por domínio")
    parser.add_argument("arquivo", help="Arquivo no formato email:senha")
    parser.add_argument("--dominio", default="uol.com.br", help="Domínio alvo")
    parser.add_argument(
        "--mostrar-senhas",
        action="store_true",
        help="Exibe senhas completas na saída (não recomendado)",
    )
    args = parser.parse_args()

    try:
        dados = processar_arquivo(args.arquivo, args.dominio)

        print(
            f"[*] Total de contas únicas em '@{args.dominio}' com padrão simples de senha: "
            f"{len(dados)}"
        )

        if not dados:
            print("[*] Nenhuma conta encontrada com os critérios definidos.")
            return

        print("\nResultados:")
        for email, senha in dados.items():
            senha_saida = senha if args.mostrar_senhas else mascarar_senha(senha)
            print(f"    {email} : {senha_saida}")

    except FileNotFoundError as erro:
        print(f"[-] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação interrompida pelo usuário.", file=sys.stderr)
        sys.exit(1)
    except Exception as erro:
        print(f"[-] Erro inesperado ao processar o arquivo: {erro}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
