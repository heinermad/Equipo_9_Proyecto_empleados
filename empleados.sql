--
-- File generated with SQLiteStudio v3.3.3 on s�b. oct. 16 21:43:58 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Dependencia
CREATE TABLE "Dependencia" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	VARCHAR(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- Table: Cargo
CREATE TABLE "Cargo" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	VARCHAR(50) NOT NULL,
	"salario"	DECIMAL NOT NULL,
	"idDependencia"	INTEGER NOT NULL,
	FOREIGN KEY("idDependencia") REFERENCES "Dependencia",
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- Table: Contrato
CREATE TABLE "Contrato" (
	"id"	INTEGER NOT NULL UNIQUE,
	"tipoContrato"	VARCHAR(20) NOT NULL,
	"estado"	VARCHAR(10) NOT NULL,
	"fechaIngreso"	VARCHAR(25) NOT NULL,
	"FechaSalida"	VARCHAR(25) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- Table: Rol
CREATE TABLE "Rol" (
	"id"	INTEGER NOT NULL,
	"nombre"	VARCHAR(15) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO Rol (id, nombre) VALUES (1, 'Usuario');
INSERT INTO Rol (id, nombre) VALUES (2, 'Administrador');
INSERT INTO Rol (id, nombre) VALUES (3, 'SuperAdministrador');

-- Table: Usuario
CREATE TABLE "Usuario" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	VARCHAR(20) NOT NULL,
	"clave"	VARCHAR(50) NOT NULL,
	"idRol"	INTEGER NOT NULL,
	FOREIGN KEY("idRol") REFERENCES "Rol"("id"),
	PRIMARY KEY("id")
);

-- Table: Empleado
CREATE TABLE "Empleado" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	VARCHAR(100) NOT NULL,
	"apellido"	VARCHAR(100) NOT NULL,
	"direccion"	VARCHAR(100) NOT NULL,
	"fechaNac"	VARCHAR(25) NOT NULL,
	"documento"	INTEGER NOT NULL,
	"correo"	VARCHAR(100) NOT NULL,
	"genero"	VARCHAR(10) NOT NULL,
	"idUsuario"	INTEGER NOT NULL,
	"foto"	VARCHAR(30),
	"idContrato"	INTEGER NOT NULL,
	"idCargo"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("idUsuario") REFERENCES "Usuario"("id"),
	FOREIGN KEY("idCargo") REFERENCES "Cargo"("id"),
	FOREIGN KEY("idContrato") REFERENCES "Contrato"("id")
);

-- Table: Evaluacion
CREATE TABLE "Evaluacion" (
	"id"	INTEGER NOT NULL UNIQUE,
	"calificacion"	DECIMAL NOT NULL,
	"retroalimentacion"	TEXT,
	"idEmpleado"	INTEGER,
	"fecEval"	VARCHAR(15),
	"fecSubida"	VARCHAR(15),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("idEmpleado") REFERENCES "Empleado"("id")
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
