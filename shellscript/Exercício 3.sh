#!/bin/bash

# 1. Captura apenas a hora atual (formato 00-23)
# O comando date +%H extrai apenas a hora do sistema
HORA=$(date +%H)

# 2. Lógica de saudação baseada no horário brasileiro padrão
# Manhã: 06:00 às 11:59
# Tarde: 12:00 às 17:59
# Noite: 18:00 às 05:59

if [ "$HORA" -ge 6 ] && [ "$HORA" -lt 12 ]; then
    echo "Bom dia! A hora atual é $HORA:$(date +%M)."
elif [ "$HORA" -ge 12 ] && [ "$HORA" -lt 18 ]; then
    echo "Boa tarde! A hora atual é $HORA:$(date +%M)."
else
    echo "Boa noite! A hora atual é $HORA:$(date +%M)."
fi