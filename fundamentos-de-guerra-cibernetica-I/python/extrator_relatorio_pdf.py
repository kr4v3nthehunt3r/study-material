#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Extrai texto de um relatório PDF, tenta identificar membros e equipes
    e opcionalmente testa conectividade com um serviço de rede.

Melhorias aplicadas:
    - Separação mais clara entre extração, análise e saída;
    - Regexes organizadas;
    - Tratamento de erros mais explícito;
    - Padronização de nomes e mensagens.
"""

import argparse
import os
import re
import socket
import sys

import PyPDF2


REGEX_MEMBRO = re.compile(r"\d+\.\s*([\w\sÁ-Úá-ú]+)\s*-\s*CPF:\s*([\d.\-]+)")
EQUIPES_PADRAO = ("SOC", "Red Team", "CSIRT", "Pentest", "Infraestrutura")


def extrair_texto_pdf(caminho_pdf: str) -> str:
    """Extrai o texto de todas as páginas de um PDF textual."""
    if not os.path.isfile(caminho_pdf):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_pdf}")

    texto_total = []
    try:
        with open(caminho_pdf, "rb") as arquivo_pdf:
            leitor = PyPDF2.PdfReader(arquivo_pdf)

            for pagina in leitor.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto_total.append(texto_pagina)

        texto = "\n".join(texto_total).strip()
        if not texto:
            raise ValueError("O PDF não possui texto extraível.")

        return texto

    except Exception as erro:
        raise RuntimeError(f"Falha ao ler o PDF: {erro}") from erro


def analisar_membros_e_equipes(texto: str) -> tuple[dict[str, str], dict[str, list[str]]]:
    """Extrai CPFs por nome e tenta associar nomes a equipes conhecidas."""
    membros = {nome.strip(): cpf.strip() for nome, cpf in REGEX_MEMBRO.findall(texto)}
    equipes: dict[str, list[str]] = {}

    for equipe in EQUIPES_PADRAO:
        padrao_bloco = rf"{re.escape(equipe)}([\wÁ-Úá-ú\s().:\-]+?)(?=\n(?:{'|'.join(map(re.escape, EQUIPES_PADRAO))})|\Z)"
        encontrado = re.search(padrao_bloco, texto, re.DOTALL)

        if not encontrado:
            equipes[equipe] = []
            continue

        nomes = re.findall(r"-\s*([\wÁ-Úá-ú\s]+)", encontrado.group(1))
        equipes[equipe] = [nome.strip() for nome in nomes if nome.strip()]

    return membros, equipes


def testar_servico(host: str, porta: int, timeout: float = 2.0) -> bool:
    """Retorna True se conseguir estabelecer conexão com o host e porta informados."""
    try:
        with socket.create_connection((host, porta), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main() -> None:
    """Executa o fluxo principal de análise."""
    parser = argparse.ArgumentParser(description="Extrator de dados de auditoria em PDF")
    parser.add_argument("pdf", help="Caminho do relatório PDF")
    parser.add_argument("-o", "--saida", help="Arquivo TXT para salvar o texto extraído")
    parser.add_argument("--host-teste", default="127.0.0.1", help="Host para teste de serviço")
    parser.add_argument("--porta-teste", type=int, default=4444, help="Porta para teste de serviço")
    args = parser.parse_args()

    try:
        print(f"[*] Processando relatório: {args.pdf}")
        texto = extrair_texto_pdf(args.pdf)

        if args.saida:
            with open(args.saida, "w", encoding="utf-8") as arquivo_saida:
                arquivo_saida.write(texto)
            print(f"[+] Texto exportado para: {args.saida}")

        membros, equipes = analisar_membros_e_equipes(texto)

        print("\n" + "=" * 60)
        print("[*] ESTRUTURA IDENTIFICADA NO RELATÓRIO")
        print("=" * 60)

        total_identificado = 0
        for equipe, lista_membros in equipes.items():
            print(f"\n[Equipe: {equipe}]")
            if not lista_membros:
                print("  - Nenhum membro listado.")
                continue

            for membro in lista_membros:
                cpf = membros.get(membro, "Não localizado")
                print(f"  - {membro} (CPF: {cpf})")
                total_identificado += 1

        print("\n" + "=" * 60)
        print(f"[*] Total de membros identificados: {total_identificado}")

        print(f"[*] Testando conectividade em {args.host_teste}:{args.porta_teste}...")
        ativo = testar_servico(args.host_teste, args.porta_teste)
        print(f"[+] Serviço {'ATIVO' if ativo else 'INATIVO ou INACESSÍVEL'}")
        print("=" * 60)

    except FileNotFoundError as erro:
        print(f"[-] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except (ValueError, RuntimeError) as erro:
        print(f"[-] Erro de processamento: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
