#!/bin/bash
if [ ! -d "venv" ]; then
    echo "Ambiente virtual não encontrado. Execute primeiro: ./configurar.sh"
    exit 1
fi

source venv/bin/activate
python main.py
