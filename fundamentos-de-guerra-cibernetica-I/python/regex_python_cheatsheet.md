# Regex para Python — Cheat Sheet 
---

## Uso rápido (`re`)

- Prefira **raw strings**: `r"..."`.
- Funções comuns: `re.search`, `re.findall`, `re.finditer`, `re.sub`, `re.fullmatch`.
- Flags comuns: `re.I` (ignorecase), `re.M` (multiline), `re.S` (dotall), `re.X` (verbose), `re.A` (ASCII).

---

## 1) Fundamentos (re)

| Tipo | O que faz | Regex |
|---|---|---|
| Classe | dígito / não dígito | `\\d / \\D` |
| Classe | word / não-word | `\\w / \\W` |
| Classe | espaço / não-espaço | `\\s / \\S` |
| Âncora | início / fim | `^ / $` |
| Âncora | início/fim absoluto | `\\A / \\Z` |
| Âncora | borda / não-borda de palavra | `\\b / \\B` |
| Quantificador | 0+ / 1+ / 0-1 | `a* / a+ / a?` |
| Quantificador | exato / mínimo / intervalo | `a{3} / a{3,} / a{3,7}` |
| Lazy | mínimo possível | `.*?` |
| Grupo | captura / não captura | `(abc) / (?:abc)` |
| Grupo | nomeado | `(?P<nome>abc)` |
| Referência | por índice / por nome | `\\1 / (?P=nome)` |
| Alternância | OU | `cat\|dog` |
| Lookaround | lookahead + / - | `foo(?=bar) / foo(?!bar)` |
| Lookaround | lookbehind + / - | `(?<=R\\$)\\s?\\d+ / (?<!admin)\\w+` |

---

## 2) Documentos Brasileiros (únicos)

| Cobre | O que pega | Regex (Python) |
|---|---|---|
| CPF (com máscara) | 000.000.000-00 | `r"\\b\\d{{3}}\\.\\d{{3}}\\.\\d{{3}}-\\d{{2}}\\b"` |
| CPF/CNH/PIS/NIS/RENAVAM (colide) | 11 dígitos | `r"\\b\\d{{11}}\\b"` |
| CPF (flexível) | com/sem pontuação | `r"\\b\\d{{3}}\\.?\\d{{3}}\\.?\\d{{3}}-?\\d{{2}}\\b"` |
| CNPJ (com máscara) | 00.000.000/0000-00 | `r"\\b\\d{{2}}\\.\\d{{3}}\\.\\d{{3}}/\\d{{4}}-\\d{{2}}\\b"` |
| CNPJ (flexível) | com/sem pontuação | `r"\\b\\d{{2}}\\.?\\d{{3}}\\.?\\d{{3}}/?\\d{{4}}-?\\d{{2}}\\b"` |
| CEP (com/sem hífen) | 00000-000 / 00000000 | `r"\\b\\d{{5}}-?\\d{{3}}\\b"` |
| Título de Eleitor | 12 dígitos | `r"\\b\\d{{12}}\\b"` |
| CNS (Cartão SUS) | 15 dígitos (com/sem espaços) | `r"\\b\\d{{3}}\\s?\\d{{4}}\\s?\\d{{4}}\\s?\\d{{4}}\\b"` |
| Processo CNJ (NUP) | 0000000-00.0000.0.00.0000 | `r"\\b\\d{{7}}-\\d{{2}}\\.\\d{{4}}\\.\\d\\.\\d{{2}}\\.\\d{{4}}\\b"` |
| RG (com contexto) | RG: ... | `r"(?i)\\bRG\\b\\s*[:\\-]?\\s*([0-9.\\-]{{6,14}}[0-9Xx])\\b"` |
| RG (formato comum) | pontos/hífen + dígito/X | `r"\\b\\d{{1,2}}\\.?\\d{{3}}\\.?\\d{{3}}-?[0-9Xx]\\b"` |
| CTPS (heurístico) | CTPS + número/série/UF | `r"(?i)\\bCTPS\\b\\s*[:\\-]?\\s*\\d{{5,8}}(?:\\s*[-/]\\s*\\d{{3}})?(?:\\s*[-/]\\s*[A-Z]{{2}})?\\b"` |
| Passaporte BR (heurístico) | 2 letras + 6 dígitos | `r"\\b[A-Z]{{2}}\\d{{6}}\\b"` |
| Inscrição Estadual (contexto) | IE ... | `r"(?i)\\bIE\\b\\s*[:\\-]?\\s*(\\d[\\d.\\-\\/]{{6,18}}\\d)\\b"` |
| OAB | OAB/SP 123456 | `r"(?i)\\bOAB\\s*[/\\-]?\\s*[A-Z]{{2}}\\s*\\d{{3,7}}[A-Za-z]?\\b"` |
| Registros Profissionais | CRM/CREA/CRP/COREN/CRF/CRO/CRMV/CRC | `r"(?i)\\b(?:CRM\|CREA\|CRP\|COREN\|CRF\|CRO\|CRMV\|CRC)\\s*[/\\-]?\\s*[A-Z]{{2}}\\s*\\d{{3,8}}\\b"` |
| NFe/Boleto (colide) | 44 dígitos | `r"\\b\\d{{44}}\\b"` |
| Placa Mercosul | ABC1D23 | `r"\\b[A-Z]{{3}}\\d[A-Z0-9]\\d{{2}}\\b"` |

