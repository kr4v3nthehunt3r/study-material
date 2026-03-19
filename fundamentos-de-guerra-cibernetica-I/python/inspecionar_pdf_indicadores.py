#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: inspecionar_pdf_indicadores.py
Descrição do módulo:
    Faz inspeção defensiva de um PDF e resume e-mails, nomes próprios e endereços IP:porta encontrados, sempre com mascaramento na saída.

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

PADRAO_EMAIL = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}\b')
PADRAO_NOME = re.compile(r'\b[A-ZÀ-Ÿ][a-zà-ÿ]+(?:\s[A-ZÀ-Ÿ][a-zà-ÿ]+){1,}\b')
PADRAO_SOCKET = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}\b')

def mascarar_nome(nome: str) -> str:
    """Mascara um nome mantendo apenas o início de cada palavra."""
    partes = nome.split()
    return " ".join(parte[0] + "***" for parte in partes)

def mascarar_email(email: str) -> str:
    """Mascara parcialmente um e-mail."""
    usuario, dominio = email.split("@", 1)
    return f"{usuario[:2]}***@{dominio}"

def mascarar_socket(socket: str) -> str:
    """Mascara parcialmente o IP em um socket."""
    ip, porta = socket.split(":", 1)
    partes = ip.split(".")
    if len(partes) == 4:
        return f"{partes[0]}.{partes[1]}.***.***:{porta}"
    return socket

def ler_pdf(caminho_pdf: Path) -> str:
    """Lê e concatena o texto das páginas de um PDF."""
    if not caminho_pdf.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_pdf}")

    partes_texto: list[str] = []
    with caminho_pdf.open("rb") as arquivo_pdf:
        leitor = PyPDF2.PdfReader(arquivo_pdf)
        for pagina in leitor.pages:
            texto = pagina.extract_text() or ""
            if texto.strip():
                partes_texto.append(texto)

    texto_final = "\n".join(partes_texto).strip()
    if not texto_final:
        raise ValueError("O PDF não contém texto extraível.")
    return texto_final

def main() -> None:
    """Função principal."""
    parser = argparse.ArgumentParser(description="Inspeção defensiva de indicadores em PDF")
    parser.add_argument("pdf", help="Arquivo PDF a ser analisado")
    args = parser.parse_args()

    try:
        texto = ler_pdf(Path(args.pdf))
        emails = sorted(set(PADRAO_EMAIL.findall(texto)))
        nomes = sorted(set(PADRAO_NOME.findall(texto)))
        sockets = sorted(set(PADRAO_SOCKET.findall(texto)))

        print("=" * 60)
        print("[*] INSPEÇÃO DEFENSIVA DE INDICADORES")
        print("=" * 60)
        print(f"[*] E-mails encontrados: {len(emails)}")
        for email in emails:
            print(f"    - {mascarar_email(email)}")
        print(f"[*] Nomes encontrados:  {len(nomes)}")
        for nome in nomes:
            print(f"    - {mascarar_nome(nome)}")
        print(f"[*] Sockets encontrados:{len(sockets)}")
        for socket in sockets:
            print(f"    - {mascarar_socket(socket)}")
        print("=" * 60)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[-] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
