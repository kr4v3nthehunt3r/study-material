#!/usr/bin/env python3
"""
Autor: Kr4v3n
Arquivo: analisar_logs_apache.py

Descrição do módulo:
    Este módulo realiza uma análise mais completa de logs Apache no formato
    Combined, calculando estatísticas de hosts, métodos HTTP, User-Agents,
    volume trafegado e quantidade de registros processados.

Objetivos:
    - Ler um arquivo access.log;
    - Processar registros válidos do Apache;
    - Ignorar linhas vazias, inválidas e respostas 304;
    - Somar o volume total de bytes trafegados;
    - Exibir e gravar um relatório final em arquivo texto.
"""

from collections import Counter
import re
from typing import Iterable

# Expressão regular utilizada para interpretar logs Apache no formato Combined.
PADRAO_LOG = re.compile(
    r'^(?P<host>\S+) \S+ \S+ '
    r'\[(?P<data>[^\]]+)\] '
    r'"(?P<metodo>\S+) (?P<url>.*?) (?P<protocolo>[^\"]+)" '
    r'(?P<status>\d{3}) (?P<bytes>\S+) '
    r'"(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"$'
)


def processar_logs_completo(
    linhas: Iterable[str],
) -> tuple[Counter, Counter, Counter, int, int]:
    """
    Processa um conjunto de linhas de log e retorna estatísticas completas.

    Parâmetros:
        linhas (Iterable[str]): Linhas do arquivo de log que serão analisadas.

    Retorno:
        tuple[Counter, Counter, Counter, int, int]:
            Retorna uma tupla contendo:
            - contagem de hosts;
            - contagem de métodos HTTP;
            - contagem de User-Agents;
            - total de bytes trafegados;
            - quantidade de registros processados.
    """
    # Inicializa os contadores e acumuladores.
    contagem_hosts = Counter()
    contagem_metodos = Counter()
    contagem_user_agents = Counter()
    total_bytes = 0
    linhas_processadas = 0

    # Percorre todas as linhas recebidas para processamento.
    for linha in linhas:
        # Remove espaços extras e ignora linhas vazias.
        linha = linha.strip()
        if not linha:
            continue

        # Tenta interpretar a linha com a expressão regular.
        correspondencia = PADRAO_LOG.match(linha)
        if not correspondencia:
            continue

        # Extrai os campos da linha em formato de dicionário.
        dados = correspondencia.groupdict()

        # Ignora respostas 304, caso não sejam relevantes para a análise.
        if dados["status"] == "304":
            continue

        # Atualiza os contadores com os dados extraídos.
        contagem_hosts[dados["host"]] += 1
        contagem_metodos[dados["metodo"]] += 1
        contagem_user_agents[dados["user_agent"]] += 1

        # Soma os bytes somente quando o valor for numérico.
        if dados["bytes"] != "-":
            total_bytes += int(dados["bytes"])

        # Incrementa a quantidade de registros válidos processados.
        linhas_processadas += 1

    return (
        contagem_hosts,
        contagem_metodos,
        contagem_user_agents,
        total_bytes,
        linhas_processadas,
    )


def escrever_relatorio(caminho_entrada: str, caminho_saida: str) -> None:
    """
    Lê um arquivo de log Apache, processa os registros e grava um relatório.

    Parâmetros:
        caminho_entrada (str): Caminho do arquivo de entrada.
        caminho_saida (str): Caminho do arquivo de saída.
    """
    # Lê o arquivo completo de entrada com tolerância a erros de codificação.
    with open(caminho_entrada, "r", encoding="utf-8", errors="ignore") as arquivo:
        linhas = list(arquivo)

    # Processa as linhas e obtém as estatísticas consolidadas.
    hosts, metodos, uas, bytes_total, total_lidas = processar_logs_completo(linhas)

    # Abre o arquivo de saída para registrar o relatório.
    with open(caminho_saida, "w", encoding="utf-8") as relatorio:
        def escrever_e_imprimir(texto: str) -> None:
            """
            Escreve uma linha no relatório e também imprime no console.

            Parâmetros:
                texto (str): Conteúdo textual que será exibido e salvo.
            """
            # Exibe a linha no terminal.
            print(texto)
            # Grava a mesma linha no arquivo de relatório.
            relatorio.write(texto + "\n")

        # Cabeçalho do relatório.
        escrever_e_imprimir("=== RELATÓRIO DE TRÁFEGO WEB ===")
        escrever_e_imprimir(f"Registros processados: {total_lidas}")
        escrever_e_imprimir(f"Volume total de dados: {bytes_total / 1024:.2f} KB")
        escrever_e_imprimir("-" * 30)

        # Exibe os principais endereços IP de origem.
        escrever_e_imprimir("\nTOP 5 HOSTS (IPs):")
        for ip, quantidade in hosts.most_common(5):
            escrever_e_imprimir(f" - {ip}: {quantidade} requisições")

        # Exibe os métodos HTTP encontrados.
        escrever_e_imprimir("\nMÉTODOS HTTP:")
        for metodo, quantidade in metodos.most_common():
            escrever_e_imprimir(f" - {metodo}: {quantidade}")

        # Exibe os User-Agents mais recorrentes.
        escrever_e_imprimir("\nTOP 3 USER AGENTS:")
        for agente, quantidade in uas.most_common(3):
            agente_resumido = agente[:80] + ("..." if len(agente) > 80 else "")
            escrever_e_imprimir(f" - {agente_resumido} ({quantidade}x)")

    # Confirma a geração do relatório ao final do processo.
    print(f"\n[OK] Relatório gerado com sucesso em: {caminho_saida}")


# Bloco de execução principal do módulo.
if __name__ == "__main__":
    # Arquivos padrão utilizados na execução direta do script.
    CAMINHO_ENTRADA = "access.log"
    CAMINHO_SAIDA = "relatorio_final_apache.txt"

    try:
        # Executa a leitura, o processamento e a escrita do relatório.
        escrever_relatorio(CAMINHO_ENTRADA, CAMINHO_SAIDA)
    except FileNotFoundError:
        # Trata o erro caso o arquivo de entrada não exista.
        print(f"Erro: o arquivo '{CAMINHO_ENTRADA}' não foi encontrado para leitura.")
