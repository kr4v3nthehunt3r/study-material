#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Servidor TCP simples com reutilização de porta, timeout e encerramento controlado.
"""

import argparse
import socket
import sys


def iniciar_servidor(host: str, porta: int) -> None:
    """Inicia um servidor TCP simples e responde aos clientes conectados."""
    print(f"[*] Configurando servidor em {host}:{porta}...")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((host, porta))
            servidor.listen(5)
            servidor.settimeout(1.0)

            print("[+] Servidor online e aguardando conexões...")

            while True:
                try:
                    conexao, endereco = servidor.accept()
                except socket.timeout:
                    continue

                with conexao:
                    print(f"[+] Cliente conectado: {endereco[0]}:{endereco[1]}")
                    conexao.settimeout(5.0)

                    try:
                        dados = conexao.recv(1024)
                        if dados:
                            mensagem = dados.decode("utf-8", errors="ignore").strip()
                            print(f"[<] Recebido: {mensagem}")

                            resposta = "Mensagem processada pelo servidor.\n"
                            conexao.sendall(resposta.encode("utf-8"))
                            print("[>] Resposta enviada.")

                    except socket.timeout:
                        print("[-] Timeout de recebimento para o cliente atual.")

                    print(f"[*] Conexão finalizada com {endereco[0]}:{endereco[1]}")

    except PermissionError:
        print("[-] Permissão negada para abrir a porta solicitada.")
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Servidor encerrado pelo usuário.")
    except Exception as erro:
        print(f"[-] Erro fatal do servidor: {erro}")
        sys.exit(1)


def main() -> None:
    """Ponto de entrada do script."""
    parser = argparse.ArgumentParser(description="Servidor TCP básico")
    parser.add_argument("--host", default="0.0.0.0", help="Endereço de escuta")
    parser.add_argument("--porta", type=int, default=8080, help="Porta de escuta")
    args = parser.parse_args()

    iniciar_servidor(args.host, args.porta)


if __name__ == "__main__":
    main()
