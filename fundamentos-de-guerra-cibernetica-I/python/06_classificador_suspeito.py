"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 06_classificador_suspeito.py
Descrição: Classifica uma pessoa conforme respostas a cinco perguntas sobre um crime.
"""


def coletar_respostas(perguntas):
    """Coleta respostas do usuário usando uma lista de perguntas."""
    # Cria a lista onde serão armazenadas as respostas válidas.
    respostas = []

    # Percorre cada pergunta da lista.
    for pergunta in perguntas:
        while True:
            resposta = input(f"{pergunta} (s/n): ").strip().lower()

            # Aceita apenas as respostas 's' ou 'n'.
            if resposta in ("s", "n"):
                respostas.append(resposta)
                break

            # Informa ao usuário que a resposta digitada é inválida.
            print("Resposta inválida. Digite apenas 's' para sim ou 'n' para não.")

    # Retorna a lista com todas as respostas coletadas.
    return respostas


def classificar_suspeito(respostas):
    """Classifica a pessoa com base na quantidade de respostas positivas."""
    # Conta quantas respostas foram 'sim'.
    quantidade_sim = respostas.count("s")

    # Aplica a regra de classificação descrita no exercício.
    if quantidade_sim == 2:
        return "Suspeita"
    if 3 <= quantidade_sim <= 4:
        return "Cúmplice"
    if quantidade_sim == 5:
        return "Assassino"
    return "Inocente"


def main():
    """Função principal do programa."""
    # Lista com as cinco perguntas do exercício.
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?",
    ]

    # Coleta as respostas do usuário.
    respostas = coletar_respostas(perguntas)

    # Classifica o suspeito a partir das respostas coletadas.
    classificacao = classificar_suspeito(respostas)

    # Exibe o resultado final.
    print(f"Classificação: {classificacao}")


# Inicia a execução do programa.
if __name__ == "__main__":
    main()
