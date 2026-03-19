#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Kr4v3n
Descrição:
    Coleta a data de nascimento do usuário, aceitando mês em número ou nome.

Melhoria importante:
    - Corrige a inconsistência entre o prompt e a validação do mês.
"""

import re
import sys


MESES = {
    "1": "Janeiro",
    "01": "Janeiro",
    "2": "Fevereiro",
    "02": "Fevereiro",
    "3": "Março",
    "03": "Março",
    "4": "Abril",
    "04": "Abril",
    "5": "Maio",
    "05": "Maio",
    "6": "Junho",
    "06": "Junho",
    "7": "Julho",
    "07": "Julho",
    "8": "Agosto",
    "08": "Agosto",
    "9": "Setembro",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro",
    "janeiro": "Janeiro",
    "fevereiro": "Fevereiro",
    "março": "Março",
    "marco": "Março",
    "abril": "Abril",
    "maio": "Maio",
    "junho": "Junho",
    "julho": "Julho",
    "agosto": "Agosto",
    "setembro": "Setembro",
    "outubro": "Outubro",
    "novembro": "Novembro",
    "dezembro": "Dezembro",
}


def normalizar_mes(mes: str) -> str:
    """Converte o mês informado para uma forma padronizada."""
    chave = mes.strip().lower()
    if chave not in MESES:
        raise ValueError("Mês inválido. Use número de 1 a 12 ou nome do mês.")
    return MESES[chave]


def validar_data(dia: str, mes: str, ano: str) -> tuple[int, str, int]:
    """Valida dia, mês e ano e retorna os valores normalizados."""
    if not (dia and mes and ano):
        raise ValueError("Todos os campos devem ser preenchidos.")

    if not re.fullmatch(r"\d{1,2}", dia):
        raise ValueError("Dia inválido. Use 1 ou 2 dígitos.")

    if not re.fullmatch(r"\d{4}", ano):
        raise ValueError("Ano inválido. Use 4 dígitos.")

    dia_int = int(dia)
    ano_int = int(ano)
    mes_normalizado = normalizar_mes(mes)

    if not 1 <= dia_int <= 31:
        raise ValueError("Dia fora do intervalo permitido (1 a 31).")

    if not 1900 <= ano_int <= 2100:
        raise ValueError("Ano fora do intervalo permitido (1900 a 2100).")

    return dia_int, mes_normalizado, ano_int


def main() -> None:
    """Coleta e exibe a data de nascimento validada."""
    print("--- Registro de Data de Nascimento ---")

    try:
        dia = input("Dia de nascimento (ex.: 15): ").strip()
        mes = input("Mês de nascimento (ex.: Abril ou 04): ").strip()
        ano = input("Ano de nascimento (ex.: 1995): ").strip()

        dia_int, mes_normalizado, ano_int = validar_data(dia, mes, ano)

        print("-" * 38)
        print(f"Você nasceu no dia {dia_int} de {mes_normalizado} de {ano_int}.")
        print("-" * 38)

    except ValueError as erro:
        print(f"[-] Erro de validação: {erro}")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n[!] Operação cancelada.")
        sys.exit(0)


if __name__ == "__main__":
    main()
