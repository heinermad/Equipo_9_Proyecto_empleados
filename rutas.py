from flask import Flask, app, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.validators import InputRequired
from formularios import FormAgregar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empleados.db'
db = SQLAlchemy(app)

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String)

class FormRol(FlaskForm):
    nombre = StringField('nombre', validators=[InputRequired()])

@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("dashboard.html")

@app.route('/crear', methods=['GET', 'POST'])
def agregar():
    form = FormAgregar()
    if form.validate_on_submit():
        return redirect(url_for('crear'))
    return render_template('crearEmpleado.html', form=form)

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
    return render_template("dashboard.html")

@app.route("/retroalimentacion", methods=["GET", "POST"])
def retroalimentar():
    return render_template("retroalimentacion.html")

@app.route("/paginaEmpleado", methods=["GET", "POST"])
def inicio_empleado():
    return render_template("paginaEmpleado.html")

@app.route("/rol", methods=["GET", "POST"])
def rola():
    form = FormRol()
    if form.validate_on_submit():
        nuevoRol = Rol(nombre=form.nombre.data)
        db.session.add(nuevoRol)
        db.session.commit() 
        return redirect(url_for('rola'))
    return render_template('rol.html', form=form)