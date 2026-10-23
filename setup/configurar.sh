#!/bin/bash
echo "=== Configurando Assimila - BOT ==="

# Navega para a raiz do projeto (um nível acima de iniciadores)
cd "$(dirname "$0")/.."

#cria o ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual (venv)..."
    python3 -m venv venv
fi

#ativa o ambiente e instala dependências
echo "Instalando bibliotecas necessárias..."
source venv/bin/activate
pip install -r setup/requirements.txt

echo "=== Configuração concluída! Lembre-se de editar o .env com seu TOKEN. ==="