---

## 3) Documentos Internacionais (únicos)

| Cobre | Região | Regex (Python) |
|---|---|---|
| SSN (com hífen) | EUA | `r"\\b\\d{{3}}-\\d{{2}}-\\d{{4}}\\b"` |
| SSN (sem hífen) | EUA | `r"\\b\\d{{9}}\\b"` |
| EIN | EUA | `r"\\b\\d{{2}}-\\d{{7}}\\b"` |
| NINO | Reino Unido | `r"\\b(?!BG)(?!GB)(?!NK)(?!KN)(?!TN)(?!NT)(?!ZZ)[A-CEGHJ-PR-TW-Z]{{2}}\\d{{6}}[A-D]\\b"` |
| SIN | Canadá | `r"\\b\\d{{3}}[- ]?\\d{{3}}[- ]?\\d{{3}}\\b"` |
| IBAN | Internacional | `r"\\b[A-Z]{{2}}\\d{{2}}[A-Z0-9]{{11,30}}\\b"` |
| SWIFT/BIC | Internacional | `r"\\b[A-Z]{{4}}[A-Z]{{2}}[A-Z0-9]{{2}}([A-Z0-9]{{3}})?\\b"` |
| VAT ID (genérico) | UE (varia) | `r"\\b[A-Z]{{2}}[A-Z0-9]{{8,12}}\\b"` |
| Aadhaar (formato) | Índia | `r"\\b\\d{{4}}\\s?\\d{{4}}\\s?\\d{{4}}\\b"` |
| Passaporte (heurístico) | Vários | `r"\\b[A-Z0-9]{{6,9}}\\b"` |

---

## 4) Web/HTTP + Consultas (unificada)

| Cobre | O que pega | Regex (Python) |
|---|---|---|
| Header genérico | Chave: valor | `r"(?m)^[A-Za-z0-9-]+:\\s*.+$"` |
| Authorization Bearer | header Bearer | `r"(?im)^authorization:\\s*bearer\\s+([^\\s]+)\\s*$"` |
| Authorization Basic | header Basic base64 | `r"(?im)^authorization:\\s*basic\\s+([A-Za-z0-9+/=]+)\\s*$"` |
| Cookie header | Cookie: ... | `r"(?im)^cookie:\\s*(.+)\\s*$"` |
| Set-Cookie header | Set-Cookie: ... | `r"(?im)^set-cookie:\\s*(.+)\\s*$"` |
| Sessão comum | PHP/JAVA/ASP.NET | `r"\\b(?:PHPSESSID\|JSESSIONID\|ASP\\.NET_SessionId)=([A-Za-z0-9._-]+)\\b"` |
| URL http/https | URL completa | `r"\\bhttps?://[^\\s\\\'\\\"<>]+"` |
| Path/endpoint | /api/v1/... | `r"(?<!\\w)(/[\\w\\-.~%]+(?:/[\\w\\-.~%]+)*)"` |
| Query string | após ? | `r"\\?([A-Za-z0-9._~%=&+-]+)"` |
| Par chave=valor | extração de pares | `r"(?i)\\b([a-z0-9_.-]+)=([^&#\\s]+)"` |
| Nomes sensíveis | token/password/etc. | `r"(?i)\\b(?:token\|apikey\|api[_-]?key\|secret\|password\|passwd\|pwd\|auth\|session\|sid\|jwt)\\b"` |
| GraphQL | query/mutation | `r"(?is)\\b(query\|mutation)\\b\\s+\\w*\\s*\\("` |
| Indicadores SQL | SELECT/INSERT/UPDATE/DELETE | `r"(?is)\\b(select\|insert\|update\|delete)\\b\\s+.+?\\b(from\|into\|set)\\b"` |
| Comentário SQL | -- ou /* */ | `r"(?s)--.*?$\\\|/\\*.*?\\*/"` |
| JSON (heurístico) | bloco {...} | `r"(?s)\\{{.*?\\}}"` |

