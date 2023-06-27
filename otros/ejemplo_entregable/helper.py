# Contiene las clases y funciones genericas para el ETL

# ========================== INFO GENERAL ==========================
# Path: otros/ejemplo_entregable/helper.py
# Autor: Lucas Trubiano (lucas.trubiano@gmail.com)
# Fecha de Creación: 2023-06-25
# Fecha de Última Modificación: 2023-06-25
# Versión: 1.0
# ==================================================================


# ========================== IMPORTACIONES ==========================
from os import environ as env
from psycopg2 import connect

from pyspark.sql import SparkSession

import pandas as pd


# ========================== CONFIGURACION ==========================

# Variables de configuración de Postgres
POSTGRES_HOST = env["POSTGRES_HOST"]
POSTGRES_PORT = env["POSTGRES_PORT"]
POSTGRES_DB = env["POSTGRES_DB"]
POSTGRES_USER = env["POSTGRES_USER"]
POSTGRES_PASSWORD = env["POSTGRES_PASSWORD"]
POSTGRES_URL = f"jdbc:postgresql://{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Variables de configuración de Redshift
REDSHIFT_HOST = env["REDSHIFT_HOST"]
REDSHIFT_PORT = env["REDSHIFT_PORT"]
REDSHIFT_DB = env["REDSHIFT_DB"]
REDSHIFT_USER = env["REDSHIFT_USER"]
REDSHIFT_PASSWORD = env["REDSHIFT_PASSWORD"]
REDSHIFT_URL = f"jdbc:postgresql://{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}?user={REDSHIFT_USER}&password={REDSHIFT_PASSWORD}"


# ============================= CODIGO =============================
class ETL_Spark:
    # Path del driver de Postgres para Spark (JDBC) (También sirve para Redshift)
    DRIVER_PATH = env["DRIVER_PATH"]
    JDBC_DRIVER = "org.postgresql.Driver"

    def __init__(self, job_name=None):
        """
        Constructor de la clase, inicializa la sesión de Spark
        """
        print(">>> [init] Inicializando ETL...")

        env[
            "PYSPARK_SUBMIT_ARGS"
        ] = f"--driver-class-path {self.DRIVER_PATH} --jars {self.DRIVER_PATH} pyspark-shell"
        env["SPARK_CLASSPATH"] = self.DRIVER_PATH

        # Crear sesión de Spark
        self.spark = (
            SparkSession.builder.master("local[1]")
            .appName("ETL Spark" if job_name is None else job_name)
            .config("spark.jars", self.DRIVER_PATH)
            .config("spark.executor.extraClassPath", self.DRIVER_PATH)
            .getOrCreate()
        )

        # try:
        #     self.conn_postgres = connect(
        #         host=POSTGRES_HOST,
        #         port=POSTGRES_PORT,
        #         database=POSTGRES_DB,
        #         user=POSTGRES_USER,
        #         password=POSTGRES_PASSWORD,
        #     )
        # except:
        #     print(">>> [init] No se pudo conectar a Postgres")

        try:
            self.conn_redshift = connect(
                host=REDSHIFT_HOST,
                port=REDSHIFT_PORT,
                database=REDSHIFT_DB,
                user=REDSHIFT_USER,
                password=REDSHIFT_PASSWORD,
            )
        except:
            print(">>> [init] No se pudo conectar a Redshift")

    def execute_create_table(self, table_name, query):
        """
        Ejecuta la creación de la tabla en Postgres
        """
        print(f">>> [execute_create_table] Creando tabla {table_name} en Postgres...")

        # Crear cursor
        try:
            cursor = self.conn_redshift.cursor()
        except:
            print(">>> [execute_create_table] No se pudo crear el cursor de Redshift")
            return

        # Crear tabla
        try:
            cursor.execute(query)
            cursor.commit()
        except:
            print(
                f">>> [execute_create_table] No se pudo crear la tabla {table_name} en Redshift"
            )
            print(f">>> [execute_create_table] Query: {self.CREATE_TABLE}")
            return
        finally:
            # Cerrar cursor
            cursor.close()

    def execute(self):
        """
        Método principal que ejecuta el ETL
        """
        print(">>> [execute] Ejecutando ETL...")

        # Extraemos datos de la API
        df_api = self.extract()

        # Transformamos los datos
        df_transformed = self.transform(df_api)

        # Cargamos los datos en Redshift
        self.load(df_transformed)

    def extract(self):
        """
        Extrae datos de la API
        """
        print(">>> [E] Extrayendo datos de la API...")

    def transform(self, df_original):
        """
        Transforma los datos
        """
        print(">>> [T] Transformando datos...")

    def load(self, df_final):
        """
        Carga los datos transformados en Redshift
        """
        print(">>> [L] Cargando datos en Redshift...")


class ETL_Pandas:
    def __init__(self):
        """
        Constructor de la clase, inicializa la sesión de Spark
        """
        print(">>> [init] Inicializando ETL...")

    def execute(self):
        """
        Método principal que ejecuta el ETL
        """
        print(">>> [execute] Ejecutando ETL...")

        # Extraemos datos de la API
        df_api = self.extract()

        # Transformamos los datos
        df_transformed = self.transform(df_api)

        # Cargamos los datos en Redshift
        self.load(df_transformed)

    def extract(self):
        """
        Extrae datos de la API
        """
        print(">>> [E] Extrayendo datos de la API...")

    def transform(self, df_original):
        """
        Transforma los datos
        """
        print(">>> [T] Transformando datos...")

    def load(self, df_final):
        """
        Carga los datos transformados en Redshift
        """
        print(">>> [L] Cargando datos en Redshift...")
