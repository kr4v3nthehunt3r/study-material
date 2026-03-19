"""
Autor: Kr4v3n
Data de criação: 2026-03-16
Arquivo: 14_conversor_data.py
Descrição: Converte uma data do formato AAAA-MM-DD para DD/MM/AAAA.
"""

from datetime import datetime


def converter_data(data_texto):
    """Converte uma data de AAAA-MM-DD para DD/MM/AAAA."""
    # Interpreta a data recebida no formato ISO solicitado.
    data_objeto = datetime.strptime(data_texto, "%Y-%m-%d")

    # Retorna a data formatada no padrão brasileiro.
    return data_objeto.strftime("%d/%m/%Y")


def main():
    """Função principal do programa."""
    # Solicita a data ao usuário.
    data_texto = input("Entrada: ").strip()

    try:
        # Tenta converter e exibir a data formatada.
        print(f"Saída: {converter_data(data_texto)}")
    except ValueError:
        # Informa se a data digitada estiver em formato inválido.
        print("Data inválida. Use o formato AAAA-MM-DD.")


# Inicia a execução do script.
if __name__ == "__main__":
    main()
