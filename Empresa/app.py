from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/recuperacion')
def recuperacion():
    return render_template('recuperacion.html')


@app.route("/productos")
def Productos():
    return render_template("productos.html")


@app.route("/contacto")
def Contacto():
    return render_template("contacto.html")

@app.route("/dashboard")
def Dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
