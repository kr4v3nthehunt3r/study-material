#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: inspecionar_zip.py
Descrição do módulo:
    Inspeciona um arquivo ZIP de forma segura, listando conteúdo, tamanho, integridade básica e sinalização de criptografia, sem qualquer rotina de quebra de senha.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import argparse
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile

def inspecionar_zip(caminho_zip: Path) -> dict[str, object]:
    """Coleta informações básicas sobre um arquivo ZIP."""
    if not caminho_zip.exists():
        raise FileNotFoundError(f"Arquivo ZIP não encontrado: {caminho_zip}")

    with ZipFile(caminho_zip, "r") as arquivo_zip:
        arquivos = arquivo_zip.infolist()
        primeiro_arquivo_corrompido = arquivo_zip.testzip()

        return {
            "total_arquivos": len(arquivos),
            "nomes": [item.filename for item in arquivos],
            "tamanho_total": sum(item.file_size for item in arquivos),
            "comprimido_total": sum(item.compress_size for item in arquivos),
            "criptografado": any(item.flag_bits & 0x1 for item in arquivos),
            "arquivo_corrompido": primeiro_arquivo_corrompido,
        }

def main() -> None:
    """Função principal."""
    parser = argparse.ArgumentParser(description="Inspeção segura de arquivos ZIP")
    parser.add_argument("zip", help="Arquivo ZIP a ser analisado")
    args = parser.parse_args()

    try:
        resumo = inspecionar_zip(Path(args.zip))
        print("=" * 55)
        print("[*] RESUMO DO ARQUIVO ZIP")
        print("=" * 55)
        print(f"[*] Total de arquivos:        {resumo['total_arquivos']}")
        print(f"[*] Tamanho descompactado:    {resumo['tamanho_total']} bytes")
        print(f"[*] Tamanho compactado:       {resumo['comprimido_total']} bytes")
        print(f"[*] Contém criptografia?:     {resumo['criptografado']}")
        print(f"[*] Primeiro item corrompido: {resumo['arquivo_corrompido']}")
        print("-" * 55)
        for nome in resumo["nomes"]:
            print(f"    - {nome}")
        print("=" * 55)
    except FileNotFoundError as erro:
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
