"""
Autor: Kr4v3n
Arquivo: leitura_contagem.py

Descrição do módulo:
    Este módulo realiza a leitura de um arquivo de texto linha por linha,
    exibindo apenas as linhas não vazias e contabilizando quantas linhas
    válidas foram encontradas durante o processamento.

Objetivos:
    - Abrir um arquivo de texto com codificação UTF-8;
    - Ignorar linhas vazias;
    - Exibir as linhas não vazias na tela;
    - Contar a quantidade de linhas não vazias;
    - Tratar erros de arquivo não encontrado e outras exceções.
"""

def ler_e_contar_linhas(caminho_arquivo):
    """
    Lê um arquivo de texto, exibe as linhas não vazias e retorna
    a quantidade total de linhas válidas encontradas.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo que será lido.

    Retorno:
        int: Quantidade de linhas não vazias encontradas no arquivo.

    Exceções:
        FileNotFoundError: Disparada quando o arquivo não é encontrado.
        Exception: Disparada para outros erros inesperados durante a leitura.
    """
    contador = 0

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Remove espaços em branco no início e no fim,
            # além da quebra de linha.
            linha = linha.strip()

            # Ignora linhas vazias.
            if not linha:
                continue

            # Exibe a linha válida e incrementa o contador.
            print(linha)
            contador += 1

    return contador

def main():
    """
    Função principal do programa.

    Responsabilidades:
        - Definir o caminho do arquivo que será lido;
        - Chamar a função de leitura e contagem;
        - Exibir o total de linhas não vazias;
        - Tratar possíveis erros durante a execução.

    Retorno:
        None
    """
    caminho_arquivo = "teste.log"

    try:
        total_linhas = ler_e_contar_linhas(caminho_arquivo)

        print("-" * 30)
        print(f"Total de linhas não vazias: {total_linhas}")

    except FileNotFoundError:
        print(f"Erro: o arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as erro:
        print(f"Ocorreu um erro ao ler o arquivo: {erro}")

# Garante que a função principal só será executada
# quando este arquivo for executado diretamente.
if __name__ == "__main__":
    main()