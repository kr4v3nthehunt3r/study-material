#!/usr/bin/env python3
"""
Autor: Kr4v3n
Arquivo: gerar_relatorio_apache.py

Descrição do módulo:
    Este módulo lê um arquivo de log Apache, processa seus registros e gera
    um relatório textual consolidado com estatísticas relevantes.

Objetivos:
    - Ler um arquivo access.log;
    - Processar os registros válidos do log;
    - Ignorar linhas inválidas e respostas HTTP 304;
    - Contabilizar hosts, métodos, User-Agents e erros 404;
    - Gerar um relatório em arquivo texto.
"""

from collections import Counter
import re
from typing import Iterable

# Expressão regular para logs Apache no formato Combined.
PADRAO_LOG = re.compile(
    r'^(?P<host>\S+) \S+ \S+ '
    r'\[(?P<data>[^\]]+)\] '
    r'"(?P<metodo>\S+) (?P<url>.*?) (?P<protocolo>[^\"]+)" '
    r'(?P<status>\d{3}) (?P<bytes>\S+) '
    r'"(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"$'
)


def processar_logs(linhas: Iterable[str]) -> tuple[Counter, Counter, Counter, int]:
    """
    Processa as linhas do log Apache e gera estatísticas resumidas.

    Parâmetros:
        linhas (Iterable[str]): Linhas do arquivo de log a serem analisadas.

    Retorno:
        tuple[Counter, Counter, Counter, int]:
            Retorna uma tupla contendo:
            - contagem de hosts;
            - contagem de User-Agents;
            - contagem de métodos HTTP;
            - total de respostas com status 404.
    """
    # Contadores usados para consolidar as estatísticas do log.
    hosts = Counter()
    user_agents = Counter()
    metodos = Counter()
    total_404 = 0

    # Percorre todas as linhas fornecidas.
    for linha in linhas:
        # Remove espaços extras e ignora linhas vazias.
        linha = linha.strip()
        if not linha:
            continue

        # Tenta interpretar a linha de acordo com o padrão Apache.
        correspondencia = PADRAO_LOG.match(linha)
        if not correspondencia:
            continue

        # Extrai os dados capturados pela expressão regular.
        dados = correspondencia.groupdict()
        status = dados["status"]

        # Ignora registros com status 304, conforme critério de análise.
        if status == "304":
            continue

        # Atualiza as estruturas de contagem.
        hosts[dados["host"]] += 1
        user_agents[dados["user_agent"]] += 1
        metodos[dados["metodo"]] += 1

        # Conta quantos eventos resultaram em erro 404.
        if status == "404":
            total_404 += 1

    return hosts, user_agents, metodos, total_404


def gerar_relatorio(caminho_entrada: str, caminho_saida: str) -> None:
    """
    Lê um arquivo de log Apache, processa os dados e salva um relatório.

    Parâmetros:
        caminho_entrada (str): Caminho do arquivo de entrada com os logs.
        caminho_saida (str): Caminho do arquivo de saída do relatório.
    """
    # Abre o arquivo de entrada com tolerância a caracteres inválidos.
    with open(caminho_entrada, "r", encoding="utf-8", errors="ignore") as arquivo:
        # Lê apenas linhas não vazias para otimizar o processamento.
        linhas = [linha for linha in arquivo if linha.strip()]

    # Processa as linhas e recebe as estatísticas consolidadas.
    hosts, user_agents, metodos, total_404 = processar_logs(linhas)

    # Abre o arquivo de saída para gravar o relatório final.
    with open(caminho_saida, "w", encoding="utf-8") as relatorio:
        relatorio.write("=== RELATÓRIO DE ANÁLISE DE LOGS ===\n\n")
        relatorio.write(f"Total de registros lidos: {len(linhas)}\n\n")

        relatorio.write("TOP 3 HOSTS:\n")
        for posicao, (host, quantidade) in enumerate(hosts.most_common(3), start=1):
            relatorio.write(f"{posicao}. {host} ({quantidade} requisições)\n")

        relatorio.write("\n" + "-" * 30 + "\n\n")
        relatorio.write("TOP 5 USER AGENTS:\n")
        for posicao, (ua, quantidade) in enumerate(user_agents.most_common(5), start=1):
            relatorio.write(f"{posicao}. {ua} ({quantidade} acessos)\n")

        relatorio.write("\nMÉTODOS HTTP:\n")
        for metodo, quantidade in metodos.most_common():
            relatorio.write(f"- {metodo}: {quantidade}\n")

        relatorio.write(f"\nTOTAL DE STATUS 404: {total_404}\n")

    # Informa ao usuário que o arquivo foi criado com sucesso.
    print(f"[SUCESSO] Relatório gerado em: {caminho_saida}")


# Ponto de entrada do script quando executado diretamente.
if __name__ == "__main__":
    # Define os arquivos padrão de entrada e saída.
    CAMINHO_ENTRADA = "access.log"
    CAMINHO_SAIDA = "relatorio_apache.txt"

    try:
        # Executa a geração do relatório.
        gerar_relatorio(CAMINHO_ENTRADA, CAMINHO_SAIDA)
    except FileNotFoundError:
        # Trata o caso em que o arquivo de log não exista.
        print(f"Erro: o arquivo '{CAMINHO_ENTRADA}' não foi encontrado.")
