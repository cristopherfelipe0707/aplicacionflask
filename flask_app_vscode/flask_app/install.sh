#!/bin/bash

echo "=== Instalación Automática de la Aplicación Flask ==="
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"

# Verificar si pip está disponible
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 no está disponible"
    exit 1
fi

echo "✅ pip encontrado"

# Instalar dependencias
echo ""
echo "📦 Instalando dependencias de Flask..."
pip3 install -r requirements.txt

# Verificar la instalación
if [ $? -eq 0 ]; then
    echo "✅ Dependencias instaladas correctamente"
else
    echo "❌ Error al instalar dependencias"
    exit 1
fi

echo ""
echo "🎉 ¡Instalación completada!"
echo ""
echo "Para ejecutar la aplicación:"
echo "  python3 main.py"
echo ""
echo "Luego visita: http://localhost:5000"