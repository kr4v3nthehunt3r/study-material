"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 23_extrator_username.py
Descrição: Extrai o nome de usuário de um e-mail informado.
"""


def extrair_username(email):
    """Extrai e retorna o trecho antes do caractere @."""
    # Divide o e-mail no caractere @ e pega a primeira parte.
    return email.split('@')[0]


def main():
    """Função principal do programa."""
    # Solicita ao usuário o endereço de e-mail.
    email = input('Entrada: ').strip()

    # Verifica se o formato mínimo do e-mail foi informado corretamente.
    if '@' not in email:
        print('E-mail inválido.')
        return

    # Extrai o nome de usuário do e-mail.
    username = extrair_username(email)

    # Exibe o resultado final.
    print(f'Saída: {username}')


# Executa o script diretamente.
if __name__ == '__main__':
    main()
