from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "secreto"  # Necesario para flash messages
Bootstrap(app)

# Página de inicio
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))  # Redirige sin verificar usuario/contraseña
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/empleados")
def empleados():
    return render_template("empleados.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/sucursales")
def sucursales():
    return render_template("sucursales.html")

@app.route("/recuperacion")
def recuperacion():
    return render_template("recuperacion.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")


if __name__ == "__main__":
    app.run(debug=True)
    