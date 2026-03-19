#!/usr/bin/env python3
"""
Autor: Kr4v3n
Arquivo: analisador_logs_apache.py

Descrição do módulo:
    Este módulo realiza a leitura, o processamento e a geração de um
    relatório simples a partir de um arquivo de log no formato
    Apache Combined Log.

Objetivos:
    - Ler um arquivo de log de entrada;
    - Ignorar linhas vazias;
    - Processar os registros válidos com expressão regular;
    - Contabilizar hosts, métodos HTTP, User-Agents e erros 404;
    - Ignorar respostas com status 304;
    - Gerar um relatório em arquivo texto;
    - Exibir um resumo no terminal.
"""

# Importa o módulo de expressões regulares.
# Ele é utilizado para criar um padrão capaz de identificar
# e extrair dados estruturados das linhas do log Apache.
import re

# Importa a classe Counter da biblioteca collections.
# Ela é utilizada para contar automaticamente a frequência
# de elementos como IPs, métodos HTTP e User-Agents.
from collections import Counter

# Define e compila a expressão regular para o formato
# Apache Combined Log.
# Os grupos capturados representam:
# 1. Host/IP de origem
# 2. Data e hora da requisição
# 3. Método HTTP
# 4. Recurso solicitado
# 5. Código de status HTTP
# 6. Quantidade de bytes retornados
# 7. Referer
# 8. User-Agent
PADRAO_LOG = re.compile(
    r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) ([^"]*)" (\d{3}) (\S+) "([^"]*)" "([^"]*)"'
)

def ler_linhas_validas(caminho_entrada):
    """
    Lê um arquivo de log e retorna apenas as linhas não vazias.

    Parâmetros:
        caminho_entrada (str): Caminho do arquivo de log de entrada.

    Retorno:
        list:
            Lista contendo apenas as linhas não vazias do arquivo,
            já com espaços extras removidos.

    Exceções:
        FileNotFoundError:
            Ocorre quando o arquivo informado não é encontrado.
    """
    with open(caminho_entrada, "r", encoding="utf-8", errors="ignore") as arquivo:
        return [linha.strip() for linha in arquivo if linha.strip()]

def processar_logs(linhas):
    """
    Processa as linhas de log e devolve estatísticas detalhadas.

    Regras aplicadas:
        - Linhas vazias são ignoradas;
        - Linhas fora do padrão esperado são ignoradas;
        - Registros com status 304 são ignorados;
        - Status 404 são contabilizados separadamente.

    Parâmetros:
        linhas (list | iterable):
            Coleção de linhas de log a serem analisadas.

    Retorno:
        tuple:
            - hosts (Counter): Contador de ocorrências por host/IP;
            - user_agents (Counter): Contador de ocorrências por User-Agent;
            - metodos (Counter): Contador de ocorrências por método HTTP;
            - total_404 (int): Quantidade total de respostas com status 404.
    """
    # Inicializa o contador de hosts/IPs.
    hosts = Counter()

    # Inicializa o contador de User-Agents.
    user_agents = Counter()

    # Inicializa o contador de métodos HTTP.
    metodos = Counter()

    # Inicializa o contador total de erros 404.
    total_404 = 0

    # Percorre cada linha recebida para análise.
    for linha in linhas:
        # Remove espaços extras e quebras de linha.
        linha = linha.strip()

        # Ignora linhas vazias.
        if not linha:
            continue

        # Tenta aplicar o padrão regex à linha atual.
        correspondencia = PADRAO_LOG.match(linha)

        # Ignora linhas que não seguem o formato esperado.
        if not correspondencia:
            continue

        # Extrai o código de status HTTP.
        status = correspondencia.group(5)

        # Ignora registros com status 304, conforme solicitado.
        if status == "304":
            continue

        # Extrai os demais campos necessários para estatística.
        host = correspondencia.group(1)
        metodo = correspondencia.group(3)
        user_agent = correspondencia.group(8)

        # Atualiza os contadores com os dados extraídos.
        hosts[host] += 1
        user_agents[user_agent] += 1
        metodos[metodo] += 1

        # Conta separadamente os registros com erro 404.
        if status == "404":
            total_404 += 1

    # Retorna todos os resultados processados.
    return hosts, user_agents, metodos, total_404

def gerar_relatorio(caminho_saida, hosts, user_agents, metodos, total_404):
    """
    Gera um relatório de análise em arquivo texto.

    O relatório contém:
        - Top 3 hosts;
        - Top 5 User-Agents;
        - Método HTTP mais usado;
        - Total de erros 404.

    Parâmetros:
        caminho_saida (str): Caminho do arquivo de relatório.
        hosts (Counter): Contador de hosts/IPs.
        user_agents (Counter): Contador de User-Agents.
        metodos (Counter): Contador de métodos HTTP.
        total_404 (int): Quantidade total de respostas 404.

    Retorno:
        None
    """
    with open(caminho_saida, "w", encoding="utf-8") as relatorio:
        relatorio.write("=== RELATÓRIO DE ANÁLISE DE LOGS ===\n\n")

        # Escreve no arquivo o Top 3 de hosts.
        relatorio.write("TOP 3 HOSTS:\n")
        for indice, (host, quantidade) in enumerate(hosts.most_common(3), start=1):
            relatorio.write(f"{indice}. {host} ({quantidade} requisições)\n")

        relatorio.write("\n" + "-" * 30 + "\n\n")

        # Escreve no arquivo o Top 5 de User-Agents.
        relatorio.write("TOP USER AGENTS:\n")
        for indice, (ua, quantidade) in enumerate(user_agents.most_common(5), start=1):
            relatorio.write(f"{indice}. {ua} ({quantidade} acessos)\n")

        relatorio.write("\n" + "-" * 30 + "\n\n")

        # Escreve no arquivo o método mais utilizado.
        if metodos:
            metodo_mais_usado, quantidade = metodos.most_common(1)[0]
            relatorio.write(f"MÉTODO MAIS USADO: {metodo_mais_usado} ({quantidade} ocorrências)\n")
        else:
            relatorio.write("MÉTODO MAIS USADO: nenhum registro válido encontrado\n")

        # Escreve no arquivo o total de erros 404.
        relatorio.write(f"TOTAL DE STATUS 404: {total_404}\n")

def exibir_resumo_console(hosts, user_agents, metodos, total_404):
    """
    Exibe no terminal um resumo dos resultados obtidos na análise.

    Parâmetros:
        hosts (Counter): Contador de hosts/IPs.
        user_agents (Counter): Contador de User-Agents.
        metodos (Counter): Contador de métodos HTTP.
        total_404 (int): Quantidade total de respostas 404.

    Retorno:
        None
    """
    print("--- Relatório de Análise ---")
    print(f"Total de IPs únicos: {len(hosts)}")

    print("\nHOSTS (Top 3):")
    for indice, (host, quantidade) in enumerate(hosts.most_common(3), start=1):
        print(f"  {indice}. {host} ({quantidade} requisições)")

    print("\nTOP USER AGENTS:")
    for indice, (ua, quantidade) in enumerate(user_agents.most_common(5), start=1):
        print(f"  {indice}. {ua} ({quantidade} acessos)")

    if metodos:
        metodo_mais_usado, quantidade = metodos.most_common(1)[0]
        print(f"\nMétodo mais usado: {metodo_mais_usado} ({quantidade} ocorrências)")
    else:
        print("\nMétodo mais usado: nenhum registro válido encontrado")

    print(f"Total de erros 404: {total_404}")

def main():
    """
    Função principal do programa.

    Responsabilidades:
        - Definir os caminhos de entrada e saída;
        - Ler as linhas válidas do arquivo de log;
        - Processar os registros;
        - Exibir o resumo no terminal;
        - Gerar o relatório em arquivo texto;
        - Tratar erro de arquivo não encontrado.

    Retorno:
        None
    """
    # Define o caminho do arquivo de entrada.
    caminho_entrada = "access.log"

    # Define o caminho do arquivo de saída.
    caminho_saida = "relatorio_treino.txt"

    try:
        # Lê as linhas válidas do arquivo de log.
        linhas = ler_linhas_validas(caminho_entrada)

        # Exibe a quantidade de registros lidos.
        print(f"Total de registros lidos: {len(linhas)}\n")

        # Processa as linhas e obtém as estatísticas.
        hosts, user_agents, metodos, total_404 = processar_logs(linhas)

        # Exibe o resumo no terminal.
        exibir_resumo_console(hosts, user_agents, metodos, total_404)

        # Gera o relatório em arquivo texto.
        gerar_relatorio(caminho_saida, hosts, user_agents, metodos, total_404)

        print(f"\n[SUCESSO] Relatório detalhado salvo em: {caminho_saida}")

    except FileNotFoundError:
        # Informa quando o arquivo de entrada não for encontrado.
        print(f"Erro: o arquivo '{caminho_entrada}' não foi encontrado.")

# Garante que a função principal será executada somente
# quando este arquivo for executado diretamente.
if __name__ == "__main__":
    main()