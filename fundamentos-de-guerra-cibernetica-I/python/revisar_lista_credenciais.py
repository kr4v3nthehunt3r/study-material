#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: revisar_lista_credenciais.py
Descrição do módulo:
    Analisa um arquivo no formato e-mail:segredo de forma defensiva, sem exibir segredos em texto claro. O objetivo é validar formato, domínio e higiene básica.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import re
import sys
from pathlib import Path

# Importações utilizadas por este módulo.

PADRAO_EMAIL = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def mascarar_texto(texto: str) -> str:
    """Mascara um valor sensível para exibição segura."""
    if len(texto) <= 3:
        return "***"
    return f"{texto[:2]}***{texto[-1]}"

def classificar_segredo(segredo: str) -> str:
    """Classifica o valor informado por comprimento e diversidade de caracteres."""
    tem_maiuscula = any(c.isupper() for c in segredo)
    tem_minuscula = any(c.islower() for c in segredo)
    tem_digito = any(c.isdigit() for c in segredo)
    tem_especial = any(not c.isalnum() for c in segredo)

    pontuacao = sum([tem_maiuscula, tem_minuscula, tem_digito, tem_especial])
    if len(segredo) >= 12 and pontuacao >= 3:
        return "forte"
    if len(segredo) >= 8 and pontuacao >= 2:
        return "médio"
    return "fraco"

def analisar_arquivo(caminho: Path, dominio: str) -> dict[str, object]:
    """Lê o arquivo e produz um resumo defensivo da lista informada."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    total_linhas = 0
    invalidas = 0
    duplicadas = 0
    contas_dominio = 0
    segredos_fracos: list[tuple[str, str]] = []
    vistos: set[str] = set()

    with caminho.open("r", encoding="utf-8", errors="ignore") as arquivo:
        for linha in arquivo:
            conteudo = linha.strip()
            if not conteudo:
                continue

            total_linhas += 1
            partes = conteudo.split(":", 1)
            if len(partes) != 2:
                invalidas += 1
                continue

            email, segredo = partes[0].strip(), partes[1].strip()
            if not PADRAO_EMAIL.fullmatch(email):
                invalidas += 1
                continue

            email_normalizado = email.lower()
            if email_normalizado in vistos:
                duplicadas += 1
                continue
            vistos.add(email_normalizado)

            if email_normalizado.endswith(f"@{dominio.lower()}"):
                contas_dominio += 1
                forca = classificar_segredo(segredo)
                if forca == "fraco":
                    segredos_fracos.append((email, mascarar_texto(segredo)))

    return {
        "total_linhas": total_linhas,
        "invalidas": invalidas,
        "duplicadas": duplicadas,
        "contas_dominio": contas_dominio,
        "segredos_fracos": segredos_fracos,
    }

def main() -> None:
    """Ponto de entrada do script."""
    parser = argparse.ArgumentParser(description="Revisor defensivo de listas de credenciais")
    parser.add_argument("arquivo", help="Arquivo no formato e-mail:segredo")
    parser.add_argument("-d", "--dominio", default="uol.com.br", help="Domínio a ser avaliado")
    args = parser.parse_args()

    try:
        resumo = analisar_arquivo(Path(args.arquivo), args.dominio)
        print("-" * 55)
        print(f"[*] Linhas válidas/avaliadas: {resumo['total_linhas']}")
        print(f"[*] Linhas inválidas:         {resumo['invalidas']}")
        print(f"[*] Duplicadas:              {resumo['duplicadas']}")
        print(f"[*] Contas em @{args.dominio}:     {resumo['contas_dominio']}")
        print(f"[*] Segredos fracos:         {len(resumo['segredos_fracos'])}")
        print("-" * 55)

        if resumo["segredos_fracos"]:
            print("[!] Contas com higiene fraca detectadas:")
            for email, mascara in resumo["segredos_fracos"]:
                print(f"    - {email} | valor mascarado: {mascara}")
    except FileNotFoundError as erro:
        print(f"[-] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
