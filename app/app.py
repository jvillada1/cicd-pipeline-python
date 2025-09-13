# app/app.py
"""
Módulo principal de la aplicación Flask.

Este archivo define la configuración de la aplicación y la ruta principal
para la calculadora, permitiendo realizar operaciones básicas (suma, resta,
multiplicación y división) mediante un formulario web.
"""
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Vista principal de la aplicación.

    Maneja las solicitudes GET y POST:
    - GET: muestra el formulario de la calculadora.
    - POST: recibe los números y la operación, realiza el cálculo
      (suma, resta, multiplicación o división) y devuelve el resultado.

    Returns:
        str: Renderiza la plantilla 'index.html' con el resultado (si existe).
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True, port=5000, host="0.0.0.0")
