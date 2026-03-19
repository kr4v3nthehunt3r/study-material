"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 13_validacao_ipv4.py
Descrição: Valida se uma string representa um endereço IPv4 válido.
"""


def validar_ipv4(ip):
    """Retorna True se a string informada for um IPv4 válido."""
    # Divide o IP pelo caractere ponto para obter os octetos.
    partes = ip.split('.')

    # Um IPv4 válido precisa ter exatamente 4 partes.
    if len(partes) != 4:
        return False

    # Valida cada octeto individualmente.
    for parte in partes:
        # Cada parte deve conter apenas dígitos.
        if not parte.isdigit():
            return False

        # Converte a parte para inteiro.
        valor = int(parte)

        # O valor de cada octeto deve estar entre 0 e 255.
        if valor < 0 or valor > 255:
            return False

    # Se todas as verificações forem aprovadas, o IP é válido.
    return True


def main():
    """Função principal do programa."""
    # Lê a string que será validada como IPv4.
    ip = input("Digite um endereço IPv4: ").strip()

    # Exibe o resultado da validação.
    if validar_ipv4(ip):
        print("Válido")
    else:
        print("Inválido")


# Executa o script diretamente.
if __name__ == "__main__":
    main()
