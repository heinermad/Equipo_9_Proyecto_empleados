--
-- File generated with SQLiteStudio v3.3.3 on vie. oct. 22 08:36:48 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Cargo
CREATE TABLE "Cargo" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	VARCHAR(50) NOT NULL,
	"salario"	DECIMAL NOT NULL,
	"idDependencia"	INTEGER NOT NULL,
	FOREIGN KEY("idDependencia") REFERENCES "Dependencia"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO Cargo (id, nombre, salario, idDependencia) VALUES (1, 'jAFE DE V', 5432, 1);

-- Table: Contrato
CREATE TABLE Contrato (id INTEGER NOT NULL, tipoContrato VARCHAR (20) NOT NULL, estado VARCHAR (10) NOT NULL, fechaIngreso VARCHAR (25) NOT NULL, fechaSalida VARCHAR (25), idEmpleado INTEGER NOT NULL, FOREIGN KEY (idEmpleado) REFERENCES Empleado (id), PRIMARY KEY (id));
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (1, 'Indefinido', 'activo', '2021-10-05', '09/10/2022', 987654321);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (2, 'Temporal', 'activo', '2021-10-11', '09/10/2022', 333333333333333);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (3, 'Indefinido', 'activo', '2021-10-05', '09/10/2022', 77777777777);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (4, 'Indefinido', 'activo', '2021-10-12', '09/10/2022', 3213214324325);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (5, 'Indefinido', 'activo', '2021-10-18', '09/10/2022', 13421412342141);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (6, 'Indefinido', 'activo', '2021-10-11', '09/10/2022', 453253543254);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (7, 'Indefinido', 'activo', '2021-10-11', '09/10/2022', 2132432142343);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (8, 'Indefinido', 'activo', '2021-10-04', '09/10/2022', 666666666666);
INSERT INTO Contrato (id, tipoContrato, estado, fechaIngreso, fechaSalida, idEmpleado) VALUES (9, 'Indefinido', 'activo', '2021-10-11', '09/10/2022', 43124312412421);

