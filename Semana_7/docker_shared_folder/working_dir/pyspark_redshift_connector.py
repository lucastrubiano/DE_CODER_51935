# Script de Python para trabajar con Redshift desde Spark (Pyspark)
# Autor: @lucastrubiano

# Importamos las librerías necesarias
from os import environ as env
from os import listdir
from pyspark.sql import SparkSession
# from pyspark.sql.types import *
# from pyspark.sql.functions import *

class my_ETL():

    DRIVER_PATH = "/home/coder/working_dir/spark_drivers/postgresql-42.5.2.jar"

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
    REDSHIFT_DRIVER = "io.github.spark_redshift_community.spark.redshift"
    REDSHIFT_URL = f"jdbc:redshift://{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}?user={REDSHIFT_USER}&password={REDSHIFT_PASSWORD}"

    def __init__(self):

        env['PYSPARK_SUBMIT_ARGS'] = f'--driver-class-path {self.DRIVER_PATH} --jars {self.DRIVER_PATH} pyspark-shell'
        env['SPARK_CLASSPATH'] = self.DRIVER_PATH

        # Crear sesión de Spark
        self.spark = SparkSession.builder \
                .master("local[1]") \
                .appName("Spark y Redshift") \
                .config("spark.executor.memory", "2g") \
                .config("spark.driver.memory", "2g") \
                .config("spark.executor.cores", "2") \
                .config("spark.cores.max", "2") \
                .config("spark.jars", self.DRIVER_PATH) \
                .config("spark.executor.extraClassPath", self.DRIVER_PATH) \
                .getOrCreate()

    
    def execute(self):
        print("Ejecutando ETL")
    
    def migration(self, csv):
        # Listar todos los csv en ./data/
        data_dir = '/home/coder/working_dir/data/'
        csvs = filter(lambda x: x.endswith(".csv"),listdir(data_dir))
        
        for csv in csvs:
            print("Leyendo: ", csv)
            # Crear Dataframes a partir de los csv
            df = self.spark.read \
                        .option("header",True) \
                        .option("inferSchema",True) \
                        .csv(data_dir+csv, )

            # Migrar Dataframes y escribir en Redshift
            print("Escribiendo: ", csv)
            # df.summary().show()

            # exit()
            df.repartition(100).write \
                .format("jdbc") \
                .option("url", f"jdbc:postgresql://{env['REDSHIFT_HOST']}:{env['REDSHIFT_PORT']}/{env['REDSHIFT_DB']}") \
                .option("dbtable", f"{env['REDSHIFT_SCHEMA']}.{csv.replace('.csv','')}") \
                .option("user", env['REDSHIFT_USER']) \
                .option("password", env['REDSHIFT_PASSWORD']) \
                .option("driver", "org.postgresql.Driver") \
                .mode("append") \
                .save()
        
        # modes: overwrite
        print("Terminado...")

if __name__ == "__main__":
    """
    Como ejecutar el script:
    spark-submit --driver-class-path $DRIVER_PATH --jars $DRIVER_PATH pyspark_redshift_connector.py
    """
    # Instanciamos la clase
    print("Instanciamos la clase")
    etl = my_ETL()
    
    # Migrar csv's a tablas
    print("Migrar csv's a tablas")
    etl.migration('productcategory.csv')
    
    # Ejecutamos los ejemplos en vivo
    #etl.execute_vivo1()