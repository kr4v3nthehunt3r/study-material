#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: auditar_pdf_exposicao.py
Descrição do módulo:
    Analisa um PDF para fins defensivos e apresenta resumo de indicadores como e-mails e IP:porta, sempre com saída mascarada.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import re
import sys
from pathlib import Path

import PyPDF2

# Importações utilizadas por este módulo.

PADRAO_EMAIL = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
PADRAO_SOCKET = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}\b')

def mascarar_email(email: str) -> str:
    """Mascara parcialmente o endereço de e-mail."""
    usuario, dominio = email.split("@", 1)
    usuario_mascarado = usuario[:2] + "***" if len(usuario) > 2 else "***"
    return f"{usuario_mascarado}@{dominio}"

def mascarar_socket(socket: str) -> str:
    """Mascara parcialmente o IP de um socket."""
    ip, porta = socket.split(":", 1)
    octetos = ip.split(".")
    if len(octetos) == 4:
        ip_mascarado = ".".join(octetos[:2] + ["***", "***"])
        return f"{ip_mascarado}:{porta}"
    return socket

def extrair_texto_pdf(caminho_pdf: Path) -> str:
    """Extrai o texto de todas as páginas de um arquivo PDF."""
    if not caminho_pdf.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_pdf}")

    texto_total: list[str] = []
    with caminho_pdf.open("rb") as arquivo_pdf:
        leitor = PyPDF2.PdfReader(arquivo_pdf)
        if not leitor.pages:
            raise ValueError("O PDF está vazio ou não contém páginas legíveis.")

        for indice, pagina in enumerate(leitor.pages, start=1):
            texto_pagina = pagina.extract_text() or ""
            if texto_pagina.strip():
                texto_total.append(texto_pagina)
            else:
                print(f"[!] Aviso: página {indice} sem texto extraível.", file=sys.stderr)

    texto_final = "\n".join(texto_total).strip()
    if not texto_final:
        raise ValueError("Nenhum texto pôde ser extraído do PDF.")
    return texto_final

def analisar_indicadores(texto: str) -> tuple[list[str], list[str]]:
    """Extrai e-mails e sockets únicos do texto."""
    emails = sorted(set(PADRAO_EMAIL.findall(texto)))
    sockets = sorted(set(PADRAO_SOCKET.findall(texto)))
    return emails, sockets

def main() -> None:
    """Função principal."""
    parser = argparse.ArgumentParser(description="Auditor defensivo de indicadores em PDF")
    parser.add_argument("pdf", help="Arquivo PDF a ser analisado")
    args = parser.parse_args()

    try:
        texto = extrair_texto_pdf(Path(args.pdf))
        emails, sockets = analisar_indicadores(texto)

        print("=" * 60)
        print("[*] RELATÓRIO DEFENSIVO DE INDICADORES EM PDF")
        print("=" * 60)
        print(f"[*] Tamanho do texto extraído: {len(texto)} caracteres")
        print(f"[*] E-mails identificados:     {len(emails)}")
        for email in emails:
            print(f"    - {mascarar_email(email)}")
        print(f"[*] Sockets identificados:     {len(sockets)}")
        for socket in sockets:
            print(f"    - {mascarar_socket(socket)}")
        print("=" * 60)
    except (FileNotFoundError, ValueError, OSError) as erro:
        print(f"[-] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
