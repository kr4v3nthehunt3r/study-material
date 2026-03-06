# Programa13.py
def valida_ip_v4(ip: str) -> bool:
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for p in partes:
        if not p.isdigit():
            return False
        # evita octetos com zeros à esquerda inválidos como "01" se desejar; aqui permitimos "0" e "00" será considerado inválido
        if p != "0" and p.startswith("0"):
            return False
        val = int(p)
        if val < 0 or val > 255:
            return False
    return True

if __name__ == "__main__":
    ip = input("Digite um IP v4: ").strip()
    if valida_ip_v4(ip):
        print("Válido")
    else:
        print("Inválido")
