#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: filtrar_frequencias_zip.py
Descrição do módulo:
    Extrai um ZIP com arquivos TXT e lista frequências dentro de uma faixa informada.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import shutil
import sys
import tempfile
from pathlib import Path
from zipfile import BadZipFile, ZipFile

def extrair_frequencias(caminho_zip: Path, limite_min: float, limite_max: float) -> list[float]:
    """Extrai frequências numéricas de arquivos TXT presentes em um ZIP."""
    if not caminho_zip.exists():
        raise FileNotFoundError(f"Arquivo ZIP não encontrado: {caminho_zip}")

    diretorio_temp = Path(tempfile.mkdtemp(prefix="freq_"))
    frequencias: set[float] = set()

    try:
        with ZipFile(caminho_zip, "r") as arquivo_zip:
            arquivo_zip.extractall(diretorio_temp)

        for arquivo_txt in diretorio_temp.rglob("*.txt"):
            with arquivo_txt.open("r", encoding="utf-8", errors="ignore") as arquivo:
                for linha in arquivo:
                    conteudo = linha.strip().replace("MHz", "").replace("mhz", "").replace(",", ".")
                    if not conteudo:
                        continue
                    try:
                        valor = float(conteudo)
                        if limite_min < valor < limite_max:
                            frequencias.add(valor)
                    except ValueError:
                        continue
    except BadZipFile as erro:
        raise ValueError(f"ZIP inválido ou corrompido: {erro}") from erro
    finally:
        shutil.rmtree(diretorio_temp, ignore_errors=True)

    return sorted(frequencias)

def main() -> None:
    """Função principal."""
    parser = argparse.ArgumentParser(description="Filtro de frequências em arquivos ZIP")
    parser.add_argument("zip", help="Arquivo ZIP contendo os dados")
    parser.add_argument("--min", dest="limite_min", type=float, default=95.0, help="Limite mínimo")
    parser.add_argument("--max", dest="limite_max", type=float, default=180.0, help="Limite máximo")
    args = parser.parse_args()

    try:
        frequencias = extrair_frequencias(Path(args.zip), args.limite_min, args.limite_max)
        print("=" * 55)
        print(f"[*] Frequências encontradas no intervalo: {len(frequencias)}")
        for frequencia in frequencias:
            print(f"    - {frequencia:.2f} MHz")
        print("=" * 55)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
