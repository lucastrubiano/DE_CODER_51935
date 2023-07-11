# Ejemplo de Entregable 3
Este es un ejemplo de entregable 3, el cual se puede utilizar como guía para la entrega del mismo. Está desarrollado con Spark como framework de ETL, pero se puede adaptar a Pandas ya que este es más sencillo.

# Distribución de los archivos
Los archivos a tener en cuenta son:
* `docker_images/`: Contiene los Dockerfiles para crear las imagenes utilizadas de Airflow y Spark.
* `docker-compose.yml`: Archivo de configuración de Docker Compose. Contiene la configuración de los servicios de Airflow y Spark.
* `.env`: Archivo de variables de entorno. Contiene variables de conexión a Redshift y driver de Postgres.
* `dags/`: Carpeta con los archivos de los DAGs.
    * `etl_users.py`: DAG principal que ejecuta el pipeline de extracción, transformación y carga de datos de usuarios.
* `logs/`: Carpeta con los archivos de logs de Airflow.
* `plugins/`: Carpeta con los plugins de Airflow.
* `postgres_data/`: Carpeta con los datos de Postgres.
* `scripts/`: Carpeta con los scripts de Spark.
    * `postgresql-42.5.2.jar`: Driver de Postgres para Spark.
    * `common.py`: Script de Spark con funciones comunes.
    * `ETL_Users.py`: Script de Spark que ejecuta el ETL.

# Pasos para ejecutar el ejemplo
1. Posicionarse en la carpeta `otros/ejemplo_entregable_3`. A esta altura debería ver el archivo `docker-compose.yml`.
2. Crear las siguientes carpetas a la misma altura del `docker-compose.yml`.
```bash
mkdir -p dags,logs,plugins,postgres_data,scripts
```
3. Crear un archivo con variables de entorno llamado `.env` ubicado a la misma altura que el `docker-compose.yml`. Cuyo contenido sea:
```bash
REDSHIFT_HOST=...
REDSHIFT_PORT=5439
REDSHIFT_DB=...
REDSHIFT_USER=...
REDSHIFT_SCHEMA=...
REDSHIFT_PASSWORD=...
REDSHIFT_URL="jdbc:postgresql://${REDSHIFT_HOST}:${REDSHIFT_PORT}/${REDSHIFT_DB}?user=${REDSHIFT_USER}&password=${REDSHIFT_PASSWORD}"
DRIVER_PATH=/tmp/drivers/postgresql-42.5.2.jar
```
4. Descargar las imagenes de Airflow y Spark.
```bash
docker-compose pull lucastrubiano/airflow:airflow_2_6_2
docker-compose pull lucastrubiano/spark:spark_3_4_1
```
5. Las imagenes fueron generadas a partir de los Dockerfiles ubicados en `docker_images/`. Si se desea generar las imagenes nuevamente, ejecutar los comandos que están en los Dockerfiles.
6. Ejecutar el siguiente comando para levantar los servicios de Airflow y Spark.
```bash
docker-compose up --build
```
7. Una vez que los servicios estén levantados, ingresar a Airflow en `http://localhost:8080/`.
8. En la pestaña `Admin -> Connections` crear una nueva conexión con los siguientes datos para Redshift:
    * Conn Id: `redshift_default`
    * Conn Type: `Amazon Redshift`
    * Host: `host de redshift`
    * Database: `base de datos de redshift`
    * Schema: `esquema de redshift`
    * User: `usuario de redshift`
    * Password: `contraseña de redshift`
    * Port: `5439`
9. En la pestaña `Admin -> Connections` crear una nueva conexión con los siguientes datos para Spark:
    * Conn Id: `spark_default`
    * Conn Type: `Spark`
    * Host: `spark://spark`
    * Port: `7077`
    * Extra: `{"queue": "default"}`
10. En la pestaña `Admin -> Variables` crear una nueva variable con los siguientes datos:
    * Key: `driver_class_path`
    * Value: `/tmp/drivers/postgresql-42.5.2.jar`
11. En la pestaña `Admin -> Variables` crear una nueva variable con los siguientes datos:
    * Key: `spark_scripts_dir`
    * Value: `/opt/airflow/scripts`
12. Ejecutar el DAG `etl_users`.