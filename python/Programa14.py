# Programa14.py
def converte_data(iso: str) -> str:
    partes = iso.split('-')
    if len(partes) != 3:
        raise ValueError("Formato inválido. Use AAAA-MM-DD")
    ano, mes, dia = partes
    if not (ano.isdigit() and mes.isdigit() and dia.isdigit()):
        raise ValueError("Formato inválido. Componentes devem ser numéricos")
    # validações simples de intervalo
    a, m, d = int(ano), int(mes), int(dia)
    if m < 1 or m > 12 or d < 1 or d > 31:
        raise ValueError("Data inválida")
    return f"{dia:02d}/{mes:02d}/{ano:04d}"

if __name__ == "__main__":
    entrada = input("Digite a data (AAAA-MM-DD): ").strip()
    try:
        print(converte_data(entrada))
    except ValueError as e:
        print("Erro:", e)
