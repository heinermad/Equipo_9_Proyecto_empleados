from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import DecimalField, EmailField, IntegerField, DateField
from wtforms.fields.simple import FileField, SubmitField
from wtforms.form import Form
from wtforms.validators import EqualTo, InputRequired, Regexp

class FormAgregar(FlaskForm):
    nombre = StringField(validators=[InputRequired()])
    apellidos = StringField(validators=[InputRequired()])
    direccion = StringField(validators=[InputRequired()])
    numDocId = IntegerField(validators=[InputRequired()])
    genero = SelectField(choices=[('', 'Seleccione una opción'),('F', 'Femenino'), ('M', 'Masculino')], validators=[InputRequired()]) 
    email = EmailField(validators=[InputRequired()])
    fechaNac = DateField(validators=[InputRequired()])
    fechaIngreso = DateField(validators=[InputRequired()])
    fechaSalida = DateField(validators=[InputRequired()])
    foto = FileField(validators=[InputRequired()])
    usuario = StringField(validators=[InputRequired()])
    clave = PasswordField(validators=[InputRequired()])
    claveConfirm = PasswordField(validators=[InputRequired(), EqualTo(clave)])
    salario = DecimalField(validators=[InputRequired()])
    rol = SelectField(choices=[('', 'Seleccione una opción'),(1, 'Usuario final'),(2, 'Administrador'), (3, 'SuperAdministrador')], validators=[InputRequired()]) 
    tipoContrato = SelectField(choices=[('', 'Seleccione una opción'),(1, 'Indefinido'),(2, 'Temporal')], validators=[InputRequired()]) 
    cargo = SelectField(choices=[('', 'Seleccione una opción'),(1, 'Gerente de ventas'),(2, 'Jefe de compras'),(3, 'Otro')], validators=[InputRequired()]) 
    dependencia = SelectField(choices=[('', 'Seleccione una opción'),(1, 'Ventas'),(2, 'Compras'),(3, 'Otro')], validators=[InputRequired()]) 
    submit = SubmitField('Guardar')

class FormRol(FlaskForm):
    nombre = StringField('nombre', validators=[InputRequired()])

    