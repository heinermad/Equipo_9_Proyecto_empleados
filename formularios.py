from wtforms.fields.html5 import DateField, IntegerField
from wtforms.fields.simple import PasswordField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import DecimalField, EmailField, IntegerField, DateField
#from wtforms.fields.simple import FileField
from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class FormRol(FlaskForm):
    nombre = StringField('nombre', validators=[InputRequired()])

class FormAgregar(FlaskForm):
    nombre = StringField(validators=[InputRequired()])
    apellidos = StringField(validators=[InputRequired()])
    direccion = StringField(validators=[InputRequired()])
    numDocId = IntegerField(validators=[InputRequired()])
    fechaNac = DateField(validators=[InputRequired()])
    usuario = StringField(validators=[InputRequired()])
    clave = PasswordField(validators=[InputRequired()])
    genero = SelectField(choices=[('', 'Seleccione una opción'),('F', 'Femenino'), ('M', 'Masculino')], validators=[InputRequired()]) 
    email = EmailField(validators=[InputRequired()])
    fechaIngreso = DateField(validators=[InputRequired()])
    fechaSalida = DateField(validators=[InputRequired()])
    #fechaSalida = DateField()
    #foto = FileField(validators=[InputRequired()])
    usuario = StringField(validators=[InputRequired()])
    clave = PasswordField(validators=[InputRequired()])
    salario = DecimalField(validators=[InputRequired()])
    rol = SelectField(choices=[('', 'Seleccione una opción'),(1, 'Usuario final'),(2, 'Administrador'), (3, 'SuperAdministrador')], validators=[InputRequired()]) 
    tipoContrato = SelectField(choices=[('', 'Seleccione una opción'),('Indefinido', 'Indefinido'),('Temporal', 'Temporal')], validators=[InputRequired()]) 
    cargo = SelectField(choices=[('', 'Seleccione una opción'),(1, 'Gerente de ventas'),(2, 'Jefe de compras'),(3, 'Otro')], validators=[InputRequired()]) 

    