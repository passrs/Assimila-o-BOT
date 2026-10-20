@echo off
title Bot Discord - Inicializador
echo === Verificando configuracao do Bot ===

if not exist venv (
    echo Criando ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate
    echo Instalando bibliotecas requeridas...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

echo Iniciando o bot...
python main.py
pause
