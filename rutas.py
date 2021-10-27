from operator import and_
from flask import Flask, app, json, jsonify, render_template, sessions
from flask.helpers import url_for
from sqlalchemy.sql.expression import true
from werkzeug.utils import redirect
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, ForeignKey, String, Float, Column
from sqlalchemy.orm import relationship
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from formularios import LoginForm, FormAgregar, FormRol
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empleados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Base = declarative_base()
# Section for class ORM DB
class Rol(UserMixin, db.Model):
    __tablename__ = 'Rol'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

class Dependencia(UserMixin, db.Model):
    __tablename__ = 'Dependencia'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

class Cargo(UserMixin, db.Model):
    __tablename__ = 'Cargo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    salario = Column(Float)
    idDependencia = Column(Integer,ForeignKey("Dependencia.id"))
    dependencia = relationship("Dependencia",foreign_keys=[idDependencia])

class Empleado(UserMixin, db.Model):
    __tablename__ = 'Empleado'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    fechaNac = Column(String)
    correo = Column(String)
    genero = Column(String)
    foto = Column(String)
    idCargo = Column(Integer,ForeignKey("Cargo.id"))
    cargo = relationship("Cargo",foreign_keys=[idCargo])

class Contrato(db.Model):
    __tablename__ = 'Contrato'
    id = Column(Integer, primary_key=True)
    tipoContrato = Column(String)
    estado = Column(String)
    fechaIngreso = Column(String)
    fechaSalida = Column(String)
    idEmpleado= Column(Integer, ForeignKey("Empleado.id"))
    empleado = relationship("Empleado",foreign_keys=[idEmpleado])

class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    clave = Column(String)
    idRol= Column(Integer, ForeignKey("Rol.id"))
    idEmpleado= Column(Integer, ForeignKey("Empleado.id"))
    rol= relationship("Rol", foreign_keys=[idRol])
    empleado= relationship("Empleado",foreign_keys=[idEmpleado])

# Schema to handle queries from Empleados
class EmployeSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'nombre',
            'apellido',
            'direccion',
            'fechaNac',
            'correo',
            'genero'
        )
Employe_Schema = EmployeSchema()
Employees_Schema = EmployeSchema(many=True)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/', methods=["GET", "POST"])
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Usuario.query.filter_by(nombre=form.username.data).first()
        if user:
            if check_password_hash(user.clave, form.password.data):
                login_user(user)
                return redirect(url_for('inicio'))
        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def inicio():
    return render_template('dashboard.html', name=current_user.nombre)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/crear', methods=['GET', 'POST'])
def agregar():
    form = FormAgregar()
    if form.validate_on_submit():

        nuevoEmpleado = Empleado(
        id=form.numDocId.data,
        nombre = form.nombre.data,
        apellido = form.apellidos.data,
        direccion = form.direccion.data,
        fechaNac = form.fechaNac.data,
        correo = form.email.data,
        genero = form.genero.data,
        #genero = dict(form.genero.choices).get(form.genero.data),#recuperar los valores que el usuario ve en el select
        foto = "hjfjdahkjfh",
        idCargo = form.cargo.data
        )

        nuevoContrato = Contrato(
            tipoContrato = form.tipoContrato.data,
            estado = 'activo',
            fechaIngreso = form.fechaIngreso.data,
            fechaSalida = '09/10/2022',
            idEmpleado = form.numDocId.data
        )

        nuevoUsuario = Usuario(
        nombre=form.usuario.data,
        clave = generate_password_hash(form.clave.data, method='sha256'),
        idEmpleado = form.numDocId.data,
        idRol=form.rol.data,
        )
        db.session.add(nuevoEmpleado)
        db.session.add(nuevoContrato)
        db.session.add(nuevoUsuario)
        db.session.commit()
        return redirect(url_for('agregar'))
    return render_template('CrearEmpleado.html', form=form, name=current_user.nombre)

@app.route("/buscar", methods=["GET", "POST"])
@login_required
def encontrar():
    return render_template("buscarEmpleados.html", name=current_user.nombre)

@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    data = db.session.query(Empleado).all()
    result = Employees_Schema.dump(data)
    return jsonify({'data':result})


