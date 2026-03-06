"""
Exercício 5: Processamento de Notas
"""

def processar_notas():
    """
    Lê um número indeterminado de notas, processa e exibe estatísticas.
    O programa encerra quando o usuário digita -1.
    """
    notas = []
    print("--- Processador de Notas ---")
    print("Digite as notas uma a uma. Para finalizar, digite -1.")

    while True:
        try:
            entrada = input("Digite uma nota: ")
            nota = float(entrada)

            if nota == -1:
                break
            
            notas.append(nota)

        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

    print("\n" + "="*25)
    if not notas:
        print("Nenhuma nota foi inserida.")
    else:
        # a) Mostra a quantidade de valores lidos
        print(f"Quantidade: {len(notas)}")

        # b) Exibe todos os valores na ordem informada
        # A função print com * desempacota a lista
        print("Ordem direta:", *notas)

        # c) Exibe todos os valores em ordem inversa
        print("Ordem inversa:")
        for nota in reversed(notas):
            print(nota)

        # d) Calcula e mostra a soma dos valores
        soma = sum(notas)
        print(f"Soma: {soma}")

        # e) Calcula e mostra a média dos valores
        media = soma / len(notas)
        print(f"Média: {media:.2f}")

        # f) Calcula e mostra quantos valores estão acima da média
        acima_da_media = sum(1 for n in notas if n > media)
        print(f"Acima da média: {acima_da_media}")

    # g) Exibe mensagem de término
    print("Programa finalizado!")
    print("="*25)

if __name__ == "__main__":
    processar_notas()

