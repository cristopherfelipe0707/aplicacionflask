#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de pruebas para verificar la funcionalidad de la aplicación Flask
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Probar que se pueden importar las librerías"""
    try:
        from flask import Flask
        print("✅ Flask importado correctamente")
        return True
    except ImportError as e:
        print(f"❌ Error al importar Flask: {e}")
        return False

def test_app_structure():
    """Verificar que los archivos de la aplicación existen"""
    required_files = [
        'main.py',
        'templates/index.html',
        'templates/ejercicio1.html', 
        'templates/ejercicio2.html',
        'static/css/style.css',
        'requirements.txt'
    ]
    
    all_files_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} existe")
        else:
            print(f"❌ {file_path} no encontrado")
            all_files_exist = False
    
    return all_files_exist

def test_flask_routes():
    """Verificar que las rutas de Flask están definidas"""
    try:
        from main import app
        
        # Probar que las rutas existen
        with app.test_client() as client:
            routes = ['/', '/ejercicio1', '/ejercicio2']
            
            for route in routes:
                response = client.get(route)
                if response.status_code == 200:
                    print(f"✅ Ruta {route} funcional")
                else:
                    print(f"❌ Ruta {route} con problema (status: {response.status_code})")
                    return False
        
        return True
    except Exception as e:
        print(f"❌ Error al probar rutas: {e}")
        return False

def test_ejercicio1_logic():
    """Probar la lógica del Ejercicio 1"""
    from main import app
    
    with app.test_client() as client:
        # Probar caso aprobado
        response = client.post('/ejercicio1', data={
            'nota1': '50',
            'nota2': '60', 
            'nota3': '55',
            'asistencia': '80'
        })
        
        if b'Aprobado' in response.data:
            print("✅ Ejercicio 1: Caso aprobado funcional")
        else:
            print("❌ Ejercicio 1: Problema con caso aprobado")
            return False
        
        # Probar caso reprobado
        response = client.post('/ejercicio1', data={
            'nota1': '35',
            'nota2': '40',
            'nota3': '30', 
            'asistencia': '80'
        })
        
        if b'Reprobado' in response.data:
            print("✅ Ejercicio 1: Caso reprobado funcional")
        else:
            print("❌ Ejercicio 1: Problema con caso reprobado")
            return False
    
    return True

def test_ejercicio2_logic():
    """Probar la lógica del Ejercicio 2"""
    from main import app
    
    with app.test_client() as client:
        # Probar comparación de nombres
        response = client.post('/ejercicio2', data={
            'nombre1': 'Christopher',
            'nombre2': 'Ana',
            'nombre3': 'Roberto'
        })
        
        if b'Christopher' in response.data and b'11' in response.data:
            print("✅ Ejercicio 2: Comparación de nombres funcional")
        else:
            print("❌ Ejercicio 2: Problema con comparación")
            return False
    
    return True

def main():
    """Ejecutar todas las pruebas"""
    print("=== PRUEBAS DE LA APLICACIÓN FLASK ===\n")
    
    tests = [
        ("Importación de librerías", test_imports),
        ("Estructura de archivos", test_app_structure),
        ("Rutas de Flask", test_flask_routes),
        ("Lógica Ejercicio 1", test_ejercicio1_logic),
        ("Lógica Ejercicio 2", test_ejercicio2_logic)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
        else:
            print("Test falló")
    
    print(f"\n=== RESULTADO FINAL ===")
    print(f"Tests pasados: {passed}/{total}")
    
    if passed == total:
        print("🎉 ¡Todos los tests pasaron! La aplicación está lista.")
        return True
    else:
        print("⚠️  Algunos tests fallaron. Revisar la configuración.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)