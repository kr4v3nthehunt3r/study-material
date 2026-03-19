"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 22_validador_senha.py
Descrição: Valida senhas com base em critérios de composição e tamanho.
"""

import re


def senha_valida(senha):
    """Retorna True se a senha atender a todos os critérios do exercício."""
    # Verifica se o tamanho está entre 6 e 12 caracteres.
    if not (6 <= len(senha) <= 12):
        return False

    # Verifica a presença de pelo menos uma letra minúscula.
    if not re.search(r'[a-z]', senha):
        return False

    # Verifica a presença de pelo menos uma letra maiúscula.
    if not re.search(r'[A-Z]', senha):
        return False

    # Verifica a presença de pelo menos um número.
    if not re.search(r'[0-9]', senha):
        return False

    # Verifica a presença de pelo menos um dos símbolos permitidos.
    if not re.search(r'[$#@]', senha):
        return False

    # Se passou por todas as verificações, a senha é válida.
    return True


def filtrar_senhas_validas(entrada):
    """Recebe uma entrada com senhas separadas por vírgula e retorna apenas as válidas."""
    # Divide a entrada em senhas individuais removendo espaços extras.
    senhas = [senha.strip() for senha in entrada.split(',')]

    # Filtra apenas as senhas que atendem aos critérios.
    return [senha for senha in senhas if senha_valida(senha)]


def main():
    """Função principal do programa."""
    # Recebe do usuário as senhas separadas por vírgula.
    entrada = input('Entrada: ')

    # Obtém somente as senhas válidas.
    validas = filtrar_senhas_validas(entrada)

    # Exibe o resultado no formato solicitado.
    print('Saída:', ','.join(validas))


# Inicia a execução do script.
if __name__ == '__main__':
    main()
