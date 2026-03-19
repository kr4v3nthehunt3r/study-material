#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Analisa PDFs em busca de padrões de exposição de dados, como e-mails e
    referências a sockets.

Melhorias aplicadas:
    - Regex de e-mail organizada;
    - Mascaração de dados na saída;
    - Estrutura mais clara.
"""

import argparse
import os
import re
import sys

import PyPDF2


REGEX_EMAIL = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")
REGEX_SOCKET = re.compile(
    r"([A-ZÁ-Ú][a-zá-ú]+(?:\s[A-ZÁ-Ú][a-zá-ú]+)*)[^.\n]*?\bsocket\b\s+"
    r"(\d{1,3}(?:\.\d{1,3}){3}:\d+)"
)


def extrair_texto_pdf(caminho_pdf: str) -> str:
    """Extrai o texto completo de um arquivo PDF."""
    if not os.path.isfile(caminho_pdf):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_pdf}")

    texto_paginas: list[str] = []

    try:
        with open(caminho_pdf, "rb") as arquivo_pdf:
            leitor = PyPDF2.PdfReader(arquivo_pdf)

            for indice, pagina in enumerate(leitor.pages, start=1):
                texto = pagina.extract_text()
                if texto:
                    texto_paginas.append(texto)
                else:
                    print(f"[!] Aviso: página {indice} sem texto extraível.")

        texto_total = "\n".join(texto_paginas).strip()
        if not texto_total:
            raise ValueError("O PDF não contém texto extraível.")

        return texto_total

    except Exception as erro:
        raise RuntimeError(f"Erro ao processar o PDF: {erro}") from erro


def analisar_exposicao(texto: str) -> tuple[list[str], list[tuple[str, str]]]:
    """Retorna lista de e-mails únicos e referências nome/socket encontradas."""
    emails = sorted(set(REGEX_EMAIL.findall(texto)))
    sockets = REGEX_SOCKET.findall(texto)
    return emails, sockets


def mascarar_email(email: str) -> str:
    """Mascara parcialmente um e-mail para reduzir exposição na saída."""
    try:
        usuario, dominio = email.split("@", 1)
        prefixo = usuario[:2] if len(usuario) >= 2 else usuario[:1]
        return f"{prefixo}***@{dominio}"
    except ValueError:
        return email


def mascarar_nome(nome: str) -> str:
    """Mascara parcialmente um nome próprio."""
    partes = nome.split()
    if not partes:
        return nome
    return f"{partes[0]} {'*' * 5}"


def main() -> None:
    """Executa a análise principal do PDF."""
    parser = argparse.ArgumentParser(description="Analisador de exposição de dados em PDF")
    parser.add_argument("pdf", help="Caminho para o arquivo PDF")
    args = parser.parse_args()

    try:
        print(f"[*] Analisando arquivo: {args.pdf}")
        texto = extrair_texto_pdf(args.pdf)
        emails, sockets = analisar_exposicao(texto)

        print("\n" + "=" * 60)
        print("[*] RELATÓRIO DE EXPOSIÇÃO DE DADOS")
        print("=" * 60)

        print(f"[+] Total de e-mails únicos: {len(emails)}")
        for email in emails:
            print(f"    - {mascarar_email(email)}")

        print(f"\n[+] Referências nome/socket: {len(sockets)}")
        for nome, socket_ref in sockets:
            print(f"    - {mascarar_nome(nome)} -> {socket_ref}")

        print("=" * 60)
        print("[*] Análise concluída.")

    except (FileNotFoundError, ValueError, RuntimeError) as erro:
        print(f"[!] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)


if __name__ == "__main__":
    main()