---

## 5) Segredos / Tokens / Chaves / Infra

| Cobre | O que pega | Regex (Python) |
|---|---|---|
| JWT | 3 partes | `r"\\beyJ[a-zA-Z0-9_-]*\\.[a-zA-Z0-9_-]+\\.[a-zA-Z0-9_-]+\\b"` |
| Bearer token (texto) | bearer ... | `r"(?i)\\bbearer\\s+([A-Za-z0-9._~+/=-]{{10,}})"` |
| Secret genérico | secret/token/api_key=... | `r"(?i)\\b(secret\|token\|api[_-]?key\|access[_-]?key)\\b\\s*[:=]\\s*([A-Za-z0-9._~+/=-]{{8,}})"` |
| AWS Access Key ID | AKIA... | `r"\\bAKIA[0-9A-Z]{{16}}\\b"` |
| AWS Secret (por nome) | aws_secret_access_key=... | `r"(?i)\\baws_secret_access_key\\b\\s*[:=]\\s*([A-Za-z0-9/+=]{{40}})"` |
| Google API Key | AIza... | `r"\\bAIza[0-9A-Za-z\\-_]{{35}}\\b"` |
| Slack token | xox... | `r"\\bxox[baprs]-[0-9A-Za-z-]{{10,}}\\b"` |
| GitHub token classic | ghp_... | `r"\\bghp_[A-Za-z0-9]{{36}}\\b"` |
| GitHub fine-grained | github_pat_... | `r"\\bgithub_pat_[A-Za-z0-9_]{{20,}}\\b"` |
| Stripe secret | sk_live/test_... | `r"\\bsk_(?:live\|test)_[0-9a-zA-Z]{{16,}}\\b"` |
| Stripe publishable | pk_live/test_... | `r"\\bpk_(?:live\|test)_[0-9a-zA-Z]{{16,}}\\b"` |
| Twilio API Key | SK... | `r"\\bSK[0-9a-fA-F]{{32}}\\b"` |
| Mailgun key | key-... | `r"\\bkey-[0-9a-fA-F]{{32}}\\b"` |
| SendGrid key | SG.xxx.yyy | `r"\\bSG\\.[A-Za-z0-9_-]{{10,}}\\.[A-Za-z0-9_-]{{10,}}\\b"` |
| Private key PEM | BEGIN ... PRIVATE KEY | `r"-----BEGIN (?:RSA \|EC \|DSA \|OPENSSH )?PRIVATE KEY-----"` |
| Cert PEM | BEGIN CERTIFICATE | `r"-----BEGIN CERTIFICATE-----"` |
| MongoDB URI | mongodb:// | `r"\\bmongodb(?:\\+srv)?:\\/\\/[^\\s\\\'\\\"<>]+"` |
| Postgres URI | postgres:// | `r"\\bpostgres(?:ql)?:\\/\\/[^\\s\\\'\\\"<>]+"` |
| MySQL URI | mysql:// | `r"\\bmysql:\\/\\/[^\\s\\\'\\\"<>]+"` |
| Redis URI | redis:// | `r"\\bredis:\\/\\/[^\\s\\\'\\\"<>]+"` |
| AMQP URI | amqp(s):// | `r"\\bamqps?:\\/\\/[^\\s\\\'\\\"<>]+"` |
| Connection string genérica | dsn/uri/connection_string | `r"(?i)\\b(?:uri\|dsn\|connection(?:_string)?)\\b\\s*[:=]\\s*([^\\s\\\'\\\";#]+)"` |
| Dockerfile ENV | ENV VAR=... | `r"(?im)^\\s*ENV\\s+([A-Za-z_][A-Za-z0-9_]*)\\s*=\\s*(.+)\\s*$"` |
| Shell export | export VAR=... | `r"(?im)^\\s*export\\s+([A-Za-z_][A-Za-z0-9_]*)=(.+)\\s*$"` |
| K8s Secret data (heurístico) | bloco data: base64 | `r"(?ms)^\\s*data:\\s*\\n(?:\\s+[A-Za-z0-9_.-]+:\\s*[A-Za-z0-9+/=]+\\s*\\n)+"` |

