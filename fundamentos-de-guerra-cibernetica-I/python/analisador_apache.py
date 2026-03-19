"""
Autor: Kr4v3n
Arquivo: analisador_apache.py
Descrição:
    Este módulo realiza a extração e a análise básica de linhas de log
    no formato Apache. O script identifica campos como IP, data, método,
    URL, versão HTTP, status e quantidade de bytes trafegados.

Objetivo:
    - Interpretar linhas de log Apache com expressão regular;
    - Extrair dados estruturados de cada linha;
    - Contar IPs mais ativos;
    - Contabilizar códigos de status HTTP encontrados.
"""

# Importa o módulo de expressões regulares,
# utilizado para definir e aplicar o padrão de parsing do log.
import re

# Importa Counter da biblioteca collections,
# usado para contar ocorrências de elementos em listas.
from collections import Counter

# Expressão regular compilada para interpretar linhas de log Apache.
# O padrão abaixo tenta capturar:
# - ip: endereço IP de origem
# - data: data/hora da requisição
# - metodo: método HTTP (GET, POST etc.)
# - url: recurso solicitado
# - versao: versão do protocolo HTTP (opcional)
# - status: código de status HTTP
# - bytes: quantidade de bytes retornados
REGEX_APACHE = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<data>[^\]]+)\]\s+"(?P<metodo>\S+)\s+(?P<url>\S+)(?:\s+HTTP/(?P<versao>[\d.]+))?"\s+(?P<status>\d{3})\s+(?P<bytes>\S+)'
)

def extrair_dados_log(linha):
    """
    Extrai os dados de uma linha de log Apache.

    Parâmetros:
        linha (str): Linha do log Apache que será analisada.

    Retorno:
        dict | None:
            - Retorna um dicionário com os campos extraídos se a linha
              corresponder ao padrão esperado;
            - Retorna None caso a linha não seja compatível com o padrão.
    """
    resultado = REGEX_APACHE.match(linha)

    if resultado:
        return resultado.groupdict()

    return None

def analisar_linhas_log(linhas):
    """
    Analisa uma coleção de linhas de log Apache e gera estatísticas básicas.

    Parâmetros:
        linhas (list[str]): Lista contendo linhas de log Apache.

    Retorno:
        tuple:
            - lista_dados (list[dict]): Lista com os dados extraídos de cada linha válida;
            - contagem_ips (Counter): Contador com a frequência de cada IP;
            - contagem_status (Counter): Contador com a frequência de cada status HTTP.
    """
    lista_dados = []
    lista_ips = []
    lista_status = []

    for linha in linhas:
        dados = extrair_dados_log(linha)

        if dados:
            lista_dados.append(dados)
            lista_ips.append(dados["ip"])
            lista_status.append(dados["status"])

    contagem_ips = Counter(lista_ips)
    contagem_status = Counter(lista_status)

    return lista_dados, contagem_ips, contagem_status

def exibir_resultados(dados_extraidos, contagem_ips, contagem_status):
    """
    Exibe na tela os dados processados e as estatísticas geradas.

    Parâmetros:
        dados_extraidos (list[dict]): Lista com os registros válidos extraídos do log.
        contagem_ips (Counter): Contador de ocorrências por IP.
        contagem_status (Counter): Contador de ocorrências por status HTTP.

    Retorno:
        None
    """
    print("Dados extraídos das linhas válidas:")
    for item in dados_extraidos:
        print(
            f"IP: {item['ip']} | "
            f"Data: {item['data']} | "
            f"Método: {item['metodo']} | "
            f"URL: {item['url']} | "
            f"Versão HTTP: {item['versao']} | "
            f"Status: {item['status']} | "
            f"Bytes: {item['bytes']}"
        )

    print("-" * 50)

    if contagem_ips:
        ip_mais_ativo, total = contagem_ips.most_common(1)[0]
        print(f"IP mais ativo: {ip_mais_ativo} ({total} ocorrências)")
    else:
        print("Nenhum IP válido foi encontrado.")

    print("Distribuição de Status HTTP:")
    for status, quantidade in contagem_status.most_common():
        print(f"Status {status}: {quantidade}")

def main():
    """
    Função principal do programa.

    Responsabilidades:
        - Definir exemplos de linhas de log;
        - Executar a análise das linhas;
        - Exibir os resultados na tela.

    Retorno:
        None
    """
    # Exemplo de linha única de log Apache para teste inicial.
    log_exemplo = '63.223.125.170 - - [18/May/2015:19:05:19 +0000] "GET /index.html HTTP/1.1" 200 37269'

    # Tenta extrair os dados da linha de exemplo.
    dados_exemplo = extrair_dados_log(log_exemplo)

    print("Teste com linha única:")
    if dados_exemplo:
        print(f"IP capturado: {dados_exemplo['ip']}")
        print(f"Método: {dados_exemplo['metodo']}")
        print(f"Status: {dados_exemplo['status']}")
    else:
        print("A linha de exemplo não corresponde ao padrão esperado.")

    print("-" * 50)

    # Lista simulando várias linhas vindas de um arquivo de log.
    linhas_arquivo = [
        '63.223.125.170 - - [18/May/2015:19:05:19] "GET /index.html" 200 37269',
        '63.223.125.170 - - [18/May/2015:19:06:01] "GET /favicon.ico" 404 120',
        '10.0.0.5 - - [18/May/2015:19:07:10] "POST /login" 200 4500',
        '63.223.125.170 - - [18/May/2015:19:08:55] "GET /index.html" 200 37269',
    ]

    # Executa a análise das linhas.
    dados_extraidos, contagem_ips, contagem_status = analisar_linhas_log(linhas_arquivo)

    # Exibe os resultados finais.
    exibir_resultados(dados_extraidos, contagem_ips, contagem_status)

# Garante que o programa principal só será executado
# quando este arquivo for chamado diretamente.
if __name__ == "__main__":
    main()