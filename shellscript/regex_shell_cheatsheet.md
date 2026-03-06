# Cheatsheet REGEX para Shell (Bash/grep/sed/awk) 
---

## 1) Dialetos (o que muda na prática)

| Ferramenta | Opção | Dialeto | Notas |
|---|---|---|---|
| `grep` | (padrão) | BRE | `+ ? \| ( )` normalmente exigem escape (`\+`, `\(`) |
| `grep -E` | `-E` | ERE | `+ ? \| ( ) {m,n}` funcionam “normal” |
| `sed` | (padrão) | BRE | Similar ao `grep` padrão |
| `sed -E` | `-E` | ERE | Preferível para regex modernas |
| `awk` | (padrão) | ERE | Bom para extrair/campos |
| `grep -P` | `-P` | PCRE | `\d \w \s`, lookarounds (se disponível) |
| Bash `[[ =~ ]]` | nativo | ERE | Capturas em `BASH_REMATCH[n]` |

**Dicas**
- Prefira **aspas simples**: `grep -E '...regex...' arquivo`
- Para **extração**: `grep -Eo 'REGEX'` (imprime só o match)

---

## 2) “Tijolinhos” (construtores)

| Conceito | Regex | Exemplo | Nota |
|---|---|---|---|
| Início / fim | `^` / `$` | `^root:` | Âncoras de linha |
| Qualquer char | `.` | `a.b` | Pode variar com newline |
| Classe numérica | `[0-9]` / `[[:digit:]]` | `[[:digit:]]+` | POSIX é mais portátil |
| Classe alfanum | `[[:alnum:]]` | `[[:alnum:]_]+` | Tokens comuns |
| Espaços | `[[:space:]]` | `^[[:space:]]+$` | Inclui tab |
| Negação | `[^...]` | `[^0-9]+` | “Qualquer coisa exceto” |
| 0+ / 1+ / opcional | `*` / `+` / `?` | `ab+` | ERE |
| Intervalo | `{m,n}` | `[0-9]{2,4}` | ERE |
| Alternação | `(a|b)` | `(http|https)` | ERE |
| Grupo | `( ... )` | `([0-9]+)` | Captura/agrupa |
| Literal | `\.` | `file\.txt` | Escapa metacaracteres |

---

## 3) Biblioteca de padrões compartilhados (use por ID)

| ID | Padrão | Regex (ERE) | Regex (PCRE) | Exemplo | Nota |
|---|---|---|---|---|---|
| SH-EMAIL | Email (prático) | `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]{2,}$` |  | `user@dominio.com.br` | Formato prático |
| SH-UUID | UUID (prático) | `^[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}$` |  | `d94f0c3a-1b2c-3d4e-5f60-1234567890ab` | Não força versão |
| SH-HEX32 | Hex 32 (MD5-like) | `^[A-Fa-f0-9]{32}$` |  | `72a589da586844d7f0818ce684948eea` | Útil p/ JA3/MD5 |
| SH-URLLINE | URL http/https (linha inteira) | `^https?://[^[:space:]]+$` |  | `https://exemplo.com/a?b=1` | Validação prática |
| SH-URLEXT | URL em texto (extração) | `https?://[^[:space:]"'\)\]]+` |  | `...https://exemplo.com/a...` | Para `grep -Eo` |
| SH-IPV4-S | IPv4 simples | `^([0-9]{1,3}[.]){3}[0-9]{1,3}$` |  | `192.168.1.10` | Não valida 0–255 |
| SH-IPV4-P | IPv4 estrito (0–255) |  | `^(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)$` | `8.8.8.8` | Requer `grep -P` |
| SH-PORT-S | Porta simples | `^[0-9]{1,5}$` |  | `443` | Não valida 0–65535 |
| SH-PORT-P | Porta estrita (0–65535) |  | `^(?:6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]?\d{1,4}|0)$` | `65535` | Requer `grep -P` |

---

## 4) Documentos brasileiros (formato)

> **Atenção:** geralmente valida **formato**, não **DV**.