---

## 6) IDs / Hashes + Indicadores

| Cobre | O que pega | Regex (Python) |
|---|---|---|
| MD5 | 32 hex | `r"\\b[a-fA-F0-9]{{32}}\\b"` |
| SHA1 | 40 hex | `r"\\b[a-fA-F0-9]{{40}}\\b"` |
| SHA256 | 64 hex | `r"\\b[a-fA-F0-9]{{64}}\\b"` |
| UUID | 8-4-4-4-12 | `r"\\b[0-9a-fA-F]{{8}}-[0-9a-fA-F]{{4}}-[0-9a-fA-F]{{4}}-[0-9a-fA-F]{{4}}-[0-9a-fA-F]{{12}}\\b"` |
| CVE | CVE-YYYY-NNNN... | `r"\\bCVE-\\d{{4}}-\\d{{4,7}}\\b"` |
| Erros SQL (heurístico) | MySQL/Oracle/Postgres/ODBC | `r"(?i)\\b(SQL syntax\|mysql_fetch\|ORA-\\d{{4,5}}\|PostgreSQL.*ERROR\|SQLite\\/JDBCDriver\|ODBC SQL Server\|SQLSTATE)\\b"` |
| Stack trace Python | Traceback ... | `r"(?m)^Traceback \\(most recent call last\\):"` |
| Caminho Windows | C:\... | `r"\\b[A-Za-z]:\\\\(?:[^\\\\\\r\\n]+\\\\)*[^\\\\\\r\\n]*\\b"` |
| Caminho Linux | /var/log/... | `r"(?<!\\w)/(?:[\\w\\-.]+/)*[\\w\\-.]+"` |
| Log de falha (heurístico) | error/warn/denied etc. | `r"(?i)\\b(error\|warn\|failed\|denied\|unauthorized\|forbidden\|exception)\\b"` |

---

## 7) Rede (IPs / MAC / Portas / Hostnames)

