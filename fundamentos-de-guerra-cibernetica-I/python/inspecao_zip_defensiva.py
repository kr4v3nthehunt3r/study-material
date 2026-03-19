#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Realiza uma inspeção defensiva de arquivos ZIP, listando conteúdo, tamanho,
    possíveis indicadores de criptografia e procurando padrões textuais de forma
    segura, sem tentativa de quebra de senha.

Mudança importante:
    - A versão anterior dependia de ferramentas externas para ataque por wordlist.
    - Esta versão foi convertida para uso defensivo e seguro.
"""

import argparse
import os
import re
import sys
import zipfile
from pathlib import Path


def listar_conteudo_zip(caminho_zip: Path) -> list[zipfile.ZipInfo]:
    """Retorna os metadados das entradas do arquivo ZIP."""
    with zipfile.ZipFile(caminho_zip, "r") as arquivo_zip:
        return arquivo_zip.infolist()


def verificar_criptografia(info_zip: zipfile.ZipInfo) -> bool:
    """Retorna True se a entrada aparentar estar criptografada."""
    return bool(info_zip.flag_bits & 0x1)


def buscar_padrao_em_arquivos_texto(caminho_zip: Path, padrao_regex: str) -> list[tuple[str, str]]:
    """
    Procura um padrão textual em arquivos não criptografados do ZIP.

    Observação:
        Apenas conteúdo legível é analisado. Arquivos criptografados são ignorados.
    """
    regex = re.compile(padrao_regex)
    resultados: list[tuple[str, str]] = []

    with zipfile.ZipFile(caminho_zip, "r") as arquivo_zip:
        for info in arquivo_zip.infolist():
            if info.is_dir() or verificar_criptografia(info):
                continue

            try:
                with arquivo_zip.open(info, "r") as entrada:
                    conteudo = entrada.read().decode("utf-8", errors="ignore")
                    encontrado = regex.search(conteudo)
                    if encontrado:
                        resultados.append((info.filename, encontrado.group(0)))
            except Exception:
                continue

    return resultados


def main() -> None:
    """Ponto de entrada da inspeção defensiva."""
    parser = argparse.ArgumentParser(description="Inspeção defensiva de arquivo ZIP")
    parser.add_argument("zip", help="Caminho do arquivo ZIP")
    parser.add_argument(
        "--padrao",
        default=r"CIGE\{.*?\}",
        help="Expressão regular a ser buscada em arquivos não criptografados",
    )
    args = parser.parse_args()

    caminho_zip = Path(args.zip)
    if not caminho_zip.is_file():
        print(f"[-] Arquivo ZIP não encontrado: {caminho_zip}")
        sys.exit(1)

    try:
        entradas = listar_conteudo_zip(caminho_zip)

        print(f"[*] Arquivo analisado: {caminho_zip.resolve()}")
        print(f"[*] Total de entradas: {len(entradas)}")
        print("-" * 60)

        for entrada in entradas:
            status = "CRIPTOGRAFADO" if verificar_criptografia(entrada) else "NÃO CRIPTOGRAFADO"
            print(f" - {entrada.filename} | {entrada.file_size} bytes | {status}")

        print("-" * 60)
        resultados = buscar_padrao_em_arquivos_texto(caminho_zip, args.padrao)

        if resultados:
            print("[+] Padrões encontrados:")
            for arquivo, trecho in resultados:
                print(f"    - {arquivo}: {trecho}")
        else:
            print("[*] Nenhum padrão textual encontrado nos arquivos legíveis do ZIP.")

    except zipfile.BadZipFile:
        print("[-] O arquivo informado não é um ZIP válido.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Operação cancelada.")
        sys.exit(0)
    except Exception as erro:
        print(f"[-] Erro inesperado: {erro}")
        sys.exit(1)


if __name__ == "__main__":
    main()