| Documento / dado | Regex (ERE) | Ref ID | Exemplo | Nota |
|---|---|---|---|---|
| CPF (c/ ou s/ pontuação) | `^[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}-?[0-9]{2}$` |  | `123.456.789-09` | DV não validado |
| CNPJ (c/ ou s/ pontuação) | `^[0-9]{2}[.]?[0-9]{3}[.]?[0-9]{3}/?[0-9]{4}-?[0-9]{2}$` |  | `12.345.678/0001-95` | DV não validado |
| CEP | `^[0-9]{5}-?[0-9]{3}$` |  | `01310-000` |  |
| Telefone BR (fixo/cel, opcional +55) | `^([+]55)?[[:space:]]*[(]?[0-9]{2}[)]?[[:space:]]*9?[0-9]{4}-?[0-9]{4}$` |  | `+55 (11) 91234-5678` | Variações comuns |
| Placa antiga (ABC-1234) | `^[A-Za-z]{3}-?[0-9]{4}$` |  | `ABC-1234` |  |
| Placa Mercosul (ABC1D23) | `^[A-Za-z]{3}[0-9][A-Za-z0-9][0-9]{2}$` |  | `BRA1E23` |  |
| PIS/PASEP/NIT | `^[0-9]{3}[.]?[0-9]{5}[.]?[0-9]{2}-?[0-9]$` |  | `123.45678.90-1` | DV não validado |
| Título de eleitor (12 dígitos) | `^[0-9]{12}$` |  | `123456789012` | DV/UF não validado |
| RENAVAM (11 dígitos) | `^[0-9]{11}$` |  | `12345678901` | DV não validado |
| CNH (registro, 11 dígitos) | `^[0-9]{11}$` |  | `01234567890` | Só formato |
| CNS (Cartão SUS, 15 dígitos) | `^[0-9]{15}$` |  | `898001160000000` | DV tem regra |
| RG (padrão comum) | `^[0-9]{1,2}[.]?[0-9]{3}[.]?[0-9]{3}-?[0-9Xx]$` |  | `12.345.678-9` | Varia por UF |
| Processo CNJ (NUP) | `^[0-9]{7}-[0-9]{2}[.][0-9]{4}[.][0-9][.][0-9]{2}[.][0-9]{4}$` |  | `0000000-00.0000.0.00.0000` | Padrão CNJ |
| Chave fiscal 44 dígitos (NFe/CT-e/MDFe) | `^[0-9]{44}$` |  | `3524...` | Unificado (44) |
| Boleto: linha digitável 47 | `^[0-9]{47}$` |  | `2379...` | Bancário (formato) |
| Arrecadação: linha digitável 48 | `^[0-9]{48}$` |  | `8361...` | Convênios (formato) |
| PIX chave aleatória |  | SH-UUID | `d94f...` | Ver biblioteca |
| PIX chave email |  | SH-EMAIL | `user@dominio.com.br` | Ver biblioteca |
| IE (genérico, só formato) | `^[0-9]{8,14}$` |  | `110042490114` | Varia por UF |

---

## 5) Documentos internacionais (formato)

| Documento / dado | Regex (ERE) | Exemplo | Nota |
|---|---|---|---|
| US SSN | `^[0-9]{3}-?[0-9]{2}-?[0-9]{4}$` | `123-45-6789` | Formato |
| US EIN | `^[0-9]{2}-?[0-9]{7}$` | `12-3456789` | Formato |
| CA SIN | `^[0-9]{3}[[:space:]]?[0-9]{3}[[:space:]]?[0-9]{3}$` | `123 456 789` | Formato |
| UK NINO (simplificado) | `^[A-Za-z]{2}[0-9]{6}[A-Za-z]$` | `QQ123456C` | Simplificado |
| IBAN (genérico) | `^[A-Za-z]{2}[0-9]{2}[A-Za-z0-9]{11,30}$` | `GB82WEST12345698765432` | Sem checksum |
| SWIFT/BIC | `^[A-Za-z]{4}[A-Za-z]{2}[A-Za-z0-9]{2}([A-Za-z0-9]{3})?$` | `DEUTDEFF` | 8 ou 11 |
| VAT (EU genérico) | `^[A-Za-z]{2}[A-Za-z0-9]{8,12}$` | `DE123456789` | Varia por país |
| Passaporte (genérico) | `^[A-Za-z0-9]{6,9}$` | `A1234567` | Muito variável |

---

## 6) Consultas (URL, SQL, JSON, Mongo, GraphQL)

