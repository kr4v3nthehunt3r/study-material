#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: analisar_log_apache.py
Descrição do módulo:
    Faz o parsing básico de uma linha de log Apache no formato Combined.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import re

# Importações utilizadas por este módulo.

PADRAO_APACHE = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<data>.*?)\] "(?P<metodo>\S+) (?P<url>\S+) (?P<protocolo>[^"]+)" (?P<status>\d{3}) (?P<bytes>\S+)'
)

def analisar_linha_log(linha: str) -> dict[str, str] | None:
    """Extrai os principais campos de uma linha de log Apache."""
    resultado = PADRAO_APACHE.match(linha)
    return resultado.groupdict() if resultado else None

def main() -> None:
    """Executa um exemplo simples de parsing."""
    log_exemplo = '63.223.125.170 - - [18/May/2015:19:05:19 +0000] "GET /index.html HTTP/1.1" 200 37269'
    dados = analisar_linha_log(log_exemplo)

    if not dados:
        print("[-] Linha de log inválida.")
        return

    print("--- Análise de Log Apache ---")
    print(f"[*] IP:        {dados['ip']}")
    print(f"[*] Data:      {dados['data']}")
    print(f"[*] Método:    {dados['metodo']}")
    print(f"[*] URL:       {dados['url']}")
    print(f"[*] Protocolo: {dados['protocolo']}")
    print(f"[*] Status:    {dados['status']}")
    print(f"[*] Bytes:     {dados['bytes']}")

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
