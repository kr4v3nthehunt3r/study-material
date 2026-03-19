#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Calcula soma, multiplicação, potência, quadrado, cubo e raiz quadrada a partir
    de três valores informados pelo usuário.

Melhorias aplicadas:
    - Padronização dos textos;
    - Validação de entradas;
    - Estrutura mais organizada.
"""

import math
import sys


def ler_numero(mensagem: str) -> float:
    """Lê um número informado pelo usuário e converte para float."""
    valor = input(mensagem).strip().replace(",", ".")
    if not valor:
        raise ValueError("Todos os campos devem ser preenchidos.")
    return float(valor)


def main() -> None:
    """Executa o cálculo das operações aritméticas."""
    print("--- Calculadora de Operações Aritméticas ---")

    try:
        numero_1 = ler_numero("Digite o primeiro número base: ")
        numero_2 = ler_numero("Digite o segundo número base: ")
        numero_3 = ler_numero("Digite o multiplicador: ")

        print("-" * 50)

        resultado_soma_multiplicada = (numero_1 + numero_2) * numero_3
        print(
            f"[*] ({numero_1} + {numero_2}) x {numero_3} = "
            f"{resultado_soma_multiplicada:.2f}"
        )

        quadrado = numero_1 ** 2
        cubo = numero_1 ** 3
        print(f"[*] Quadrado de {numero_1}: {quadrado:.2f}")
        print(f"[*] Cubo de {numero_1}: {cubo:.2f}")

        potencia = numero_1 ** numero_2
        print(f"[*] {numero_1} elevado a {numero_2}: {potencia:.2f}")

        if potencia < 0:
            print("[*] Raiz quadrada: não definida no conjunto dos reais para valor negativo.")
        else:
            print(f"[*] Raiz quadrada da potência: {math.sqrt(potencia):.2f}")

        print("-" * 50)

    except ValueError as erro:
        print(f"[-] Erro de entrada: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada pelo usuário.")
        sys.exit(0)


if __name__ == "__main__":
    main()
