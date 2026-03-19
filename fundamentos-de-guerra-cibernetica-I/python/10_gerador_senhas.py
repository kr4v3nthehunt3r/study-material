"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 10_gerador_senhas.py
Descrição: Gera uma senha forte aleatória com no mínimo 12 caracteres.
"""

import random
import string


def gerar_senha(tamanho=12):
    """Gera uma senha forte contendo letras, números e símbolos."""
    # Define os grupos de caracteres permitidos.
    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = "!@#$%"

    # Garante ao menos um caractere de cada grupo obrigatório.
    senha = [
        random.choice(minusculas),
        random.choice(maiusculas),
        random.choice(numeros),
        random.choice(simbolos),
    ]

    # Junta todos os grupos para completar o restante da senha.
    todos_caracteres = minusculas + maiusculas + numeros + simbolos

    # Adiciona caracteres aleatórios até atingir o tamanho desejado.
    while len(senha) < tamanho:
        senha.append(random.choice(todos_caracteres))

    # Embaralha a lista para não deixar padrão previsível.
    random.shuffle(senha)

    # Retorna a senha final em formato de texto.
    return "".join(senha)


def main():
    """Função principal do programa."""
    # Gera e exibe uma nova senha forte a cada execução.
    print(f"Senha gerada: {gerar_senha(12)}")


# Executa o programa diretamente.
if __name__ == "__main__":
    main()
