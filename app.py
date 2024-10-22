from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'patitoxd'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        datos = {
            'nombre': request.form['nombre'],
            'apellidos': request.form['apellidos'],
            'curso': request.form['curso']
        }
        session['datos_inscripcion_curso'] = datos
        return redirect(url_for('mostrar_datos', formulario='inscripcion_curso'))
    return render_template('inscripcion_curso.html')

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        datos = {
            'nombre': request.form['nombre'],
            'apellidos': request.form['apellidos'],
            'email': request.form['email'],
            'contrasena': request.form['contrasena']
        }
        session['datos_registro_usuario'] = datos
        return redirect(url_for('mostrar_datos', formulario='registro_usuario'))
    return render_template('registro_usuario.html')

@app.route('/registro_producto', methods=['GET', 'POST'])
def registro_producto():
    if request.method == 'POST':
        datos = {
            'producto': request.form['producto'],
            'categoria': request.form['categoria'],
            'existencia': request.form['existencia'],
            'precio': request.form['precio']
        }
        session['datos_registro_producto'] = datos
        return redirect(url_for('mostrar_datos', formulario='registro_producto'))
    return render_template('registro_producto.html')

@app.route('/registro_libro', methods=['GET', 'POST'])
def registro_libro():
    if request.method == 'POST':
        datos = {
            'titulo': request.form['titulo'],
            'autor': request.form['autor'],
            'resumen': request.form['resumen'],
            'medio': request.form['medio']
        }
        session['datos_registro_libro'] = datos
        return redirect(url_for('mostrar_datos', formulario='registro_libro'))
    return render_template('registro_libro.html')

@app.route('/mostrar_datos/<formulario>')
def mostrar_datos(formulario):
    datos = session.get(f'datos_{formulario}')
    return render_template('mostrar_datos.html', datos=datos, formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)
