#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Demonstra comunicação entre processos via socket TCP, validação de e-mail com
    expressões regulares e execução controlada de comandos do sistema.

Melhorias aplicadas:
    - Validação mais clara de e-mails;
    - Execução de comandos com lista de argumentos;
    - Encerramento seguro do servidor por evento;
    - Mensagens e parâmetros mais consistentes;
    - Código padronizado e comentado em PT-BR.
"""

import argparse
import re
import shlex
import socket
import subprocess
import sys
import time
from threading import Event, Thread


EVENTO_PARADA = Event()
REGEX_EMAIL = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def validar_email(email: str) -> bool:
    """Retorna True se o e-mail estiver em um formato sintaticamente válido."""
    return bool(REGEX_EMAIL.fullmatch(email))


def executar_comando(comando: str, tempo_limite: int = 10) -> None:
    """
    Executa um comando local com shell desabilitado.

    Observação:
        O uso de shlex.split permite separar o comando em argumentos sem depender
        de shell=True, reduzindo risco de injeção em cenários simples.
    """
    print(f"[*] Executando comando: {comando}")
    try:
        resultado = subprocess.run(
            shlex.split(comando),
            capture_output=True,
            text=True,
            timeout=tempo_limite,
            check=False,
        )

        if resultado.stdout.strip():
            print(f"[Saída]\n{resultado.stdout.strip()}")
        if resultado.stderr.strip():
            print(f"[Erro]\n{resultado.stderr.strip()}")

    except subprocess.TimeoutExpired:
        print(f"[-] O comando excedeu o tempo limite de {tempo_limite} segundos.")
    except FileNotFoundError:
        print("[-] Comando não encontrado no sistema.")
    except Exception as erro:
        print(f"[-] Falha ao executar o comando: {erro}")


def servidor_tcp(host: str, porta: int) -> None:
    """Inicia um servidor TCP simples para testes locais."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind((host, porta))
            servidor.listen(5)
            servidor.settimeout(1.0)

            print(f"[SERVIDOR] Escutando em {host}:{porta}")

            while not EVENTO_PARADA.is_set():
                try:
                    conexao, endereco = servidor.accept()
                    with conexao:
                        print(f"[SERVIDOR] Conexão recebida de {endereco[0]}:{endereco[1]}")
                        dados = conexao.recv(1024).decode("utf-8", errors="ignore").strip()

                        if dados:
                            print(f"[SERVIDOR] Mensagem recebida: {dados}")
                            conexao.sendall(b"OK - Mensagem recebida\n")

                except socket.timeout:
                    continue
                except Exception as erro:
                    if not EVENTO_PARADA.is_set():
                        print(f"[SERVIDOR] Erro ao atender cliente: {erro}")

            print("[SERVIDOR] Encerrando servidor...")

    except Exception as erro:
        print(f"[SERVIDOR] Falha fatal: {erro}")


def cliente_tcp(host: str, porta: int, mensagem: str) -> None:
    """Conecta ao servidor TCP e envia uma mensagem de teste."""
    print(f"[CLIENTE] Conectando a {host}:{porta}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.settimeout(5.0)
            cliente.connect((host, porta))
            cliente.sendall((mensagem + "\n").encode("utf-8"))

            resposta = cliente.recv(1024).decode("utf-8", errors="ignore").strip()
            print(f"[CLIENTE] Resposta: {resposta}")

    except socket.timeout:
        print("[CLIENTE] Tempo limite excedido.")
    except ConnectionRefusedError:
        print("[CLIENTE] Conexão recusada pelo servidor.")
    except Exception as erro:
        print(f"[CLIENTE] Erro inesperado: {erro}")


def main() -> None:
    """Executa o fluxo principal da demonstração."""
    parser = argparse.ArgumentParser(description="Demonstração de socket, regex e subprocess")
    parser.add_argument("-p", "--porta", type=int, default=9999, help="Porta do teste TCP")
    parser.add_argument("--sem-comando", action="store_true", help="Pula a etapa de execução de comando")
    parser.add_argument(
        "--mensagem",
        default="Teste de conectividade Python Socket",
        help="Mensagem enviada pelo cliente ao servidor",
    )
    args = parser.parse_args()

    print("\n--- Etapa 1: Validação de e-mails ---")
    for email in ["valido@empresa.com", "invalido@com", "user.name@sub.dominio.org"]:
        status = "VÁLIDO" if validar_email(email) else "INVÁLIDO"
        print(f"  - {email}: {status}")

    if not args.sem_comando:
        print("\n--- Etapa 2: Execução de comando local ---")
        comando = "hostname" if sys.platform == "win32" else "whoami"
        executar_comando(comando)
        time.sleep(0.8)

    print("\n--- Etapa 3: Comunicação socket ---")
    thread_servidor = Thread(target=servidor_tcp, args=("127.0.0.1", args.porta), daemon=True)
    thread_servidor.start()

    time.sleep(1.0)
    cliente_tcp("127.0.0.1", args.porta, args.mensagem)

    print("\n[*] Finalizando demonstração...")
    EVENTO_PARADA.set()
    thread_servidor.join(timeout=2.0)
    print("[+] Concluído com sucesso.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        EVENTO_PARADA.set()
        print("\n[!] Execução interrompida pelo usuário.")
        sys.exit(0)
