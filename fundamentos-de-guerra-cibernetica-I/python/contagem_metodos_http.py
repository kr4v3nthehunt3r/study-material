"""
Autor: Kr4v3n
Arquivo: contagem_metodos_http.py

Descrição do módulo:
    Este módulo realiza a contagem de métodos HTTP a partir de duas fontes:
    1. Uma lista simples de métodos já extraídos;
    2. Linhas simuladas de log no formato "MÉTODO CAMINHO STATUS".

Objetivos:
    - Contar a frequência de métodos HTTP;
    - Exibir um ranking completo de ocorrência;
    - Mostrar os métodos mais utilizados;
    - Extrair métodos HTTP a partir de linhas de log.
"""

# Importa a classe Counter da biblioteca collections.
# Ela é utilizada para contar automaticamente a quantidade
# de vezes que cada elemento aparece em uma lista.
from collections import Counter

def contar_metodos(lista_metodos):
    """
    Conta a quantidade de ocorrências de cada método HTTP.

    Parâmetros:
        lista_metodos (list): Lista contendo métodos HTTP, como
        GET, POST, PUT e DELETE.

    Retorno:
        Counter: Objeto com a contagem de cada método encontrado.
    """
    return Counter(lista_metodos)

def exibir_ranking(contagem):
    """
    Exibe o ranking completo dos métodos HTTP encontrados,
    em ordem decrescente de frequência.

    Parâmetros:
        contagem (Counter): Objeto Counter com a frequência
        dos métodos HTTP.

    Retorno:
        None
    """
    print("Ranking de métodos encontrados:")
    for metodo, total in contagem.most_common():
        print(f"Método: {metodo:<8} | Ocorrências: {total}")

def exibir_top_metodos(contagem, quantidade=2):
    """
    Exibe os métodos HTTP mais frequentes.

    Parâmetros:
        contagem (Counter): Objeto Counter com a frequência
        dos métodos HTTP.
        quantidade (int): Número de métodos mais frequentes
        que serão exibidos. O valor padrão é 2.

    Retorno:
        None
    """
    top_metodos = contagem.most_common(quantidade)

    print(f"Os {quantidade} métodos mais utilizados são:")
    for metodo, total in top_metodos:
        print(f"{metodo}: {total}")

def extrair_metodos_de_logs(linhas_log):
    """
    Extrai o método HTTP de cada linha de log.

    Observação:
        Este processamento considera que cada linha está no formato:
        "MÉTODO CAMINHO STATUS"

    Parâmetros:
        linhas_log (list): Lista de strings representando linhas de log.

    Retorno:
        list: Lista contendo apenas os métodos HTTP extraídos.
    """
    return [linha.split()[0] for linha in linhas_log if linha.strip()]

def main():
    """
    Função principal do programa.

    Responsabilidades:
        - Simular uma lista de métodos HTTP;
        - Contar e exibir o ranking desses métodos;
        - Exibir os métodos mais frequentes;
        - Simular linhas de log;
        - Extrair métodos das linhas de log;
        - Contar e exibir o resultado final.

    Retorno:
        None
    """
    # Simula uma lista de métodos HTTP já extraídos de outra fonte.
    metodos = ["GET", "GET", "POST", "PUT", "GET", "POST", "DELETE", "GET", "POST"]

    # Faz a contagem dos métodos presentes na lista.
    contagem = contar_metodos(metodos)

    # Exibe o ranking completo dos métodos encontrados.
    exibir_ranking(contagem)

    print("-" * 30)

    # Exibe apenas os 2 métodos mais frequentes.
    exibir_top_metodos(contagem, 2)

    print("-" * 30)

    # Simula linhas de log no formato: MÉTODO CAMINHO STATUS
    linhas_log = [
        "GET /home 200",
        "POST /login 302",
        "GET /produtos 200",
        "GET /contato 200",
        "POST /login 401",
        "GET /home 200"
    ]

    # Extrai apenas os métodos HTTP das linhas de log.
    lista_metodos = extrair_metodos_de_logs(linhas_log)

    # Conta os métodos encontrados nas linhas de log.
    contagem_final = contar_metodos(lista_metodos)

    # Exibe o resultado final da análise dos logs.
    print("Análise final de métodos no log:")
    for metodo, total in contagem_final.most_common():
        print(f"{metodo}: {total}")

# Garante que a função principal só será executada
# quando este arquivo for executado diretamente.
if __name__ == "__main__":
    main()