| Cobre | O que pega | Regex (Python) |
|---|---|---|
| IPv4 válido (0–255) | IP | `r"\\b(?:(?:25[0-5]\|2[0-4]\\d\|1?\\d?\\d)\\.){{3}}(?:25[0-5]\|2[0-4]\\d\|1?\\d?\\d)\\b"` |
| IPv4 CIDR | x.x.x.x/0-32 | `r"\\b(?:(?:25[0-5]\|2[0-4]\\d\|1?\\d?\\d)\\.){{3}}(?:25[0-5]\|2[0-4]\\d\|1?\\d?\\d)\\/(?:[0-9]\|[12]\\d\|3[0-2])\\b"` |
| IPv4 privado 10/8 | 10.x.x.x | `r"\\b10\\.(?:(?:25[0-5]\|2[0-4]\\d\|1?\\d?\\d)\\.){{2}}(?:25[0-5]\|2[0-4]\\d\|1?\\d?\\d)\\b"` |
| IPv4 privado 172.16–31 | 172.16..172.31 | `r"\\b172\\.(?:1[6-9]\|2\\d\|3[01])\\.(?:\\d{{1,3}})\\.(?:\\d{{1,3}})\\b"` |
| IPv4 privado 192.168/16 | 192.168.x.x | `r"\\b192\\.168\\.(?:\\d{{1,3}})\\.(?:\\d{{1,3}})\\b"` |
| IPv4 loopback | 127.x.x.x | `r"\\b127\\.(?:\\d{{1,3}}\\.){{2}}\\d{{1,3}}\\b"` |
| IPv4 link-local | 169.254.x.x | `r"\\b169\\.254\\.(?:\\d{{1,3}})\\.(?:\\d{{1,3}})\\b"` |
| IPv4 multicast | 224–239.* | `r"\\b(?:22[4-9]\|23\\d)\\.(?:\\d{{1,3}}\\.){{2}}\\d{{1,3}}\\b"` |
| Range IPv4 com hífen | a-b | `r"\\b\\d{{1,3}}(?:\\.\\d{{1,3}}){{3}}\\s*-\\s*\\d{{1,3}}(?:\\.\\d{{1,3}}){{3}}\\b"` |
| IPv6 (heurístico) | IPv6 | `r"\\b(?:[A-Fa-f0-9]{{1,4}}:){{2,7}}[A-Fa-f0-9]{{1,4}}\\b"` |
| IPv6 CIDR (heurístico) | ::/0-128 | `r"\\b(?:[A-Fa-f0-9]{{0,4}}:){{2,7}}[A-Fa-f0-9]{{0,4}}\\/(?:\\d\|[1-9]\\d\|1[01]\\d\|12[0-8])\\b"` |
| IPv6 link-local (heurístico) | fe80:: | `r"\\bfe80:(?::[A-Fa-f0-9]{{0,4}}){{2,7}}\\b"` |
| MAC (:) | AA:BB:... | `r"\\b(?:[0-9A-Fa-f]{{2}}:){{5}}[0-9A-Fa-f]{{2}}\\b"` |
| MAC (-) | AA-BB-... | `r"\\b(?:[0-9A-Fa-f]{{2}}-){{5}}[0-9A-Fa-f]{{2}}\\b"` |
| MAC Cisco (.) | aabb.ccdd.eeff | `r"\\b[0-9A-Fa-f]{{4}}\\.[0-9A-Fa-f]{{4}}\\.[0-9A-Fa-f]{{4}}\\b"` |
| Porta (0–65535) | número válido | `r"\\b(?:6553[0-5]\|655[0-2]\\d\|65[0-4]\\d{{2}}\|6[0-4]\\d{{3}}\|[1-5]\\d{{4}}\|\\d{{1,4}})\\b"` |
| Porta c/ protocolo | 80/tcp, 53/udp | `r"\\b(?:6553[0-5]\|655[0-2]\\d\|65[0-4]\\d{{2}}\|6[0-4]\\d{{3}}\|[1-5]\\d{{4}}\|\\d{{1,4}})\\/(?:tcp\|udp)\\b"` |
| Socket host:porta | host:443 | `r"\\b(?:[A-Za-z0-9.-]+\|\\d{{1,3}}(?:\\.\\d{{1,3}}){{3}}):\\d{{2,5}}\\b"` |
| Hostname (RFC-ish) | srv-01 | `r"\\b[a-zA-Z0-9](?:[a-zA-Z0-9-]{{0,61}}[a-zA-Z0-9])?\\b"` |
| FQDN/domínio | api.exemplo.com | `r"\\b(?:[A-Za-z0-9-]+\\.)+[A-Za-z]{{2,}}\\b"` |
| PTR reverse IPv4 | ...in-addr.arpa | `r"\\b(?:\\d{{1,3}}\\.){{4}}in-addr\\.arpa\\b"` |
| Netmask dotted | 255.255.255.0 | `r"\\b(?:(?:255\|254\|252\|248\|240\|224\|192\|128\|0)\\.){{3}}(?:255\|254\|252\|248\|240\|224\|192\|128\|0)\\b"` |
| VLAN ID | vlan 1..4094 | `r"(?i)\\bvlan\\b\\s*[:#]?\\s*(?:[1-9]\\d{{0,2}}\|[1-3]\\d{{3}}\|40[0-8]\\d\|409[0-4])\\b"` |
| ASN | AS12345 | `r"\\bAS\\d{{1,6}}\\b"` |
| UNC path | \\srv\share\... | `r"\\\\\\\\[A-Za-z0-9._-]+\\\\[A-Za-z0-9 $._-]+(?:\\\\[^\\r\\n\\\\]+)*"` |

---

