#!/usr/bin/env python3
"""
Autor: Kr4v3n
Arquivo: relatorio_trafego_web.py

Descrição do módulo:
    Este módulo realiza a leitura e o processamento de um arquivo de log
    no formato Apache Combined Log, gerando estatísticas sobre o tráfego web.

Objetivos:
    - Ler um arquivo de log Apache;
    - Ignorar linhas vazias e registros com status 304;
    - Contabilizar hosts/IPs, métodos HTTP e User-Agents;
    - Somar o volume total de bytes trafegados;
    - Exibir os resultados no terminal;
    - Salvar um relatório consolidado em arquivo texto.
"""

# Importa o módulo de expressões regulares.
# Ele será utilizado para definir e aplicar o padrão de parsing
# das linhas do arquivo de log.
import re

# Importa a classe Counter da biblioteca collections.
# Ela é utilizada para contar automaticamente a frequência de elementos,
# como hosts, métodos HTTP e User-Agents.
from collections import Counter

# Define e compila o padrão de log Apache Combined.
# Os grupos capturados representam:
# 1. Host/IP de origem
# 2. Data e hora da requisição
# 3. Método HTTP
# 4. Recurso solicitado e versão HTTP
# 5. Código de status HTTP
# 6. Quantidade de bytes retornados
# 7. Referer
# 8. User-Agent
PADRAO_LOG = re.compile(
    r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) ([^"]*)" (\d{3}) (\S+) "([^"]*)" "([^"]*)"$'
)

def processar_logs_completo(linhas):
    """
    Processa uma coleção de linhas de log e retorna estatísticas completas.

    Regras aplicadas:
        - Linhas vazias são ignoradas;
        - Linhas fora do padrão esperado são ignoradas;
        - Registros com status 304 são ignorados;
        - O campo de bytes é somado apenas quando contém valor numérico.

    Parâmetros:
        linhas (list | iterable):
            Coleção de linhas de log que será analisada.

    Retorno:
        tuple:
            - contagem_hosts (Counter): Contador de ocorrências por host/IP;
            - contagem_metodos (Counter): Contador de ocorrências por método HTTP;
            - contagem_ua (Counter): Contador de ocorrências por User-Agent;
            - total_bytes (int): Soma total dos bytes trafegados;
            - linhas_processadas (int): Quantidade total de registros válidos processados.
    """
    # Inicializa o contador de hosts/IPs.
    contagem_hosts = Counter()

    # Inicializa o contador de métodos HTTP.
    contagem_metodos = Counter()

    # Inicializa o contador de User-Agents.
    contagem_ua = Counter()

    # Inicializa a variável que armazenará o total de bytes trafegados.
    total_bytes = 0

    # Inicializa a contagem de linhas válidas processadas.
    linhas_processadas = 0

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

        # Extrai os campos relevantes da linha.
        host = correspondencia.group(1)
        metodo = correspondencia.group(3)
        status = correspondencia.group(5)
        bytes_str = correspondencia.group(6)
        user_agent = correspondencia.group(8)

        # Ignora registros com status 304.
        if status == "304":
            continue

        # Atualiza os contadores com os dados extraídos.
        contagem_hosts[host] += 1
        contagem_metodos[metodo] += 1
        contagem_ua[user_agent] += 1

        # Soma os bytes apenas quando o campo não for "-".
        # O Apache utiliza "-" quando não há valor numérico disponível.
        if bytes_str.isdigit():
            total_bytes += int(bytes_str)

        # Incrementa a quantidade de linhas válidas processadas.
        linhas_processadas += 1

    # Retorna todas as estatísticas calculadas.
    return contagem_hosts, contagem_metodos, contagem_ua, total_bytes, linhas_processadas

def escrever_e_imprimir(texto, arquivo_saida):
    """
    Exibe um texto no terminal e também grava esse mesmo texto
    em um arquivo de saída.

    Parâmetros:
        texto (str): Conteúdo que será exibido e salvo.
        arquivo_saida (TextIO): Arquivo aberto em modo escrita.

    Retorno:
        None
    """
    print(texto)
    arquivo_saida.write(texto + "\n")

def formatar_user_agent(user_agent, limite=80):
    """
    Formata o User-Agent para exibição, limitando o tamanho
    do texto quando necessário.

    Parâmetros:
        user_agent (str): Texto completo do User-Agent.
        limite (int): Quantidade máxima de caracteres exibidos.

    Retorno:
        str:
            User-Agent original, se estiver dentro do limite,
            ou versão truncada com reticências.
    """
    if len(user_agent) <= limite:
        return user_agent
    return user_agent[:limite] + "..."

def main():
    """
    Função principal do programa.

    Responsabilidades:
        - Definir os caminhos dos arquivos de entrada e saída;
        - Ler o arquivo de log com segurança;
        - Processar os registros encontrados;
        - Gerar o relatório no terminal e em arquivo texto;
        - Tratar erros de arquivo não encontrado e falhas inesperadas.

    Retorno:
        None
    """
    # Define o caminho do arquivo de entrada.
    caminho_entrada = "access.log"

    # Define o caminho do arquivo de saída.
    caminho_saida = "relatorio_final.txt"

    try:
        # Abre o arquivo de log para leitura com segurança.
        with open(caminho_entrada, "r", encoding="utf-8", errors="ignore") as arquivo_entrada:
            # Constrói uma lista com todas as linhas do arquivo.
            todas_as_linhas = list(arquivo_entrada)

        # Processa as linhas lidas do arquivo.
        hosts, metodos, uas, bytes_total, total_lidas = processar_logs_completo(todas_as_linhas)

        # Abre o arquivo de saída para gravação do relatório.
        with open(caminho_saida, "w", encoding="utf-8") as relatorio:
            # Escreve e exibe o cabeçalho do relatório.
            escrever_e_imprimir("=== RELATÓRIO DE TRÁFEGO WEB ===", relatorio)
            escrever_e_imprimir(f"Registros processados: {total_lidas}", relatorio)
            escrever_e_imprimir(f"Volume total de dados: {bytes_total / 1024:.2f} KB", relatorio)
            escrever_e_imprimir("-" * 30, relatorio)

            # Exibe e salva o Top 5 hosts.
            escrever_e_imprimir("", relatorio)
            escrever_e_imprimir("TOP 5 HOSTS (IPs):", relatorio)
            for ip, quantidade in hosts.most_common(5):
                escrever_e_imprimir(f" - {ip}: {quantidade} requisições", relatorio)

            # Exibe e salva a distribuição dos métodos HTTP.
            escrever_e_imprimir("", relatorio)
            escrever_e_imprimir("MÉTODOS HTTP:", relatorio)
            for metodo, quantidade in metodos.most_common():
                escrever_e_imprimir(f" - {metodo}: {quantidade}", relatorio)

            # Exibe e salva o Top 3 User-Agents.
            escrever_e_imprimir("", relatorio)
            escrever_e_imprimir("TOP 3 USER AGENTS:", relatorio)
            for agent, quantidade in uas.most_common(3):
                agent_formatado = formatar_user_agent(agent)
                escrever_e_imprimir(f" - {agent_formatado} ({quantidade}x)", relatorio)

        # Informa ao usuário que o relatório foi gerado com sucesso.
        print(f"\n[OK] Relatório gerado com sucesso em: {caminho_saida}")

    except FileNotFoundError:
        # Informa erro caso o arquivo de entrada não seja encontrado.
        print(f"Erro: o arquivo '{caminho_entrada}' não foi encontrado para leitura.")
    except Exception as erro:
        # Trata qualquer erro inesperado durante a execução.
        print(f"Ocorreu um erro inesperado: {erro}")

# Garante que a função principal será executada apenas
# quando este arquivo for executado diretamente.
if __name__ == "__main__":
    main()