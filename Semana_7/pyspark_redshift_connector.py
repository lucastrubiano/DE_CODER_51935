# Script de Python para trabajar con Redshift desde Spark (Pyspark)
# Autor: @lucastrubiano

# Importamos las librerías necesarias
from os import environ as env
from pyspark.sql import SparkSession
# from pyspark.sql.types import *
# from pyspark.sql.functions import *

class my_ETL():

    DRIVER_PATH = env['DRIVER_PATH']

    # Variables de configuración de Postgres
    POSTGRES_HOST = env['POSTGRES_HOST']
    POSTGRES_PORT = env['POSTGRES_PORT']
    POSTGRES_DB = env['POSTGRES_DB']
    POSTGRES_USER = env["POSTGRES_USER"]
    POSTGRES_PASSWORD = env["POSTGRES_PASSWORD"]
    POSTGRES_DRIVER = "org.postgresql.Driver"
    POSTGRES_URL = f"jdbc:postgresql://{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Variables de configuración de Redshift
    REDSHIFT_HOST = env['REDSHIFT_HOST']
    REDSHIFT_PORT = env['REDSHIFT_PORT']
    REDSHIFT_DB = env['REDSHIFT_DB']
    REDSHIFT_USER = env["REDSHIFT_USER"]
    REDSHIFT_PASSWORD = env["REDSHIFT_PASSWORD"]
    # REDSHIFT_DRIVER = "io.github.spark_redshift_community.spark.redshift"
    REDSHIFT_URL = f"jdbc:redshift://{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}?user={REDSHIFT_USER}&password={REDSHIFT_PASSWORD}"

    def __init__(self):

        env['PYSPARK_SUBMIT_ARGS'] = f'--driver-class-path {self.DRIVER_PATH} --jars {self.DRIVER_PATH} pyspark-shell'
        env['SPARK_CLASSPATH'] = self.DRIVER_PATH

        # Crear sesión de Spark
        self.spark = SparkSession.builder \
                .master("local[1]") \
                .appName("Spark y Redshift") \
                .config("spark.jars", self.DRIVER_PATH) \
                .config("spark.executor.extraClassPath", self.DRIVER_PATH) \
                .getOrCreate()

    
    def execute(self):
        print("Ejecutando ETL")

if __name__ == "__main__":
    """
    Como ejecutar el script:
    spark-submit --driver-class-path $DRIVER_PATH --jars $DRIVER_PATH pyspark_redshift_connector.py
    """
    # Instanciamos la clase
    etl = my_ETL()
    # Ejecutamos el método execute
    etl.execute()