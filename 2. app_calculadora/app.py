# importamos las clases y métodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def aritmetica():
    if request.method == "POST":
        # Valores que recibo del form n1, n2 son pasados
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        # Realizamos operaciones aritméticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html', total_suma=suma,
                               total_resta=resta,
                               total_multiplicacion=multiplicacion,
                               total_division=division)

    return render_template('index.html')

TASA_CAMBIO = 0.00025

# Ruta y función para la calculadora de divisas
@app.route('/divisa', methods=['GET', 'POST'])
def divisa():
    resultado_conversion = None
    if request.method == "POST":
        # Intenta obtener el valor y manejar errores
        try:
            pesos_colombianos = float(request.form.get('pesos', 0))
            resultado_conversion = pesos_colombianos * TASA_CAMBIO
        except ValueError:
            resultado_conversion = "Error: Ingrese un número válido"

    return render_template('divisa.html', resultado_conversion=resultado_conversion)

    
    
    return render_template('longitudes.html')

if __name__ == "__main__":
    app.run(debug=True)
