#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: buscar_texto_zip.py
Descrição do módulo:
    Pesquisa um termo em arquivos texto dentro de um ZIP não criptografado, para fins defensivos e de inspeção local autorizada.

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

# Importações utilizadas por este módulo.

EXTENSOES_TEXTO = {".txt", ".log", ".csv", ".md", ".json", ".xml"}

def buscar_termo_no_zip(caminho_zip: Path, termo: str) -> list[tuple[str, int, str]]:
    """Extrai temporariamente o ZIP e procura um termo em arquivos texto."""
    if not caminho_zip.exists():
        raise FileNotFoundError(f"Arquivo ZIP não encontrado: {caminho_zip}")

    pasta_temp = Path(tempfile.mkdtemp(prefix="zip_busca_"))
    ocorrencias: list[tuple[str, int, str]] = []

    try:
        with ZipFile(caminho_zip, "r") as arquivo_zip:
            if any(item.flag_bits & 0x1 for item in arquivo_zip.infolist()):
                raise ValueError("O ZIP possui conteúdo criptografado e não será extraído por este script.")
            arquivo_zip.extractall(pasta_temp)

        for arquivo in pasta_temp.rglob("*"):
            if not arquivo.is_file() or arquivo.suffix.lower() not in EXTENSOES_TEXTO:
                continue

            with arquivo.open("r", encoding="utf-8", errors="ignore") as conteudo:
                for numero_linha, linha in enumerate(conteudo, start=1):
                    if termo.lower() in linha.lower():
                        trecho = linha.strip()
                        ocorrencias.append((str(arquivo.relative_to(pasta_temp)), numero_linha, trecho))
    finally:
        shutil.rmtree(pasta_temp, ignore_errors=True)

    return ocorrencias

def main() -> None:
    """Função principal."""
    parser = argparse.ArgumentParser(description="Busca segura de texto dentro de ZIP")
    parser.add_argument("zip", help="Arquivo ZIP a ser analisado")
    parser.add_argument("termo", help="Termo de busca")
    args = parser.parse_args()

    try:
        ocorrencias = buscar_termo_no_zip(Path(args.zip), args.termo)
        print("=" * 60)
        print(f"[*] Ocorrências encontradas: {len(ocorrencias)}")
        for arquivo, linha, trecho in ocorrencias:
            print(f"    - {arquivo} | linha {linha}: {trecho}")
        print("=" * 60)
    except (FileNotFoundError, ValueError) as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except BadZipFile as erro:
        print(f"[-] ZIP inválido ou corrompido: {erro}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
