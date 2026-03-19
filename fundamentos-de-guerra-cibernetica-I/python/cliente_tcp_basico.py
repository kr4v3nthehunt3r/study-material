#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Cliente TCP simples para teste de comunicação com um servidor.
"""

import argparse
import socket
import sys


def iniciar_cliente(host: str, porta: int, mensagem: str) -> None:
    """Conecta a um servidor TCP, envia uma mensagem e exibe a resposta."""
    print(f"[*] Conectando a {host}:{porta}...")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.settimeout(10.0)
            cliente.connect((host, porta))
            print("[+] Conexão estabelecida com sucesso.")

            cliente.sendall(mensagem.encode("utf-8"))
            print(f"[>] Enviado: {mensagem}")

            dados = cliente.recv(1024)
            if dados:
                print(f"[<] Recebido: {dados.decode('utf-8', errors='ignore').strip()}")
            else:
                print("[!] O servidor encerrou a conexão sem responder.")

    except socket.timeout:
        print("[-] Timeout da conexão.")
    except ConnectionRefusedError:
        print(f"[-] Conexão recusada por {host}:{porta}.")
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operação cancelada pelo usuário.")
    except Exception as erro:
        print(f"[-] Erro inesperado: {erro}")
        sys.exit(1)


def main() -> None:
    """Ponto de entrada do script."""
    parser = argparse.ArgumentParser(description="Cliente TCP básico")
    parser.add_argument("--host", default="127.0.0.1", help="Endereço do servidor")
    parser.add_argument("--porta", type=int, default=8080, help="Porta do servidor")
    parser.add_argument(
        "--mensagem",
        default="Olá, servidor! Teste de comunicação.",
        help="Mensagem a ser enviada",
    )
    args = parser.parse_args()

    iniciar_cliente(args.host, args.porta, args.mensagem)


if __name__ == "__main__":
    main()
