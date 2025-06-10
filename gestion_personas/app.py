from flask import Flask, render_template, request, redirect
from gestion import Gestion
from empleado import EmpleadoTemporal, EmpleadoFijo
from cliente import Cliente

app = Flask(__name__)
gestion = Gestion()

@app.route('/')
def index():
    return render_template('index.html', personas=gestion.personas)

@app.route('/agregar', methods=['POST'])
def agregar():
    tipo = request.form['tipo']
    nombre = request.form['nombre']
    edad = int(request.form['edad'])

    if tipo == 'cliente':
        email = request.form['email']
        persona = Cliente(nombre, edad, email)
    elif tipo == 'empleado_temporal':
        salario = float(request.form['salario'])
        duracion = int(request.form['duracion'])
        persona = EmpleadoTemporal(nombre, edad, salario, duracion)
    else:
        salario = float(request.form['salario'])
        beneficios = request.form['beneficios']
        persona = EmpleadoFijo(nombre, edad, salario, beneficios)

    gestion.agregar_persona(persona)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
