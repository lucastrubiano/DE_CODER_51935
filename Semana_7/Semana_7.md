# Semana 7

Para realizar la práctica de esta semana, utilizaremos el Docker Compose de la **Semana 7**.

> &nbsp;
>
> ### Docker Semana 7:
> * **Jupyter Notebook + Pyspark**: [http:// localhost:8888/lab?token=coder](http://localhost:8888/lab?token=coder)
> * **Postgres**: `localhost:5435` (user: `postgres`, password: `postgres`, db: `postgres`)
>
> &nbsp;

Antes de ejecutar el Docker Compose, desde la carpeta `Semana_7` ejecutar los comandos para crear las carpetas `postgres_data` y `working_dir`:

```bash
mkdir -p ./Semana_7/docker_shared_folder/postgres_data
mkdir -p ./Semana_7/docker_shared_folder/working_dir
mkdir -p ./Semana_7/docker_shared_folder/working_dir/spark_drivers
```

Crear archivo `.env` con las siguientes variables de entorno en la carpeta `Semana_7/docker_shared_folder/.env`:

```bash
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST_AUTH_METHOD=trust
POSTGRES_PORT=5435
POSTGRES_HOST=postgres_sem7

REDSHIFT_USER=...
REDSHIFT_PASSWORD=...
REDSHIFT_HOST=data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com
REDSHIFT_PORT=5439
REDSHIFT_DB=data-engineer-database
REDSHIFT_SCHEMA=...

JUPYTER_ENABLE_LAB=1
JUPYTER_TOKEN=coder
DRIVER_PATH=/home/coder/working_dir/spark_drivers/postgresql-42.5.2.jar
```

Para ejecutar el Docker Compose, desde la carpeta `Semana_7` ejecutar el comando:

```bash
docker-compose -f ./Semana_7/docker-compose.yml up --build
```

## Microdesafío

Desafío con Pytrends en el archuvo `MicroDesafio_Semana7.ipynb`.
* Ver consigna en [Google Drive](https://docs.google.com/presentation/d/1qJq38395QNSCTTvzzRVRXzRLgZIjvXTk3ZKpTWqj6Mw/edit?usp=sharing)
* Resolución en [Github](https://github.com/CoderContenidos/Data.Engineering/blob/main/Semana%207/MicroDesafio_Semana7.ipynb)

## SQL Alchemy
Ejemplo en vivo.

## Pyscopg2
Pequeño ejemplo rápido.

## Entregable 2
Consignas.