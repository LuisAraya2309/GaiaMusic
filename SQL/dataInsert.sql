USE[GaiaMusic]

INSERT INTO dbo.UserTypes
VALUES(
	'Cliente'
)

INSERT INTO dbo.UserTypes
VALUES(
	'Administrador'
)

INSERT INTO dbo.UserTypes
VALUES(
	'Proveedor'
)

INSERT INTO dbo.InstrumentTypes
VALUES(
	'Cuerdas'
)

INSERT INTO dbo.InstrumentTypes
VALUES(
	'Percusión'
)
INSERT INTO dbo.InstrumentTypes
VALUES(
	'Viento'
)

INSERT INTO dbo.TransactionTypes
VALUES(
	'Sale'
)
INSERT INTO dbo.TransactionTypes
VALUES(
	'Guarantee'
)
INSERT INTO dbo.TransactionTypes
VALUES(
	'Update'
)
INSERT INTO dbo.TransactionTypes
VALUES(
	'Add'
)
INSERT INTO dbo.TransactionTypes
VALUES(
	'Delete'
)

/*Sing Up users*/
EXECUTE sp_SignUp 'Rolbin Mendez', 'Llegando al cielo y luego 50 a la derecha', 'DonRobin','elDeJorge','Administrador',0 ;
EXECUTE sp_SignUp 'Manfred Pozuelo', 'El Molino, Cartago', 'MGalleta','oreoLaMejor','Administrador',0 ;
EXECUTE sp_SignUp 'Sebastián Díaz Obando', 'Palo verde, casa 18A', 'Not_Scout01','sufreMamon','Cliente',0 ;
EXECUTE sp_SignUp 'Gabriel Vega Obando', 'La Pithaya, Hacienda de oro', 'GaboBot','metropoli123','Cliente',0 ;
EXECUTE sp_SignUp 'Andrey Campos', 'San Blas, Cartago', 'Cito','economia123','Cliente',0 ;
EXECUTE sp_SignUp 'Luis Carlos Araya', 'Tejar centro', 'DonLuis','12345','Proveedor',0 ;
EXECUTE sp_SignUp 'Robert Araya', 'La Angelina, Tres Rios', 'Fraya','54321','Proveedor',0 ;

/*Add and buy an instrument*/
EXECUTE sp_AddNewInstrument 'Cuerdas' ,'DonRobin', 'Guitarra electrica fender', 'Cuerdas de metal , con salidas para ampllificador',180000,3,0;
EXECUTE sp_AddNewInstrument 'Cuerdas' ,'DonRobin', 'Violin Yamaha', 'Cuerdas de metal , sonido natural',120000,5,0;
EXECUTE sp_AddNewInstrument 'Cuerdas' ,'MGalleta', 'Bajo fender', 'Salidas para ampllificador',100000,2,0;

EXECUTE sp_AddNewInstrument 'Percusión' ,'DonRobin', 'Tambor cilindrico ', 'Fabricado sobre una base soldada de 10mm de acero',180000,3,0;
EXECUTE sp_AddNewInstrument 'Percusión' ,'MGalleta', 'Tambor de reloj', 'sonido natural',120000,5,0;
EXECUTE sp_AddNewInstrument 'Percusión' ,'MGalleta', 'Platillos Crash', 'Nueva versión con mejor sonido',100000,2,0;

EXECUTE sp_AddNewInstrument 'Viento' ,'DonRobin', 'Clarinete yamaha', 'YCL-250 ayuda a proyectar y mejorar la entonación en las notas más bajas.',180000,3,0;
EXECUTE sp_AddNewInstrument 'Viento' ,'DonRobin', 'Oboe yamaha', 'tono de un equilibrio excepcional y gran colorido.',120000,5,0;
EXECUTE sp_AddNewInstrument 'Viento' ,'MGalleta', 'Flauta yamaha', 'Digitación Alemana; Estilo Barroco; Material: Resina',100000,2,0;

EXECUTE sp_BuyProduct 'Guitarra electrica fender' , 'Not_Scout01', 1,0;

/*Request Orders*/
EXECUTE sp_RequestOrders 'DonRobin', 'DonLuis','5 pianos , 1 guitarra, 2 flautas',0;
EXECUTE sp_RequestOrders 'DonRobin', 'DonLuis','1 bateria , 2 bajos',0;

/*Update Orders*/
EXECUTE sp_UpdateOrderStatus 'Doing' , '5 pianos , 1 guitarra, 2 flautas',0;

/*View Orders*/

EXECUTE sp_ViewOrders 'DonLuis',0 

/*
DBCC CHECKIDENT (Instruments, RESEED, 1)
DBCC CHECKIDENT (Guarantees, RESEED, 1)
DBCC CHECKIDENT (InstrumentTypes, RESEED, 1)
DBCC CHECKIDENT (ProductsOrders, RESEED, 1)
DBCC CHECKIDENT (Stock, RESEED, 1)
DBCC CHECKIDENT (Transactions, RESEED, 1)
DBCC CHECKIDENT (TransactionTypes, RESEED, 1)
DBCC CHECKIDENT (Users, RESEED, 1)
DBCC CHECKIDENT (UserTypes, RESEED, 1)
*/