"""
Autor: Kr4v3n
Arquivo: analisador_access_log.py

Descrição do módulo:
    Este módulo realiza a leitura e o processamento de um arquivo
    de log de acesso no formato Apache Combined Log.

Objetivos:
    - Ler um arquivo de log linha por linha;
    - Extrair informações relevantes de cada requisição;
    - Contabilizar hosts/IPs, User-Agents, métodos HTTP e status HTTP;
    - Exibir um relatório resumido com estatísticas básicas;
    - Tratar erro caso o arquivo não seja encontrado.
"""

# Importa a classe Counter da biblioteca collections.
# Ela é utilizada para contar automaticamente quantas vezes
# cada elemento aparece, como IPs, métodos, status e User-Agents.
from collections import Counter

# Importa o módulo de expressões regulares.
# Ele será utilizado para definir um padrão de parsing das linhas de log.
import re

# Define e compila o padrão de log Apache Combined.
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

def processar_logs(linhas):
    """
    Processa uma sequência de linhas de log e retorna contadores
    com informações estatísticas sobre os dados extraídos.

    Parâmetros:
        linhas (iterável): Coleção de linhas de log em formato de texto.
        Pode ser uma lista, tupla ou até mesmo o próprio arquivo aberto.

    Retorno:
        tuple:
            - hosts (Counter): Contador de ocorrências por host/IP;
            - user_agents (Counter): Contador de ocorrências por User-Agent;
            - metodos (Counter): Contador de ocorrências por método HTTP;
            - status_codes (Counter): Contador de ocorrências por código de status HTTP.
    """
    # Cria um contador para armazenar a frequência de cada host/IP.
    hosts = Counter()

    # Cria um contador para armazenar a frequência de cada User-Agent.
    user_agents = Counter()

    # Cria um contador para armazenar a frequência de cada método HTTP.
    metodos = Counter()

    # Cria um contador para armazenar a frequência de cada status HTTP.
    status_codes = Counter()

    # Percorre cada linha recebida.
    for linha in linhas:
        # Remove espaços extras e quebras de linha.
        linha = linha.strip()

        # Ignora linhas vazias.
        if not linha:
            continue

        # Tenta aplicar o padrão regex à linha atual.
        match = PADRAO_LOG.match(linha)

        # Se a linha corresponder ao formato esperado, extrai os dados.
        if match:
            # Extrai o host/IP de origem.
            host = match.group(1)

            # Extrai o método HTTP utilizado.
            metodo = match.group(3)

            # Extrai o código de status HTTP retornado.
            status = match.group(5)

            # Extrai o User-Agent do cliente.
            ua = match.group(8)

            # Atualiza o contador de hosts/IPs.
            hosts[host] += 1

            # Atualiza o contador de métodos HTTP.
            metodos[metodo] += 1

            # Atualiza o contador de códigos de status HTTP.
            status_codes[status] += 1

            # Atualiza o contador de User-Agents.
            user_agents[ua] += 1

    # Retorna todos os contadores gerados.
    return hosts, user_agents, metodos, status_codes

def exibir_relatorio(c_hosts, c_ua, c_metodos, c_status):
    """
    Exibe um relatório resumido com base nos contadores gerados
    pelo processamento do arquivo de log.

    Parâmetros:
        c_hosts (Counter): Contador de hosts/IPs.
        c_ua (Counter): Contador de User-Agents.
        c_metodos (Counter): Contador de métodos HTTP.
        c_status (Counter): Contador de códigos de status HTTP.

    Retorno:
        None
    """
    print("--- Relatório de Acessos ---")
    print(f"Total de IPs únicos: {len(c_hosts)}")
    print(f"Top 3 IPs: {c_hosts.most_common(3)}")
    print(f"Método mais usado: {c_metodos.most_common(1)}")
    print(f"Status 404 encontrados: {c_status['404']}")

def main():
    """
    Função principal do programa.

    Responsabilidades:
        - Definir o caminho do arquivo de log;
        - Abrir o arquivo para leitura;
        - Processar as linhas do log;
        - Exibir o relatório final;
        - Tratar erro caso o arquivo não exista.

    Retorno:
        None
    """
    # Define o caminho do arquivo de log que será analisado.
    caminho = "access.log"

    try:
        # Abre o arquivo em modo leitura com codificação UTF-8.
        with open(caminho, "r", encoding="utf-8") as arquivo:
            # Passa o iterador do arquivo diretamente para a função de processamento.
            c_hosts, c_ua, c_metodos, c_status = processar_logs(arquivo)

        # Exibe o relatório com os dados processados.
        exibir_relatorio(c_hosts, c_ua, c_metodos, c_status)

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho.")

# Garante que a função principal será executada apenas
# quando este arquivo for chamado diretamente.
if __name__ == "__main__":
    main()