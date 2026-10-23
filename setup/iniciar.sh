#!/bin/bash
# Navega para a raiz do projeto (um nível acima de iniciadores)
cd "$(dirname "$0")/.."

if [ ! -d "venv" ]; then
    echo "Ambiente virtual não encontrado. Execute primeiro: ./configurar.sh"
    exit 1
fi

source venv/bin/activate
python3 main/main.py