from flask import Flask, app, render_template
app = Flask(__name__)
@app.route("/")
def hola():
    return render_template("crearEmpleado.html")
