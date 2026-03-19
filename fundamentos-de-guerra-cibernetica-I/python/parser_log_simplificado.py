"""
Autor: Kr4v3n
Arquivo: parser_log_simplificado.py

Descrição do módulo:
    Este módulo realiza a análise simplificada de uma linha de log
    no formato Apache Combined Log. O objetivo é identificar e extrair
    informações específicas, como o endereço IP de origem, o código
    de status HTTP e o User-Agent do cliente.

Objetivos:
    - Compilar uma expressão regular para interpretar linhas de log;
    - Extrair campos relevantes de uma linha de acesso;
    - Exibir um relatório simplificado com os dados encontrados;
    - Informar quando a linha não corresponder ao padrão esperado.
"""

# Importa o módulo de expressões regulares.
# Ele será utilizado para definir e aplicar o padrão de parsing da linha de log.
import re

# Compila o padrão de log para melhorar o desempenho em múltiplas análises.
# Este padrão tenta capturar:
# 1. IP de origem
# 2. Data e hora da requisição
# 3. Método HTTP
# 4. Recurso solicitado e versão HTTP
# 5. Código de status HTTP
# 6. Quantidade de bytes retornados
# 7. Referer
# 8. User-Agent
PADRAO_LOG = re.compile(
    r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) ([^"]*)" (\d{3}) (\S+) "([^"]*)" "([^"]*)"'
)

def extrair_dados_log(linha_log):
    """
    Extrai informações relevantes de uma linha de log Apache.

    Parâmetros:
        linha_log (str): Linha de log que será analisada.

    Retorno:
        dict | None:
            - Retorna um dicionário com os campos extraídos caso a linha
              corresponda ao padrão esperado;
            - Retorna None caso a linha não seja compatível com o padrão.
    """
    correspondencia = PADRAO_LOG.match(linha_log)

    if not correspondencia:
        return None

    return {
        "host": correspondencia.group(1),
        "data": correspondencia.group(2),
        "metodo": correspondencia.group(3),
        "recurso": correspondencia.group(4),
        "status": correspondencia.group(5),
        "bytes": correspondencia.group(6),
        "referer": correspondencia.group(7),
        "user_agent": correspondencia.group(8),
    }

def exibir_relatorio(dados_log):
    """
    Exibe um relatório simplificado com os principais dados extraídos do log.

    Parâmetros:
        dados_log (dict): Dicionário contendo os dados extraídos da linha de log.

    Retorno:
        None
    """
    print("--- Relatório Simplificado ---")
    print(f"Host:       {dados_log['host']}")
    print(f"Status:     {dados_log['status']}")
    print(f"User-Agent: {dados_log['user_agent']}")

def main():
    """
    Função principal do programa.

    Responsabilidades:
        - Definir uma linha de log de exemplo;
        - Executar a extração dos dados;
        - Exibir o relatório simplificado quando houver sucesso;
        - Informar quando a linha não corresponder ao padrão esperado.

    Retorno:
        None
    """
    # Exemplo de linha real simulando acesso por dispositivo móvel.
    linha_real = (
        '191.185.15.120 - - [04/Mar/2026:12:45:01 +0000] '
        '"GET /api/v1/products HTTP/1.1" 200 1542 "-" '
        '"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) '
        'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 '
        'Mobile/15E148 Safari/604.1"'
    )

    # Tenta extrair os dados da linha informada.
    dados_log = extrair_dados_log(linha_real)

    # Exibe o relatório caso a linha seja válida.
    if dados_log:
        exibir_relatorio(dados_log)
    else:
        print("A linha não condiz com o padrão esperado.")

# Garante que a função principal será executada apenas
# quando este arquivo for chamado diretamente.
if __name__ == "__main__":
    main()