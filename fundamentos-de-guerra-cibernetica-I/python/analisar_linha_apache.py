#!/usr/bin/env python3
"""
Autor: Kr4v3n
Arquivo: analisar_linha_apache.py

Descrição do módulo:
    Este módulo realiza a análise de uma única linha de log Apache no formato
    Combined, retornando os principais campos encontrados no registro.

Objetivos:
    - Interpretar uma linha individual de log Apache;
    - Extrair host, data, método, URL, protocolo, status, bytes, referer e
      User-Agent;
    - Demonstrar a análise unitária de um registro de acesso web.
"""

import re
from typing import Optional

# Padrão de expressão regular para logs Apache no formato Combined.
# O uso de grupos nomeados torna o código mais legível e fácil de manter.
PADRAO_LOG = re.compile(
    r'^(?P<host>\S+) \S+ \S+ '
    r'\[(?P<data>[^\]]+)\] '
    r'"(?P<metodo>\S+) (?P<url>.*?) (?P<protocolo>[^\"]+)" '
    r'(?P<status>\d{3}) (?P<bytes>\S+) '
    r'"(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"$'
)


def analisar_linha_log(linha: str) -> Optional[dict[str, str]]:
    """
    Analisa uma única linha de log Apache e retorna os campos extraídos.

    Parâmetros:
        linha (str): Linha do log que será processada.

    Retorno:
        Optional[dict[str, str]]:
            Um dicionário com os campos do log, caso a linha esteja no formato
            esperado. Se a linha não corresponder ao padrão, retorna None.
    """
    # Remove espaços excedentes no início e no fim da linha.
    linha = linha.strip()

    # Tenta casar a linha com o padrão definido.
    correspondencia = PADRAO_LOG.match(linha)

    # Caso não haja correspondência, informa falha por meio de None.
    if not correspondencia:
        return None

    # Retorna todos os grupos capturados em formato de dicionário.
    return correspondencia.groupdict()


# Execução direta do módulo para fins de teste e demonstração.
if __name__ == "__main__":
    # Linha de exemplo simulando um acesso realizado por dispositivo móvel.
    linha_real = (
        '191.185.15.120 - - [04/Mar/2026:12:45:01 +0000] '
        '"GET /api/v1/products HTTP/1.1" 200 1542 "-" '
        '"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) '
        'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 '
        'Mobile/15E148 Safari/604.1"'
    )

    # Processa a linha de exemplo.
    dados = analisar_linha_log(linha_real)

    # Exibe o relatório simplificado com os campos encontrados.
    if dados:
        print("=== RELATÓRIO SIMPLIFICADO ===")
        print(f"Host:       {dados['host']}")
        print(f"Data:       {dados['data']}")
        print(f"Método:     {dados['metodo']}")
        print(f"URL:        {dados['url']}")
        print(f"Protocolo:  {dados['protocolo']}")
        print(f"Status:     {dados['status']}")
        print(f"Bytes:      {dados['bytes']}")
        print(f"Referer:    {dados['referer']}")
        print(f"User-Agent: {dados['user_agent']}")
    else:
        print("A linha não condiz com o padrão esperado.")
