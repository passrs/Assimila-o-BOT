@echo off
title Inicializador Assimila - BOT 
echo === Verificando configuracao do Bot ===

rem Navega para a raiz do projeto (um nível acima de iniciadores)
cd /d "%~dp0.."

rem verifica se possui o ambiente virtual .venv
if not exist venv ( 
    echo Criando ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate
    echo Instalando bibliotecas requeridas...
    pip install -r setup\requirements.txt
) else (
    call venv\Scripts\activate
)

echo Iniciando o bot...
python main\main.py
pause
