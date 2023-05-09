# Semana 3

## Arquitectura del Docker-Compose

![Arquitectura](./images/arquitectura.png)

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

-- seleccionar una BD
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
<br>
<br>

# Anexo: Limitación de recursos del WSL2 (en Windows):

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