-- Table: Dependencia
CREATE TABLE "Dependencia" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	VARCHAR(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO Dependencia (id, nombre) VALUES (1, 'Ventas');
INSERT INTO Dependencia (id, nombre) VALUES (2, 'Recursos humanos');

-- Table: Empleado
CREATE TABLE Empleado (id INTEGER NOT NULL UNIQUE, nombre VARCHAR (100) NOT NULL, apellido VARCHAR (100) NOT NULL, direccion VARCHAR (100) NOT NULL, fechaNac VARCHAR (25) NOT NULL, correo VARCHAR (100) NOT NULL, genero VARCHAR (10) NOT NULL, foto VARCHAR (30), idCargo INTEGER REFERENCES Cargo (id) NOT NULL, PRIMARY KEY (id));
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (987654321, 'Daniel', 'Kruk R', 'C 20 10 22', '2021-10-04', 'krukdaniel@gmail.com', 'M', 'hjfjdahkjfh', 1);
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (77777777777, 'Heiner', 'Madera Duarte', 'C 20 10 22', '2021-10-12', 'heinermad88@hotmail.com', 'F', 'hjfjdahkjfh', 1);
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (453253543254, 'Heiner', 'Madera Duarte', 'C 20 10 22', '2021-10-12', 'fdsafasfa@jksajfjkjalfk', 'M', 'hjfjdahkjfh', 1);
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (666666666666, 'Andr�s', 'MAr�n', 'C 20 10 22', '2021-10-12', 'fdsafasfa@jksajfjkjalfk', 'F', 'hjfjdahkjfh', 1);
-- INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (2132432142343, 'Wilmer', 'Madera Duarte', 'C 20 10 22', '2021-10-13', 'trtetrewtrewt@hjgfjf', 'M', 'hjfjdahkjfh', 1);
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (3213214324325, 'Slide', 'Slode', 'C 20 10 22', '2021-10-10', 'slideslode@hotmail.com', 'F', 'hjfjdahkjfh', 1);
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (13421412342141, 'Heiner', 'Madera Duarte', 'C 20 10 22', '2021-10-09', 'fdsafasfa@jksajfjkjalfk', 'F', 'hjfjdahkjfh', 1);
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (43124312412421, 'KArla', 'sfadsafdsa', 'C 20 10 22', '2021-10-05', 'fdsafasfa@jksajfjkjalfk', 'F', 'hjfjdahkjfh', 1);
INSERT INTO Empleado (id, nombre, apellido, direccion, fechaNac, correo, genero, foto, idCargo) VALUES (333333333333333, 'Ricardo', 'Gareca', 'C 30 28 99', '1984-06-06', 'rgareca@sistemp.org', 'M', 'hjfjdahkjfh', 1);

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

-- Table: Rol
CREATE TABLE "Rol" (
	"id"	INTEGER NOT NULL,
	"nombre"	VARCHAR(15) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO Rol (id, nombre) VALUES (1, 'Usuario');
INSERT INTO Rol (id, nombre) VALUES (2, 'Administrador');
INSERT INTO Rol (id, nombre) VALUES (3, 'SuperAdministrador');
INSERT INTO Rol (id, nombre) VALUES (4, 'ADmin2');
INSERT INTO Rol (id, nombre) VALUES (5, 'Superadmin2');
INSERT INTO Rol (id, nombre) VALUES (6, 'ffsfsdfsdfsf');
INSERT INTO Rol (id, nombre) VALUES (7, 'WOnder Woman');
INSERT INTO Rol (id, nombre) VALUES (8, 'hghhhdsgdsfasdsdfdghgjhjkhj,lkjglk');
INSERT INTO Rol (id, nombre) VALUES (9, 'Superman');

-- Table: Usuario
CREATE TABLE Usuario (id INTEGER NOT NULL UNIQUE, nombre VARCHAR (20) NOT NULL, clave VARCHAR (50) NOT NULL, idRol INTEGER NOT NULL, idEmpleado INTEGER REFERENCES Empleado (id) CONSTRAINT evitar_fk_duplicada UNIQUE ON CONFLICT ROLLBACK, FOREIGN KEY (idRol) REFERENCES Rol (id), PRIMARY KEY (id));
INSERT INTO Usuario (id, nombre, clave, idRol, idEmpleado) VALUES (1, 'heinermad', 'heinermadera', 1, 77777777777);
INSERT INTO Usuario (id, nombre, clave, idRol, idEmpleado) VALUES (2, 'heinermad', 'sha256$0TuAqtvSD0GDhgdN$917c56f164b16333504f4f6326eaa58e814bdf6a5f4e5d756c6c4ebeaaad7e89', 1, 13421412342141);
INSERT INTO Usuario (id, nombre, clave, idRol, idEmpleado) VALUES (3, 'heinermad', 'sha256$XGjY6rMGfcjAVx3b$45373fe580d5239ec93d5d19ad55ef423344ec5490ac4f4b4e8f1fbd68237a2c', 2, 453253543254);
INSERT INTO Usuario (id, nombre, clave, idRol, idEmpleado) VALUES (4, 'wilmermad', 'sha256$GIYBekpWyxwQLutJ$6493812bb3e0c65bf2a57f889d7335b009617175b5f513b1efd7d17e32f19bfb', 2, 2132432142343);
INSERT INTO Usuario (id, nombre, clave, idRol, idEmpleado) VALUES (5, 'andremarin', 'sha256$S7CBlkBm5g3i1ald$ce088198f6f239502cc1570ae70399b304bf6d69712f86760050a0d763036f43', 1, 666666666666);
INSERT INTO Usuario (id, nombre, clave, idRol, idEmpleado) VALUES (6, 'sfsdfsdgdgg', 'sha256$qLXkXzqc8BtFTTtH$17a2478e3d49f2fc91ba82687a64302364535a7adb9f449ccfae98b500d2267e', 1, 43124312412421);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
