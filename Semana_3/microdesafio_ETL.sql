--agregar los create database;

CREATE SCHEMA articulos;

CREATE TABLE articulos.titulos
(titulo_id char(6) NOT NULL,
titulo varchar(80) NOT NULL,
tipo char(20) NOT NULL);


INSERT INTO articulos.titulos VALUES ('1', 'Consultas SQL','bbdd');
INSERT INTO articulos.titulos VALUES ('3', 'Grupo recursos Azure','administracion');
INSERT INTO articulos.titulos VALUES ('4', '.NET Framework 4.5','programacion');
INSERT INTO articulos.titulos VALUES ('5', 'Programacion C#','dev');
INSERT INTO articulos.titulos VALUES ('7', 'Power BI','BI');
INSERT INTO articulos.titulos VALUES ('8', 'Administracion Sql server','administracion');

CREATE TABLE articulos.autores
(TituloId char(6) NOT NULL,
NombreAutor Varchar(100) NOT NULL,
ApellidosAutor Varchar(100) NOT NULL,
TelefonoAutor VarChar(25)
);

INSERT INTO articulos.autores VALUES ('3', 'David', 'Saenz', '99897867');
INSERT INTO articulos.autores VALUES ('8', 'Ana', 'Ruiz', '99897466');
INSERT INTO articulos.autores VALUES ('2', 'Julian', 'Perez', '99897174');
INSERT INTO articulos.autores VALUES ('1', 'Andres', 'Calamaro', '99876869');
INSERT INTO articulos.autores VALUES ('4', 'Cidys', 'Castillo', '998987453');
INSERT INTO articulos.autores VALUES ('5', 'Pedro', 'Molina', '99891768');

CREATE TABLE DimTitulos
(TituloId char(6) NOT NULL,
TituloNombre VarChar(100) NOT NULL,
TituloTipo VarChar(100) NOT NULL,
NombreCompleto VarChar(200),
TelefonoAutor Varchar(25));


CREATE PROCEDURE pETL_Insertar_DimTitulo()
LANGUAGE plpgsql
as
$$
begin
DELETE FROM DimTitulos;
INSERT INTO DimTitulos
SELECT 
t.titulo_id,
CAST(t.titulo as VarChar(100)) as TituloNombre,
CASE CAST(t.tipo as Varchar(100))
WHEN 'bbdd' THEN 'Base de datos, Transact-SQL'
WHEN 'BI' THEN 'Base de datos, BI'
WHEN 'administracion' THEN 'Base de datos, Administraci�n'
WHEN 'dev' THEN 'Desarrollo'
WHEN 'programacion' THEN 'Desarrollo'
end as TituloTipo,
CONCAT(a.NombreAutor,' ',a.ApellidosAutor) as NombreCompleto,
a.TelefonoAutor
FROM articulos.titulos as t
JOIN articulos.autores as a ON t.titulo_id =a.TituloId;
end
$$;

CALL pETL_Insertar_DimTitulo();

SELECT * FROM DimTitulos;