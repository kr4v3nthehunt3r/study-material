#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Bot cliente para partidas de Jokenpô via TCP. O programa lê as jogadas do
    servidor, calcula a resposta vencedora e envia automaticamente a jogada.

Melhorias aplicadas:
    - Funções renomeadas;
    - Tratamento de mensagens mais claro;
    - Comentários em PT-BR;
    - Padronização geral do código.
"""

import argparse
import re
import socket
import sys


REGRAS_VITORIA = {
    "PEDRA": "PAPEL",
    "PAPEL": "TESOURA",
    "TESOURA": "PEDRA",
}
REGEX_JOGADAS = re.compile(r"\b(PEDRA|PAPEL|TESOURA)\b", re.IGNORECASE)


def calcular_resposta_vencedora(jogada_oponente: str) -> str | None:
    """Retorna a jogada vencedora para a jogada recebida."""
    return REGRAS_VITORIA.get(jogada_oponente.upper())


def jogar(host: str, porta: int, timeout: float) -> None:
    """Conecta ao servidor e executa o bot de Jokenpô."""
    print(f"[*] Conectando ao servidor em {host}:{porta}...")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.settimeout(timeout)
            cliente.connect((host, porta))
            print("[+] Conexão estabelecida.")

            try:
                introducao = cliente.recv(4096).decode("utf-8", errors="ignore").strip()
                if introducao:
                    print(f"[SERVIDOR] {introducao}")
            except socket.timeout:
                print("[!] Timeout ao aguardar mensagem inicial.")

            cliente.sendall(b"iniciar\n")
            print("[*] Comando 'iniciar' enviado.")

            while True:
                try:
                    dados = cliente.recv(4096).decode("utf-8", errors="ignore")
                    if not dados:
                        print("[*] Conexão encerrada pelo servidor.")
                        break

                    print(f"\n[SERVIDOR] {dados.strip()}")
                    jogadas = REGEX_JOGADAS.findall(dados)

                    if jogadas:
                        respostas = [
                            calcular_resposta_vencedora(jogada)
                            for jogada in jogadas
                            if calcular_resposta_vencedora(jogada)
                        ]

                        if respostas:
                            resposta = "-".join(respostas) + "\n"
                            print(f"[BOT] Respondendo com: {resposta.strip()}")
                            cliente.sendall(resposta.encode("utf-8"))
                        continue

                    if any(palavra in dados.lower() for palavra in ("venceu", "perdeu", "flag")):
                        if "flag" in dados.lower():
                            print(f"[!] Mensagem especial recebida: {dados.strip()}")
                        print("[*] Partida finalizada.")
                        break

                except socket.timeout:
                    print("[-] Timeout aguardando jogada do servidor.")
                    break

    except ConnectionRefusedError:
        print(f"[-] Conexão recusada em {host}:{porta}.")
    except Exception as erro:
        print(f"[-] Erro inesperado: {erro}")


def main() -> None:
    """Ponto de entrada do bot."""
    parser = argparse.ArgumentParser(description="Bot de Jokenpô via TCP")
    parser.add_argument("host", nargs="?", default="127.0.0.1", help="Endereço do servidor")
    parser.add_argument("porta", nargs="?", type=int, default=55455, help="Porta do servidor")
    parser.add_argument("-t", "--timeout", type=float, default=5.0, help="Timeout do socket")
    args = parser.parse_args()

    try:
        jogar(args.host, args.porta, args.timeout)
    except KeyboardInterrupt:
        print("\n[!] Bot interrompido pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
