from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Página principal con menú de dos botones"""
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    """Ejercicio 1: Cálculo de promedio y estado académico"""
    resultado = None
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])
            
            # Validar rangos
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                resultado = "Error: Las notas deben estar entre 10 y 70"
            elif not (0 <= asistencia <= 100):
                resultado = "Error: La asistencia debe estar entre 0 y 100"
            else:
                # Calcular promedio
                promedio = (nota1 + nota2 + nota3) / 3
                
                # Determinar estado
                if promedio >= 40 and asistencia >= 75:
                    estado = "Aprobado"
                else:
                    estado = "Reprobado"
                
                resultado = {
                    'promedio': round(promedio, 2),
                    'asistencia': asistencia,
                    'estado': estado
                }
        except ValueError:
            resultado = "Error: Por favor ingrese valores numéricos válidos"
    
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    """Ejercicio 2: Comparación de nombres por cantidad de caracteres"""
    resultado = None
    if request.method == 'POST':
        try:
            # Obtener nombres del formulario
            nombre1 = request.form['nombre1'].strip()
            nombre2 = request.form['nombre2'].strip()
            nombre3 = request.form['nombre3'].strip()
            
            # Validar que no estén vacíos
            if not nombre1 or not nombre2 or not nombre3:
                resultado = "Error: Todos los nombres deben ser ingresados"
            else:
                # Crear lista de tuplas (nombre, cantidad_caracteres)
                nombres = [
                    (nombre1, len(nombre1)),
                    (nombre2, len(nombre2)),
                    (nombre3, len(nombre3))
                ]
                
                # Encontrar el nombre con más caracteres
                nombre_mas_largo = max(nombres, key=lambda x: x[1])
                
                resultado = {
                    'nombres': [nombre1, nombre2, nombre3],
                    'nombre_mas_largo': nombre_mas_largo[0],
                    'cantidad_caracteres': nombre_mas_largo[1]
                }
        except Exception as e:
            resultado = f"Error: {str(e)}"
    
    return render_template('ejercicio2.html', resultado=resultado)

@app.route('/volver')
def volver():
    """Redirigir al inicio"""
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)