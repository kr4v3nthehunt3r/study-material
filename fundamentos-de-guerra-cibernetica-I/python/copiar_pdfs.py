#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: copiar_pdfs.py
Descrição do módulo:
    Copia arquivos PDF de um diretório para outro com tratamento de duplicidade.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

def resolver_destino(caminho_destino: Path, estrategia: str) -> Path | None:
    """Define o destino final do arquivo conforme a estratégia escolhida."""
    if not caminho_destino.exists():
        return caminho_destino

    if estrategia == "sobrescrever":
        return caminho_destino

    if estrategia == "pular":
        return None

    timestamp = datetime.now().strftime("_%Y%m%d_%H%M%S")
    return caminho_destino.with_name(f"{caminho_destino.stem}{timestamp}{caminho_destino.suffix}")

def copiar_pdfs(origem: Path, destino: Path, estrategia: str) -> tuple[int, int, int]:
    """Copia todos os PDFs encontrados em origem para o diretório de destino."""
    if not origem.exists():
        raise FileNotFoundError(f"Diretório de origem não encontrado: {origem}")
    if not origem.is_dir():
        raise ValueError(f"A origem '{origem}' não é um diretório válido.")

    destino.mkdir(parents=True, exist_ok=True)

    copiados = 0
    renomeados = 0
    pulados = 0

    for arquivo in origem.rglob("*.pdf"):
        alvo_padrao = destino / arquivo.name
        alvo_final = resolver_destino(alvo_padrao, estrategia)

        if alvo_final is None:
            print(f"[-] Arquivo ignorado: {arquivo.name}")
            pulados += 1
            continue

        if alvo_final != alvo_padrao and alvo_padrao.exists():
            renomeados += 1
            print(f"[!] Arquivo duplicado renomeado: {arquivo.name} -> {alvo_final.name}")
        else:
            print(f"[+] Copiando: {arquivo.name}")

        shutil.copy2(arquivo, alvo_final)
        copiados += 1

    return copiados, renomeados, pulados

def main() -> None:
    """Função principal da aplicação."""
    parser = argparse.ArgumentParser(description="Copiador de arquivos PDF")
    parser.add_argument("origem", help="Diretório de origem")
    parser.add_argument("destino", help="Diretório de destino")
    parser.add_argument(
        "-e",
        "--estrategia",
        choices=["renomear", "sobrescrever", "pular"],
        default="renomear",
        help="Estratégia para arquivos duplicados",
    )
    args = parser.parse_args()

    try:
        copiados, renomeados, pulados = copiar_pdfs(Path(args.origem), Path(args.destino), args.estrategia)
        print("-" * 50)
        print(f"[*] Arquivos copiados:   {copiados}")
        print(f"[*] Arquivos renomeados: {renomeados}")
        print(f"[*] Arquivos pulados:    {pulados}")
        print("-" * 50)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[-] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada pelo usuário.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
