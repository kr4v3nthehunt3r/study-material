#!/usr/bin/env python3
"""
Autor: Kr4v3n
Arquivo: processar_logs_apache.py

Descrição do módulo:
    Este módulo processa múltiplas linhas de log Apache no formato Combined,
    gerando contadores com estatísticas básicas de análise.

Objetivos:
    - Ler uma coleção de linhas de log já carregadas em memória;
    - Contabilizar hosts, User-Agents, métodos HTTP e códigos de status;
    - Facilitar análises iniciais de tráfego web.
"""

from collections import Counter
import re
from typing import Iterable

# Expressão regular para parsing de logs Apache no formato Combined.
PADRAO_LOG = re.compile(
    r'^(?P<host>\S+) \S+ \S+ '
    r'\[(?P<data>[^\]]+)\] '
    r'"(?P<metodo>\S+) (?P<url>.*?) (?P<protocolo>[^\"]+)" '
    r'(?P<status>\d{3}) (?P<bytes>\S+) '
    r'"(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"$'
)


def processar_logs(linhas: Iterable[str]) -> tuple[Counter, Counter, Counter, Counter]:
    """
    Processa linhas de log Apache e retorna estatísticas agregadas.

    Parâmetros:
        linhas (Iterable[str]): Conjunto de linhas que será analisado.

    Retorno:
        tuple[Counter, Counter, Counter, Counter]:
            Retorna uma tupla contendo:
            - contagem de hosts;
            - contagem de User-Agents;
            - contagem de métodos HTTP;
            - contagem de códigos de status.
    """
    # Estruturas responsáveis por armazenar as contagens.
    contagem_hosts = Counter()
    contagem_user_agents = Counter()
    contagem_metodos = Counter()
    contagem_status = Counter()

    # Percorre cada linha recebida para extração das informações.
    for linha in linhas:
        # Remove espaços extras e ignora linhas vazias.
        linha = linha.strip()
        if not linha:
            continue

        # Tenta casar a linha com o padrão do Apache.
        correspondencia = PADRAO_LOG.match(linha)
        if not correspondencia:
            continue

        # Converte os grupos capturados em um dicionário.
        dados = correspondencia.groupdict()

        # Atualiza os contadores com base nos campos extraídos.
        contagem_hosts[dados["host"]] += 1
        contagem_metodos[dados["metodo"]] += 1
        contagem_status[dados["status"]] += 1
        contagem_user_agents[dados["user_agent"]] += 1

    # Retorna todas as estruturas consolidadas.
    return (
        contagem_hosts,
        contagem_user_agents,
        contagem_metodos,
        contagem_status,
    )


# Execução direta para teste rápido do módulo.
if __name__ == "__main__":
    # Conjunto de linhas de exemplo para simular um pequeno arquivo de log.
    linhas_exemplo = [
        '191.185.15.120 - - [04/Mar/2026:12:45:01 +0000] "GET /api/v1/products HTTP/1.1" 200 1542 "-" "Mozilla/5.0"',
        '191.185.15.120 - - [04/Mar/2026:12:45:03 +0000] "POST /login HTTP/1.1" 401 320 "-" "Mozilla/5.0"',
        '10.0.0.8 - - [04/Mar/2026:12:45:05 +0000] "GET /painel HTTP/1.1" 404 210 "-" "curl/8.0"',
    ]

    # Processa as linhas de exemplo e recebe os contadores resultantes.
    hosts, user_agents, metodos, status_codes = processar_logs(linhas_exemplo)

    # Exibe um resumo das estatísticas obtidas.
    print("=== RESUMO DE PROCESSAMENTO ===")
    print(f"Hosts:        {dict(hosts)}")
    print(f"Métodos:      {dict(metodos)}")
    print(f"Status:       {dict(status_codes)}")
    print(f"User-Agents:  {dict(user_agents)}")
