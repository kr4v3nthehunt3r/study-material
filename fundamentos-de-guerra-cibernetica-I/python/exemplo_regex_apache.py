#!/usr/bin/env python3
"""
Autor: Kr4v3n
Arquivo: exemplo_regex_apache.py

Descrição do módulo:
    Este módulo demonstra, de forma simples, como utilizar uma expressão
    regular para extrair informações básicas de uma linha de log Apache.

Objetivos:
    - Definir um padrão de expressão regular para logs Apache;
    - Testar o padrão com uma linha de exemplo;
    - Exibir os principais campos capturados;
    - Servir como exemplo introdutório para estudos de parsing de logs.
"""

import re
from typing import Optional

# Expressão regular utilizada para capturar campos essenciais do log Apache.
# Os grupos nomeados facilitam a leitura e o acesso aos valores extraídos.
PADRAO_LOG_APACHE = re.compile(
    r'(?P<ip>\S+) \S+ \S+ '
    r'\[(?P<data>.*?)\] '
    r'"(?P<metodo>\S+) (?P<url>\S+) .*?" '
    r'(?P<status>\d+) (?P<bytes>\S+)'
)


def extrair_dados_basicos(linha_log: str) -> Optional[dict[str, str]]:
    """
    Extrai os principais campos de uma única linha de log Apache.

    Parâmetros:
        linha_log (str): Linha do log que será analisada.

    Retorno:
        Optional[dict[str, str]]:
            Retorna um dicionário com os dados capturados caso o padrão seja
            encontrado. Caso contrário, retorna None.
    """
    # Tenta aplicar o padrão à linha informada.
    correspondencia = PADRAO_LOG_APACHE.match(linha_log)

    # Se não houver correspondência, o retorno será None.
    if not correspondencia:
        return None

    # Converte os grupos capturados em dicionário para facilitar o uso.
    return correspondencia.groupdict()


# Bloco de execução direta do script.
if __name__ == "__main__":
    # Linha de exemplo para demonstrar o funcionamento do parser.
    log_exemplo = (
        '63.223.125.170 - - [18/May/2015:19:05:19 +0000] '
        '"GET /index.html HTTP/1.1" 200 37269'
    )

    # Executa a extração dos dados da linha informada.
    dados = extrair_dados_basicos(log_exemplo)

    # Exibe o resultado do processamento.
    if dados:
        print(f"IP capturado: {dados['ip']}")
        print(f"Data: {dados['data']}")
        print(f"Método: {dados['metodo']}")
        print(f"URL: {dados['url']}")
        print(f"Status: {dados['status']}")
        print(f"Bytes: {dados['bytes']}")
    else:
        print("A linha informada não corresponde ao padrão esperado.")
