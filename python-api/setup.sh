#!/bin/bash
# Si no existe el entorno virtual, lo crea e instala las dependencias
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
    # Activa el entorno virtual y actualiza pip
    source venv/bin/activate
    pip install --upgrade pip
    echo "Instalando dependencias desde requirements.txt..."
    pip install --no-cache-dir -r requirements.txt
else
    echo "Entorno virtual ya existe, activando..."
    source venv/bin/activate
fi

echo "Setup completado."
