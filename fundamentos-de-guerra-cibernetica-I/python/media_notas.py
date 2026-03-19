#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: media_notas.py
Descrição do módulo:
    Lê duas notas, calcula a média final e informa a situação do aluno.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import sys

def ler_nota(mensagem: str) -> float:
    """Lê uma nota numérica informada pelo usuário."""
    while True:
        try:
            entrada = input(mensagem).strip().replace(",", ".")
            if not entrada:
                print("[!] A nota não pode ficar vazia.")
                continue
            return float(entrada)
        except ValueError:
            print("[!] Valor inválido. Digite apenas números, como 7.5 ou 7,5.")
        except (EOFError, KeyboardInterrupt):
            print("\n[!] Operação cancelada pelo usuário.")
            sys.exit(0)

def classificar_media(media: float) -> str:
    """Classifica o resultado final do aluno com base na média."""
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"

def main() -> None:
    """Função principal do programa."""
    print("--- Calculadora de Média Escolar ---")
    nota_1 = ler_nota("Digite a primeira nota: ")
    nota_2 = ler_nota("Digite a segunda nota: ")

    media = (nota_1 + nota_2) / 2
    situacao = classificar_media(media)

    print("-" * 40)
    print(f"[*] Nota 1:     {nota_1:.2f}")
    print(f"[*] Nota 2:     {nota_2:.2f}")
    print(f"[*] Média:      {media:.2f}")
    print(f"[*] Situação:   {situacao}")
    print("-" * 40)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
