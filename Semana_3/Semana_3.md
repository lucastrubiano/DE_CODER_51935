# Semana 3

## Indice:

1. [¿Cómo configurar y ejecutar Docker?](#como-configurar-y-ejecutar-docker)
1. [Ejercicios con Postgres para BBDD SQL](#ejercicios-con-postgres-para-bbdd-sql)
2. [Ejercicio con MongoDB para BBDD NoSQL](#ejercicio-con-mongodb-para-bbdd-nosql)
3. [Limitación de recursos del WSL2 (en Windows)](#limitacion-de-recursos-del-wsl2-en-windows)

<!-- ## Arquitectura de Data Lakehouse en Docker-Compose

![Arquitectura](./images/arquitectura.png) -->

<a name="#como-configurar-y-ejecutar-docker"> </a>
## ¿Cómo configurar y ejecutar Docker?

### **Requerimientos:**
* Tener Docker y Docker Compose instalado.
* Tener Docker Desktop y WSL2 instalado. (Sólo para Windows)

### **Crear carpetas para los contenedores:**
La estructura de carpetas a crear es la siguiente:
* Semana_3/
    * docker_shared_folder/
        * mongo_data/
        * postgres_data/
    * docker-compose.yml



### **Crear imagenes y ejecutar contenedores:**
Posicionar la consola dentro de la carpeta `Semana_3` utilizando el comando `cd`. Debería ver el archivo `docker-compose.yml` dentro de esta carpeta.

```bash
# Windows
cd {...relative_path}\dateng_coder\Semana_3
```
```bash
# Linux
cd {...relative_path}/dateng_coder/Semana_3
```

Luego ejecutar el comando `docker-compose up --build` para crear las imagenes y ejecutar los contenedores.

```bash
# Windows
docker-compose up --build
```
```bash
# Linux
sudo docker-compose up --build
```

> El comando `--build` es para que se construya la imagen de docker y luego se ejecute el container.

> Si recibe un error `no configuration file provided: not found`, es porque no se encuentran en el directorio correcto. Deben estar en el directorio donde se encuentra el archivo **docker-compose.yml** dentro de la carpeta **Semana_3**.

> **Sólo para Linux**: Si recibe un error de permisos o que no está iniciado el Docker Daemon, es porque no se está ejecutando el comando con permisos de administrador. En ese caso, ejecutar el comando con `sudo`.

<br>
<br>

<a name="ejercicios-con-postgres-para-bbdd-sql"></a>
# Ejercicios con Postgres para BBDD SQL:
Para ejecutar la solución ETL vista en clase, debe abrir dbeaver u algún otro cliente de postgres y crear una conexión a la base de datos postgres. (Con la IP `localhost` u otra si **postgres** no está corriendo en su maquina).

Luego, debe ejecutar el script **ETL_Postgres.sql**.

> Si no tiene dbeaver instalado, puede utilizar [pgAdmin](https://www.pgadmin.org/download/).

Queries del ejercicio:
<!-- -- agregar los create database; -->
```SQL
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
WHEN 'administracion' THEN 'Base de datos, Administración'
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
```

<br>
<br>

<a name="ejercicio-con-mongodb-para-bbdd-nosql"></a>
# Ejercicio con MongoDB para BBDD NoSQL:
Entrar a la consola de **MongoDB** con el comando:
```bash
docker exec -it mongo bash
```

También puede abrir [Mongo Express](http://localhost:8081) en el navegador.

Comandos del ejercicio:
```
-- Version mongo
mongo

-- Cambiar a la base de datos admin
use admin

-- Autenticarme con usuario root
db.auth("root", "example");

-- Ver databases disponibles
show dbs

-- seleccionar una BD, crearla previamente
use datos

-- verificar BD seleccionada
db

-- Crear usuarios
db.createUser({"user":"lucas", pwd:"lucas123",roles:["readWrite","dbAdmin"]})

-- Crear colecciones
db.createCollection('clientes');
show collections;

-- Insertar datos
db.clientes.insert({nombres:"Lucas", apellido:"Trubiano"});
db.clientes.insert({nombres:"Fernando", apellido:"Pareja"});
db.clientes.insert({nombres:"Juan", apellido:"Perez"});

-- Ver registros de coleccion
db.clientes.find();

-- Ver de mejor manera
db.clientes.find().pretty();

-- Ver registros de coleccion con filtro
db.clientes.find({nombres:"Lucas"});

-- Editar registros de coleccion
db.clientes.update({nombres:"Lucas"},{$set:{apellido:"Coder"}});

-- Eliminar registros de coleccion
db.clientes.remove({nombres:"Juan"});
```

<br>
<br>

<a name="limitacion-de-recursos-del-wsl2-en-windows"></a>
# Limitación de recursos del WSL2 (en Windows):

A continuación se detalla como limitar los recursos de la máquina de Linux que corre Docker en Windows.	

> WSL2 es una capa de compatibilidad para ejecutar Linux en Windows. Es necesario para poder ejecutar Docker en Windows. Y para que Docker no consuma demasiados recursos de la máquina, se debe configurar la cantidad de memoria RAM y procesadores que puede utilizar. Para esto, se debe crear un archivo de configuración de WSL2.

Para configurar la limitación de recursos de WSL2, seguir los siguientes pasos:

* Crear archivo de configuración de WSL2 (**.wslconfig**) en la ruta (**C:\Users\\{username}\\.wslconfig**) con el siguiente contenido:
```bash
[wsl2]
processors=1
memory=2GB
```
* Esto es para que la maquina de Linux que corre Docker no consuma demasiados recursos de la máquina, ya que por defecto consume 4GB de RAM y 2 procesadores.
* Al aplicar esta configuración, se debe reiniciar la máquina.
```bash
wsl --shutdown
```

<!-- ```bash
[wsl2]
processors=1
memory=2GB
swap=0
localhostForwarding=true
``` -->

<br>
<br>

<a name="fin"></a>