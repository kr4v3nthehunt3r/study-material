#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Arquivo: registrar_nascimento.py
Descrição do módulo:
    Solicita e valida uma data de nascimento com apoio do módulo datetime.

Objetivo:
    Disponibilizar uma versão revisada, padronizada e comentada em
    português do Brasil, com foco em legibilidade, estudo e manutenção.
"""

import sys
from datetime import date

def ler_inteiro(mensagem: str) -> int:
    """Lê um número inteiro da entrada padrão."""
    try:
        entrada = input(mensagem).strip()
        if not entrada:
            raise ValueError("Campo vazio.")
        return int(entrada)
    except ValueError as erro:
        raise ValueError(f"Entrada inválida: {erro}") from erro

def validar_data_nascimento(dia: int, mes: int, ano: int) -> date:
    """Valida a data informada e retorna um objeto date."""
    data = date(ano, mes, dia)
    if data > date.today():
        raise ValueError("A data de nascimento não pode estar no futuro.")
    return data

def main() -> None:
    """Função principal."""
    print("--- Registro de Data de Nascimento ---")
    try:
        dia = ler_inteiro("Dia: ")
        mes = ler_inteiro("Mês: ")
        ano = ler_inteiro("Ano: ")
        data_nascimento = validar_data_nascimento(dia, mes, ano)
        print("-" * 40)
        print(f"[*] Data registrada: {data_nascimento.strftime('%d/%m/%Y')}")
        print("-" * 40)
    except ValueError as erro:
        print(f"[-] Erro de validação: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)

# Executa o módulo apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
