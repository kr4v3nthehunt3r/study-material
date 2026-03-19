#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Copia arquivos PDF de um diretório para outro, permitindo escolher uma
    estratégia para lidar com arquivos duplicados.

Melhorias aplicadas:
    - Padronização do código;
    - Melhor organização da lógica;
    - Mensagens mais objetivas;
    - Nomes mais claros.
"""

import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


def copiar_arquivos_pdf(origem: str, destino: str, estrategia_duplicados: str = "renomear") -> None:
    """Copia PDFs do diretório de origem para o destino."""
    origem_path = Path(origem)
    destino_path = Path(destino)

    if not origem_path.exists():
        raise FileNotFoundError(f"Diretório de origem não encontrado: {origem}")
    if not origem_path.is_dir():
        raise ValueError(f"A origem '{origem}' não é um diretório válido.")

    destino_path.mkdir(parents=True, exist_ok=True)

    print(f"[*] Origem: {origem_path.resolve()}")
    print(f"[*] Destino: {destino_path.resolve()}")
    print(f"[*] Estratégia para duplicados: {estrategia_duplicados}")
    print("-" * 60)

    copiados = 0
    renomeados = 0
    pulados = 0

    for raiz, _, arquivos in os.walk(origem_path):
        for nome_arquivo in arquivos:
            if not nome_arquivo.lower().endswith(".pdf"):
                continue

            caminho_origem = Path(raiz) / nome_arquivo
            caminho_destino = destino_path / nome_arquivo

            if caminho_destino.exists():
                if estrategia_duplicados == "sobrescrever":
                    shutil.copy2(caminho_origem, caminho_destino)
                    print(f"[!] Sobrescrito: {nome_arquivo}")
                    copiados += 1
                elif estrategia_duplicados == "renomear":
                    timestamp = datetime.now().strftime("_%Y%m%d%H%M%S")
                    novo_nome = f"{caminho_destino.stem}{timestamp}{caminho_destino.suffix}"
                    caminho_destino_final = destino_path / novo_nome
                    shutil.copy2(caminho_origem, caminho_destino_final)
                    print(f"[!] Renomeado e copiado: {nome_arquivo} -> {novo_nome}")
                    renomeados += 1
                elif estrategia_duplicados == "pular":
                    print(f"[-] Arquivo já existe. Pulado: {nome_arquivo}")
                    pulados += 1
                else:
                    raise ValueError(f"Estratégia inválida: {estrategia_duplicados}")
            else:
                shutil.copy2(caminho_origem, caminho_destino)
                print(f"[+] Copiado: {nome_arquivo}")
                copiados += 1

    print("-" * 60)
    print("[*] Resumo da cópia")
    print(f"    - Copiados:   {copiados}")
    print(f"    - Renomeados: {renomeados}")
    print(f"    - Pulados:    {pulados}")


def main() -> None:
    """Ponto de entrada do script."""
    parser = argparse.ArgumentParser(description="Copiador de arquivos PDF")
    parser.add_argument("origem", help="Diretório de origem")
    parser.add_argument("destino", help="Diretório de destino")
    parser.add_argument(
        "-s",
        "--estrategia",
        choices=["sobrescrever", "renomear", "pular"],
        default="renomear",
        help="Estratégia para arquivos duplicados",
    )
    args = parser.parse_args()

    try:
        copiar_arquivos_pdf(args.origem, args.destino, args.estrategia)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[-] Erro: {erro}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
