#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Audita defensivamente um arquivo no formato email:senha, contando registros,
    filtrando por domínio e identificando senhas que seguem um padrão fraco ou previsível.

Correção importante:
    - A lógica do relatório foi corrigida. Agora o script destaca como problema
      apenas as credenciais que correspondem ao padrão fraco definido.
"""

import argparse
import os
import re
import sys


REGEX_EMAIL = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def carregar_linhas(caminho: str) -> list[tuple[int, str]]:
    """Lê as linhas do arquivo, preservando a numeração original."""
    dados: list[tuple[int, str]] = []

    with open(caminho, "r", encoding="utf-8", errors="ignore") as arquivo:
        for numero, linha in enumerate(arquivo, start=1):
            linha_limpa = linha.strip()
            if linha_limpa:
                dados.append((numero, linha_limpa))

    return dados


def processar_credenciais(dados_brutos: list[tuple[int, str]]) -> tuple[dict[str, str], int]:
    """Valida o formato email:senha e retorna credenciais únicas e total inválido."""
    credenciais: dict[str, str] = {}
    invalidas = 0

    for _, linha in dados_brutos:
        partes = linha.split(":", 1)
        if len(partes) != 2:
            invalidas += 1
            continue

        email, senha = partes[0].strip(), partes[1].strip()
        if not REGEX_EMAIL.fullmatch(email):
            invalidas += 1
            continue

        credenciais.setdefault(email, senha)

    return credenciais, invalidas


def encontrar_padrao_fraco(
    credenciais: dict[str, str],
    dominio: str,
    regex_senha_fraca: re.Pattern[str],
) -> list[tuple[str, str]]:
    """Retorna credenciais do domínio cuja senha combina com o padrão fraco informado."""
    resultados: list[tuple[str, str]] = []

    for email, senha in credenciais.items():
        if email.lower().endswith(f"@{dominio.lower()}") and regex_senha_fraca.fullmatch(senha):
            resultados.append((email, senha))

    return resultados


def mascarar_senha(senha: str) -> str:
    """Mascara a senha para reduzir exposição no terminal."""
    if len(senha) <= 3:
        return "*" * len(senha)
    return f"{senha[:2]}***{senha[-1]}"


def main() -> None:
    """Executa a auditoria defensiva."""
    parser = argparse.ArgumentParser(description="Auditoria defensiva de credenciais")
    parser.add_argument("arquivo", help="Arquivo de entrada no formato email:senha")
    parser.add_argument("-d", "--dominio", default="uol.com.br", help="Domínio alvo")
    parser.add_argument(
        "--regex-fraca",
        default=r"^[A-Z].*\d$",
        help="Regex que representa um padrão de senha considerado fraco",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.arquivo):
        print(f"[-] O arquivo '{args.arquivo}' não existe.", file=sys.stderr)
        sys.exit(1)

    try:
        try:
            regex_fraca = re.compile(args.regex_fraca)
        except re.error as erro:
            print(f"[-] Expressão regular inválida: {erro}", file=sys.stderr)
            sys.exit(1)

        linhas = carregar_linhas(args.arquivo)
        credenciais, erros_formato = processar_credenciais(linhas)
        fragilidades = encontrar_padrao_fraco(credenciais, args.dominio, regex_fraca)

        print("-" * 55)
        print("[*] Resumo da auditoria")
        print(f"    - Linhas lidas:            {len(linhas)}")
        print(f"    - Registros inválidos:     {erros_formato}")
        print(f"    - Credenciais únicas:      {len(credenciais)}")
        print(f"    - Fragilidades em @{args.dominio}: {len(fragilidades)}")
        print("-" * 55)

        if fragilidades:
            print("[!] Credenciais que seguem o padrão fraco definido:")
            for email, senha in fragilidades:
                print(f"    - {email} | senha mascarada: {mascarar_senha(senha)}")
        else:
            print("[+] Nenhuma fragilidade detectada para o domínio informado.")

    except KeyboardInterrupt:
        print("\n[!] Operação cancelada pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