| Tipo | Regex (ERE) | Ref ID | Exemplo | Uso típico |
|---|---|---|---|---|
| Querystring (trecho) | `[?][^[:space:]#]+` |  | `?a=1&b=2` | Extrair query da URL |
| Par key=value (em URL) | `(^|[?&])[A-Za-z0-9._~-]+=[^&#[:space:]]*` |  | `&q=test` | Extrair params |
| Parâmetro `q=` | `(^|[?&])q=[^&#[:space:]]+` |  | `?q=login` | Busca em logs |
| SQL keywords (triagem) | `(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER|CREATE)[[:space:]]+` |  | `SELECT *` | Use `grep -Ei` |
| Comentário SQL (triagem) | `(--[[:space:]]|/[*].*[*]/)` |  | `-- comment` | Sinalizar comentários |
| JSON key:value (simples) | `"[^"]+"[[:space:]]*:[[:space:]]*("[^"]*"|[0-9]+|true|false|null)` |  | `"id": 10` | Parsing leve |
| Mongo operators (triagem) | `"\$[A-Za-z]+"[[:space:]]*:` |  | `"$gt": 10` | Sinaliza `$op` |
| GraphQL (triagem) | `(query|mutation|subscription)` |  | `mutation {}` | Use `grep -Ei` |
| URL (linha inteira) |  | SH-URLLINE | `https://exemplo.com/a?b=1` | Referência |
| URL (extração) |  | SH-URLEXT | `...https://exemplo...` | Referência |

---

## 7) Rede (endereços, hosts, portas, artefatos)

