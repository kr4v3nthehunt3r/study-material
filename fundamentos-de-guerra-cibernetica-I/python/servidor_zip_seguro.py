#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Servidor TCP para recebimento de arquivos ZIP e extração segura em diretório local.

Melhorias aplicadas:
    - Validação contra Path Traversal;
    - Sanitização do nome recebido pela rede;
    - Mensagens padronizadas;
    - Código reorganizado e documentado em PT-BR.
"""

import argparse
import os
import socket
import sys
import zipfile
from pathlib import Path


TAMANHO_BUFFER = 4096


def esta_dentro_do_destino(caminho_base: Path, caminho_final: Path) -> bool:
    """Retorna True se o caminho final estiver contido dentro do diretório base."""
    try:
        caminho_final.resolve().relative_to(caminho_base.resolve())
        return True
    except ValueError:
        return False


def extrair_zip_seguro(caminho_zip: Path, pasta_destino: Path) -> None:
    """
    Extrai um ZIP somente se os caminhos internos permanecerem dentro da pasta de destino.
    """
    with zipfile.ZipFile(caminho_zip, "r") as arquivo_zip:
        for membro in arquivo_zip.infolist():
            destino_previsto = pasta_destino.joinpath(membro.filename).resolve()

            if not esta_dentro_do_destino(pasta_destino, destino_previsto):
                print(f"[!] Entrada insegura ignorada: {membro.filename}")
                continue

            arquivo_zip.extract(membro, pasta_destino)


def iniciar_servidor(host: str, porta: int, pasta_base: Path) -> None:
    """Inicia o servidor de recebimento de arquivos."""
    pasta_base.mkdir(parents=True, exist_ok=True)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((host, porta))
            servidor.listen(5)
            servidor.settimeout(1.0)

            print(f"[*] Servidor ativo em {host}:{porta}")
            print(f"[*] Diretório de destino: {pasta_base.resolve()}")
            print("-" * 60)

            while True:
                try:
                    conexao, endereco = servidor.accept()
                except socket.timeout:
                    continue

                with conexao:
                    print(f"[+] Conexão recebida de {endereco[0]}:{endereco[1]}")

                    nome_bruto = conexao.recv(1024).decode("utf-8", errors="ignore").strip()
                    if not nome_bruto:
                        print("[!] Nome de arquivo vazio. Conexão ignorada.")
                        continue

                    nome_arquivo = os.path.basename(nome_bruto)
                    caminho_destino = pasta_base / nome_arquivo

                    print(f"[*] Recebendo: {nome_arquivo}")

                    with open(caminho_destino, "wb") as arquivo_saida:
                        while True:
                            dados = conexao.recv(TAMANHO_BUFFER)
                            if not dados:
                                break
                            arquivo_saida.write(dados)

                    print(f"[+] Arquivo salvo em: {caminho_destino}")

                    if caminho_destino.suffix.lower() == ".zip":
                        print("[*] ZIP detectado. Iniciando extração segura...")
                        try:
                            extrair_zip_seguro(caminho_destino, pasta_base)
                            print("[+] Extração concluída com segurança.")
                        except zipfile.BadZipFile:
                            print("[-] O arquivo recebido não é um ZIP válido.")
                        except Exception as erro:
                            print(f"[-] Falha ao extrair ZIP: {erro}")

    except PermissionError:
        print(f"[-] Permissão negada para abrir a porta {porta}.")
    except KeyboardInterrupt:
        print("\n[!] Servidor encerrado pelo usuário.")
    except Exception as erro:
        print(f"[-] Erro fatal do servidor: {erro}")
        sys.exit(1)


def main() -> None:
    """Ponto de entrada da aplicação."""
    parser = argparse.ArgumentParser(description="Servidor seguro de recebimento e extração de ZIP")
    parser.add_argument("-p", "--porta", type=int, default=8888, help="Porta de escuta")
    parser.add_argument(
        "-d",
        "--diretorio",
        default="arquivos_recebidos",
        help="Diretório onde os arquivos serão salvos",
    )
    args = parser.parse_args()

    iniciar_servidor("0.0.0.0", args.porta, Path(args.diretorio))


if __name__ == "__main__":
    main()
