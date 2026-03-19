#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: operacoes_basicas.py
Descrição do módulo:
    Calcula operações aritméticas e exponenciais a partir de três números.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import math
import sys

def ler_numero(mensagem: str) -> float:
    """Lê um número real informado pelo usuário."""
    entrada = input(mensagem).strip().replace(",", ".")
    if not entrada:
        raise ValueError("Todos os valores precisam ser informados.")
    return float(entrada)

def main() -> None:
    """Função principal da calculadora."""
    print("--- Calculadora de Operações Básicas ---")
    try:
        numero_1 = ler_numero("Digite o primeiro número: ")
        numero_2 = ler_numero("Digite o segundo número: ")
        numero_3 = ler_numero("Digite o multiplicador: ")

        soma_multiplicada = (numero_1 + numero_2) * numero_3
        quadrado = numero_1 ** 2
        cubo = numero_1 ** 3
        potencia = numero_1 ** numero_2

        print("-" * 55)
        print(f"[*] ({numero_1} + {numero_2}) x {numero_3} = {soma_multiplicada:.2f}")
        print(f"[*] Quadrado de {numero_1}: {quadrado:.2f}")
        print(f"[*] Cubo de {numero_1}:     {cubo:.2f}")
        print(f"[*] Potência:               {potencia:.2f}")
        if potencia >= 0:
            print(f"[*] Raiz da potência:       {math.sqrt(potencia):.2f}")
        else:
            print("[*] Raiz da potência:       não definida nos reais")
        print("-" * 55)
    except ValueError as erro:
        print(f"[-] Erro: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