| Item | Regex (ERE) | Regex (PCRE) | Ref ID | Exemplo | Nota |
|---|---|---|---|---|---|
| IPv4 simples |  |  | SH-IPV4-S | `192.168.1.10` | Referência |
| IPv4 estrito (0–255) |  |  | SH-IPV4-P | `8.8.8.8` | PCRE |
| IPv4 em texto (extração) | `([0-9]{1,3}[.]){3}[0-9]{1,3}` |  |  | `...10.0.0.5...` | `grep -Eo` |
| CIDR v4 (simples) | `^([0-9]{1,3}[.]){3}[0-9]{1,3}/[0-9]{1,2}$` |  |  | `10.0.0.0/24` | Não limita /0–32 |
| CIDR v4 (0–32) |  | `^(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\/(?:3[0-2]|[12]?\d)$` |  | `192.168.0.0/16` | PCRE |
| Porta simples | `^[0-9]{1,5}$` |  | SH-PORT-S | `443` | Referência |
| Porta estrita (0–65535) |  |  | SH-PORT-P | `65535` | PCRE |
| IP:PORT (IPv4, prático) | `^([0-9]{1,3}[.]){3}[0-9]{1,3}:[0-9]{1,5}$` |  |  | `10.0.0.1:8080` | Porta não estrita |
| [IPv6]:PORT |  | `^\[(?:[0-9A-Fa-f:]+)\]:(?:6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]?\d{1,4}|0)$` |  | `[2001:db8::1]:443` | PCRE |
| IPv6 full (sem `::`) | `^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$` |  |  | `2001:0db8:...:0001` | Não cobre `::` |
| IPv6 com `::` (abrangente) |  | `^(?:[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){7}|(?:[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){0,6})?::(?:[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){0,6})?)$` |  | `2001:db8::1` | PCRE |
| MAC (:` ou `-`) | `^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$` |  |  | `aa:bb:cc:dd:ee:ff` |  |
| MAC Cisco (aabb.ccdd.eeff) | `^([0-9A-Fa-f]{4}[.]){2}[0-9A-Fa-f]{4}$` |  |  | `a1b2.c3d4.e5f6` |  |
| Hostname/FQDN (prático) | `^([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?[.])+[A-Za-z]{2,}$` |  |  | `api.exemplo.com.br` |  |
| Hostname:PORT (prático) | `^([A-Za-z0-9-]+[.])+[A-Za-z]{2,}:[0-9]{1,5}$` |  |  | `srv.local:8443` | Porta não estrita |
| ASN | `^AS[0-9]{1,10}$` |  |  | `AS15169` | BGP/OSINT |
| Privado 10/8 (prático) | `^10([.][0-9]{1,3}){3}$` |  |  | `10.1.2.3` | Não estrito |
| Privado 192.168/16 (prático) | `^192[.]168([.][0-9]{1,3}){2}$` |  |  | `192.168.0.2` |  |
| Loopback 127/8 | `^127([.][0-9]{1,3}){3}$` |  |  | `127.0.0.1` |  |
| Link-local 169.254/16 | `^169[.]254([.][0-9]{1,3}){2}$` |  |  | `169.254.10.20` |  |
| Interface Linux (heurística) | `^(lo|eth|ens|enp|wlan|wl|br|docker|tun|tap)[A-Za-z0-9._:-]*$` |  |  | `wlan0` | Parsing |
| URL (linha inteira) |  |  | SH-URLLINE | `https://exemplo.com/a` | Referência |
| URL (extração) |  |  | SH-URLEXT | `...https://exemplo...` | Referência |
| JA3 / MD5-like |  |  | SH-HEX32 | `72a589da...` | Referência |

---

## 8) Extração (padrões + comandos prontos)

| Extrair | Ref/Regex | Comando pronto | Observação |
|---|---|---|---|
| IPv4 em texto | `([0-9]{1,3}[.]){3}[0-9]{1,3}` | `grep -Eo '([0-9]{1,3}[.]){3}[0-9]{1,3}' arquivo` | Prático (não estrito) |
| URL em texto | **SH-URLEXT** | `grep -Eo 'https?://[^[:space:]"'\''\)\]]+' arquivo` | Evita fechar em `" ' ) ]` |
| Emails | **SH-EMAIL** | `grep -Eo '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]{2,}' arquivo` |  |
| Hash MD5-like | **SH-HEX32** | `grep -Eo '[A-Fa-f0-9]{32}' arquivo \| sort -u` | Útil p/ JA3/MD5 |
| UUID | **SH-UUID** | `grep -Eo '[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}' arquivo \| sort -u` |  |

---

## 9) Logs (atalhos úteis)

### 9.1 Nginx/Apache access.log (Combined)

| Tarefa | Regex/Ref | Comando | Nota |
|---|---|---|---|
| IPs únicos | (início) | `grep -Eo '^([0-9]{1,3}[.]){3}[0-9]{1,3}' access.log \| sort -u` | Prático |
| `METHOD PATH` | `"([A-Z]+) ([^"]+) HTTP/[^"]+"` | `sed -nE 's/.*"([A-Z]+) ([^"]+) HTTP\/[^"]+".*/\1 \2/p' access.log` | Extração robusta |
| Só PATH | `"([A-Z]+) ([^"]+) HTTP/[^"]+"` | `sed -nE 's/.*"[A-Z]+ ([^"]+) HTTP\/[^"]+".*/\1/p' access.log` | Inclui query |
| Só 4xx/5xx | `"[^"]+" ([45][0-9]{2}) ` | `grep -E '"[^"]+" ([45][0-9]{2}) ' access.log` | Triagem |

### 9.2 auth.log (SSH/sudo)

| Tarefa | Regex | Comando | Nota |
|---|---|---|---|
| Top IPs “Failed password” | `Failed password for( invalid user)? ... from IPV4` | `sed -nE 's/.*from (([0-9]{1,3}[.]){3}[0-9]{1,3}).*/\1/p' auth.log \| sort \| uniq -c \| sort -nr \| head` | Brute-force |
| Top usernames (fail) | `Failed password for( invalid user)? ([^ ]+) from` | `sed -nE 's/.*Failed password for( invalid user)? ([^ ]+) from.*/\2/p' auth.log \| sort \| uniq -c \| sort -nr \| head` | Alvos |

---

## 10) Nmap (oN/oG)

| Tarefa | Regex | Comando | Nota |
|---|---|---|---|
| Portas abertas (oN) | `^[0-9]+/(tcp|udp)[[:space:]]+open[[:space:]]+` | `grep -E '^[0-9]+/(tcp|udp)[[:space:]]+open[[:space:]]+' scan.nmap` | Linhas open |
| Compactar porta/serviço | `^([0-9]+/(tcp|udp)) ... open ... ([^[:space:]]+)` | `sed -nE 's/^([0-9]+\/(tcp|udp))[[:space:]]+open[[:space:]]+([^[:space:]]+).*/\1 \3/p' scan.nmap` |  |
| Portas abertas (oG aprox.) | `([0-9]+)\/open\/(tcp|udp)` | `grep -Eo '([0-9]+)\/open\/(tcp|udp)' scan.gnmap \| sed -E 's/\/open\///' \| sort -u` | Sai `80/tcp` |

---

## 11) Burp/ZAP (JSON/HAR + raw HTTP)

| Tarefa | Regex | Comando | Nota |
|---|---|---|---|
| URLs em HAR (`"url":"..."`) | `"url":"https?://[^"]+"` | `grep -Eo '"url":"https?://[^"]+"' export.har \| sed -E 's/^"url":"//;s/"$//' \| sort -u` | Melhor com JSON minificado |
| Request line (raw) | `^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)[[:space:]]+[^[:space:]]+` | `grep -En '^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)[[:space:]]+[^[:space:]]+' raw.txt` | Localiza requisições |
| Header Host (raw) | `^Host:[[:space:]]*[^[:space:]]+` | `grep -Ei '^Host:[[:space:]]*[^[:space:]]+' raw.txt \| sort -u` | Lista hosts |

---

