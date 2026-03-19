"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 05_processamento_notas.py
Descrição: Lê um número indeterminado de notas até o usuário digitar -1 e exibe estatísticas.
"""


def ler_notas():
    """Lê notas do usuário até que o valor -1 seja digitado."""
    # Cria a lista que armazenará as notas válidas.
    notas = []

    # Mantém a leitura ativa até o critério de parada ser atendido.
    while True:
        nota = float(input("Digite uma nota: "))

        # Encerra a leitura quando o usuário digita -1.
        if nota == -1:
            break

        # Adiciona a nota válida à lista.
        notas.append(nota)

    # Retorna todas as notas informadas.
    return notas


def exibir_relatorio(notas):
    """Exibe o relatório completo com estatísticas das notas lidas."""
    # Verifica se ao menos uma nota foi informada.
    if not notas:
        print("Nenhuma nota válida foi informada.")
        print("Programa finalizado!")
        return

    # Calcula os principais indicadores solicitados.
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    acima_da_media = sum(1 for nota in notas if nota > media)

    # Exibe a quantidade de valores lidos.
    print(f"\nQuantidade: {quantidade}")

    # Exibe os valores na ordem original, separados por espaço.
    print("Ordem direta:", " ".join(str(nota) for nota in notas))

    # Exibe os valores em ordem inversa, um por linha.
    print("\nOrdem inversa:")
    for nota in reversed(notas):
        print(nota)

    # Exibe soma, média e quantidade acima da média.
    print(f"\nSoma: {soma}")
    print(f"Média: {media}")
    print(f"Acima da média: {acima_da_media}")
    print("Programa finalizado!")


def main():
    """Função principal do programa."""
    # Lê todas as notas digitadas pelo usuário.
    notas = ler_notas()

    # Exibe o relatório final com os dados coletados.
    exibir_relatorio(notas)


# Ponto de entrada do script.
if __name__ == "__main__":
    main()