@app.route("/editar", methods=["GET", "POST"])
@login_required
def actualizar():
    idForm=request.form.get("idEmp")
    print('El numero es', idForm) 
    if idForm: 
       result=db.session.query(Empleado,Contrato, Usuario).\
       outerjoin(Contrato).\
       outerjoin(Usuario).\
       filter(Empleado.id==idForm )
       print (type(result))
            
       
       for  result2,result3, result4 in result:
          
          Empleado.idCargo=result2.idCargo
          Empleado.nombre= result2.nombre
          Empleado.apellido= result2.apellido
          Empleado.direccion= result2.direccion
          Empleado.fechaNac=result2.fechaNac
          Empleado.correo= result2.correo
          Empleado.genero= result2.genero
          
          if result4:
             Usuario.nombre=result4.nombre
             Usuario.clave=result4.clave
             Usuario.idRol=result4.idRol
          else:
              Usuario.nombre=""
              Usuario.clave=""
              Usuario.idRol=""

          if result3:
            Contrato.tipoContrato=result3.tipoContrato.strip()
            Contrato.estado=result3.estado.strip()
            Contrato.fechaIngreso=result3.fechaIngreso.strip()
            Contrato.fechaSalida=result3.fechaSalida.strip()
          else:
            Contrato.tipoContrato=""
            Contrato.estado=""
            Contrato.fechaIngreso='mm/dd/aaaa '
            Contrato.fechaSalida='mm/dd/aaaa '

          if  Usuario.idRol==1:
              Rol.nombre='Usuario'
          elif  Usuario.idRol==2:
              Rol.nombre='Administrador'
          elif   Usuario.idRol==3:
               Rol.nombre='SuperAdministrador'
          else:
              Rol.nombre=""

          cargo=db.session.query(Cargo).\
          outerjoin(Empleado).\
          filter(and_(Empleado.id==idForm, Cargo.id==Empleado.idCargo)).first()  
         
       cargos=db.session.query(Cargo).filter( Cargo.id!=Empleado.idCargo).all()
        
       return render_template("editarEmpleado.html",  cargos1=cargos, cargoId=cargo.id, cargoNom=cargo.nombre,cSalario=cargo.salario, eNombre=Empleado.nombre, 
                    eApellido=Empleado.apellido, eDireccion=Empleado.direccion,fNac=Empleado.fechaNac,eCorreo=Empleado.correo,
                    eGenero= Empleado.genero.strip(), cTipoContrato=Contrato.tipoContrato, cEstado=Contrato.estado,
                    fechaIngreso=Contrato.fechaIngreso, fechaSalida=Contrato.fechaSalida, nomUsu=Usuario.nombre, claveUsu=Usuario.clave,
                    uRol=Usuario.idRol, p=['Indefinido', 'Temporal', 'Otro'], nomRol=Rol.nombre, roles=enumerate(['Usuario', 'Administrador', 'SuperAdministrador']), docNum=idForm, gen=['Masculino', 'Femenino'],
                    est=['Activo','Inactivo'])
    else:
      return render_template("editarEmpleado.html", name=current_user.nombre)


@app.route("/actualizarEmp", methods=["GET", "POST"])
def actualizarEmpleado():
    cargoAntiguo=request.form.get("cargOld")
    rolAntiguo=request.form.get("rolOld")
    idEmp=request.form.get("doc")
   
    nombreEmp=request.form.get("nombre")
    apellidoEmp=request.form.get("apellidos")
    direccionEmp=request.form.get("direccion")
    fechaNacEmp=request.form.get("fecha_nac")
    correoEmp=request.form.get("correo")
    generoEmp=request.form.get("genero")
    rolEmp=request.form.get("rol")
    usuEmp=request.form.get("usuario")
    claveEmp=request.form.get("clave")
    fechIngEmp=request.form.get('fecha_ingreso')
   
    estadoCon=request.form.get("estado")
    contratoEmp=request.form.get("tipo_contrato")
    fechSalEmp=request.form.get("fecha_salida")
    idCargoEmp=request.form.get("cargo")
    cargoSalario=request.form.get("salario")
    print('EL NOMBRE',nombreEmp, type(fechaNacEmp), type(fechIngEmp), generoEmp,rolEmp,  cargoSalario, idEmp)

    sqlContrato = "update Contrato set tipoContrato ='" + str(contratoEmp) + """
    ', estado ='""" + str(estadoCon) + """
    ', fechaIngreso ='"""+ str(fechIngEmp) + """
    ', fechaSalida ='"""+  str(fechSalEmp) + """
    ' where exists (SELECT id FROM Empleado 
    WHERE Empleado.id = """ + idEmp + " AND Contrato.idEmpleado=" + idEmp + ");"
    db.engine.execute(sqlContrato) 



    sqlUsuario = "update Usuario set nombre = '"+ str(usuEmp) +"', clave ='"+ str(claveEmp) +"',idRol = '"+ str(rolEmp) +"""
    'where exists (SELECT id FROM Empleado  WHERE Empleado.id = '"""+ idEmp +"' AND Usuario.idEmpleado="+ idEmp +""") AND 
    (SELECT id FROM Rol WHERE Rol.id = """+ str(rolAntiguo) +" AND Usuario.idRol = "+ str(rolAntiguo) +");"
    db.engine.execute(sqlUsuario) 

    sqlEmpleado = "update Empleado set nombre = '"+ nombreEmp +"', apellido = '"+ apellidoEmp +"""', 
    direccion = '"""+direccionEmp+"', fechaNac='"+fechaNacEmp+"',correo = '"+correoEmp+"""', 
    genero='"""+ generoEmp +"', idCargo="+ str(idCargoEmp) +""" where exists (SELECT id FROM Cargo 
    WHERE Empleado.id = """+ str(idEmp) +" AND Cargo.id = "+ str(cargoAntiguo) +" AND Empleado.idCargo = "+ str( cargoAntiguo) +");"""
    db.engine.execute(sqlEmpleado)
     
    return render_template("editarEmpleado.html")

@app.route("/eliminar", methods=["GET", "POST"])
@login_required
def borrar():
    return render_template("eliminarEmpleado.html", name=current_user.nombre)

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def administrar():
    return render_template("dashboard.html", name=current_user.nombre)

@app.route("/retroalimentacion", methods=["GET", "POST"])
@login_required
def retroalimentar():
    return render_template("retroalimentacion.html", name=current_user.nombre)

@app.route("/paginaEmpleado", methods=["GET", "POST"])
@login_required
def inicio_empleado():
    return render_template("paginaEmpleado.html", name=current_user.nombre)

@app.route("/rol", methods=["GET", "POST"])
@login_required
def rola():
    form = FormRol()
    if form.validate_on_submit():
        nuevoRol = Rol(nombre=form.nombre.data)
        db.session.add(nuevoRol)
        db.session.commit()
        return redirect(url_for('rola'))
    return render_template('rol.html', form=form, name=current_user.nombre)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
