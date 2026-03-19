#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: contar_metodos.py
Descrição do módulo:
    Conta métodos HTTP a partir de uma lista simulada e exibe ranking de uso.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

from collections import Counter

def main() -> None:
    """Executa a contagem e exibe o ranking dos métodos HTTP."""
    metodos = ["GET", "GET", "POST", "PUT", "GET", "POST", "DELETE", "GET", "POST"]
    contagem = Counter(metodos)

    print("--- Ranking de Métodos HTTP ---")
    for metodo, total in contagem.most_common():
        print(f"Método: {metodo:<8} | Ocorrências: {total}")

    print("-" * 35)
    print(f"Top 2 métodos: {contagem.most_common(2)}")

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
