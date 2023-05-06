# Semana 3

## Arquitectura del Docker-Compose

![Arquitectura](./images/arquitectura.png)

## ¿Cómo configurar y ejecutar Docker?

### **Requerimientos:**
* Instalar Docker
* Instalar Docker Compose
* Instalar Docker Desktop
* Instalar WSL2 (Windows Subsystem for Linux)

quiero cambiar algo

### **Crear carpetas para postgres:**
* Crear la carpeta **postgres_data** en la ruta **Semana_1/docker_shared_folder/postgres_data**.
> Sin este paso es muy probable que la imagen de Postgres no se cree correctamente. **Atención!**

### **Configurar recursos del WSL2:**
> WSL2 es una capa de compatibilidad para ejecutar Linux en Windows. Es necesario para poder ejecutar Docker en Windows. Y para que Docker no consuma demasiados recursos de la máquina, se debe configurar la cantidad de memoria RAM y procesadores que puede utilizar. Para esto, se debe crear un archivo de configuración de WSL2.
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


### **Crear las imagenes y ejecutar el container de docker:**
Lo primero que hay que hacer para poder crear la imagen y luego ejecutar el container, es movernos por consola (con el comando `cd`) al directorio donde se encuentra el archivo **docker-compose.yml**.
```bash
# Windows
cd C:\\{...relative_path}\dateng_coder\Semana_1

# Linux
cd {...relative_path}/dateng_coder/Semana_1
```

Luego ejecutar el siguiente comando:

```bash
# Windows
docker-compose up --build

# Linux
sudo docker-compose up --build
```

> El comando `--build` es para que se construya la imagen de docker y luego se ejecute el container.
> Si recibe un error `no configuration file provided: not found`, es porque no se encuentran en el directorio correcto. Deben estar en el directorio donde se encuentra el archivo **docker-compose.yml** dentro de la carpeta **Semana_1**.
> **Sólo para Linux**: Si recibe un error de permisos o que no está iniciado el Docker Daemon, es porque no se está ejecutando el comando con permisos de administrador. En ese caso, ejecutar el comando con `sudo`.

### **Buscar la IP interna de la base de datos Postgres**
Cuando queramos hacer la conexión entre Pyspark y Postgres, necesitamos saber la IP interna de la base de datos Postgres. Para esto, ejecutar el siguiente comando:
```bash
# Windows
docker inspect postgres_db | findstr IPAddress

# Linux
docker inspect postgres_db | grep IPAddress
```

### En mi caso el output fue:
```bash
# Windows
# postgres_db --> 172.18.0.2

# Linux
# postgres_db --> 172.19.0.3
```
> Esto sirve para cuando queramos hacer la conexión interna entre Pyspark y Postgres.

<!-- Ingresar en la página de [PG Admin 4](http://127.0.0.1:10003/), con el user: **admin@admin.com** y contraseña: **admin**.
Luego click en **Agregar un Nuevo Servidor** -->

<!-- ### Por cualquier problema, para reiniciar el servicio de Docker y parar los containers:
```bash
sudo systemctl restart docker.socket docker.service
docker container ls
docker rm -f <container id>
``` -->


# Ejercicios Python:
1. Escribir un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
2. Escribir un programa que pida al usuario cuántos números quiere introducir. Luego que lea todos los números y realice una media aritmética.
3. Utilizando la función range() y la conversión a listas generar las siguientes listas dinámicamente:
    - Todos los números del 0 al 10 [0, 1, 2, ..., 10]
    - Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
    - Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
    - Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
    - Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
4. Dadas dos listas (las que se quiera crear), generar una tercera con los elementos que estén presentes en AMBAS listas. Retornar esta nueva lista pero sin elementos duplicados.
5. Escribir un programa que sume todos los números enteros impares desde el 0 hasta el 100.
6. Contar cuantas veces aparece un elemento en una lista.

## Conexion con Jupyter Notebook:

Para ejecutar las soluciones de los ejercicios y realizar pruebas, se debe abrir el archivo **ejercicios_python_jupyter.ipynb** en [Jupyter Notebook]( http://127.0.0.1:10003/lab?token=coder).



# Ejercicios SQL
1. Extraer agentes cuyo nombre empiezen por M o terminen en O.
2. Escriba una consulta que produzca una lista, en orden alfabético, de todas las distintas ocupaciones en la tabla Customer que contengan la palabra "Engineer".
3. Escriba una consulta que devuelva el ID del cliente, su nombre y una columna  Mayor30 que contenga "Sí "si el cliente tiene más de 30 años y "No" en caso contrario.
4. Escriba una consulta que devuelva todas las llamadas realizadas a clientes de la profesión de ingeniería y muestre si son mayores o menores de 30, así como si terminaron comprando el producto de esa llamada.
5. Escriba dos consultas: una que calcule las ventas totales y las llamadas totales realizadas a los clientes de la profesión de ingeniería y otra que calcule las mismas métricas para toda la base de clientes.

## Conexion DBeaver con Postgres DB:
1. Descargar e instalar [DBeaver](https://dbeaver.io/download/)
2. Crear una nueva conexión con los siguientes datos en DBeaver:
    - Host: **127.0.0.1** o **localhost** (es lo mismo cualquiera de estos dos).
    - Port: **10002**
    - Database: **postgres**
    - User: **postgres**
    - Password: **postgres**
3. Click en **Test Connection** y luego en **Finish**.
4. Primero hay que crear las tablas y migrar los datos. Esto se hace sólo la primera vez que se ejecuta el docker-compose.
5. Los script para las migraciones están en la carpeta **Semana_1/docker_shared_folder/working_dir/data/** y son:
    - **agents_migration.sql**
    - **calls_migration.sql**
    - **customers_migration.sql**
4. Abrir el script **ejercicio_sql_dbeaver.sql** con la conexión creada en DBeaver. Y ejecutar el script.

# Mini desafio

Tenemos un aplicativo llamado **CoderReport** que se encarga de generar reportes de los alumnos que cursan en **CoderHouse**. Estos reportes de vez en cuando se generan de forma erronea debido a **alumnos que no existen o que no estan activos en el sistema**. Por lo tanto, necesitamos obtener unas metricas para saber que tan grave es este problema y si es necesario tomar alguna medida al respecto.

Para esto se pide lo siguiente:
* Analizar las ejecuciones de los reportes del mes de Marzo de 2023.
* De las ejecuciones obtener las que fueron correctas y las que fallaron. No las que están planificadas.
* Agrupar por curso, la cantidad de ejecuciones correctas y fallidas. Y el promedio de tiempo de ejecución de cada una (correctas e incorrectas).

Para esto se tienen las siguientes tablas con los siguientes campos:
- **courses**: id, name
- **reports**: id, course_id, status, total_students, active_students, execution_time, created_at
- **reports_status**: id, name

> **Nota:** Los datos de las tablas son ficticios y no representan la realidad.