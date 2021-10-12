from flask import Flask, app, render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("dashboard.html")

@app.route("/crear", methods=["GET", "POST"])
def agregar():
    return render_template("CrearEmpleado.html")

@app.route("/buscar", methods=["GET", "POST"])
def encontrar():
    return render_template("buscarEmpleados.html")

@app.route("/editar", methods=["GET", "POST"])
def actualizar():
    return render_template("editarEmpleado.html")

@app.route("/eliminar", methods=["GET", "POST"])
def borrar():
    return render_template("eliminarEmpleado.html")

@app.route("/dashboard", methods=["GET", "POST"])
def administrar():
    return render_template("eliminarEmpleado.html")
