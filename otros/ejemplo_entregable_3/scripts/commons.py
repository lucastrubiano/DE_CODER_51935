from os import environ as env
from psycopg2 import connect
from pyspark.sql import SparkSession

# Variables de configuración de Redshift
REDSHIFT_HOST = env["REDSHIFT_HOST"]
REDSHIFT_PORT = env["REDSHIFT_PORT"]
REDSHIFT_DB = env["REDSHIFT_DB"]
REDSHIFT_USER = env["REDSHIFT_USER"]
REDSHIFT_PASSWORD = env["REDSHIFT_PASSWORD"]
REDSHIFT_URL = env["REDSHIFT_URL"]


class ETL_Spark:
    # Path del driver de Postgres para Spark (JDBC) (También sirve para Redshift)
    DRIVER_PATH = env["DRIVER_PATH"]
    JDBC_DRIVER = "org.postgresql.Driver"

    def __init__(self, job_name=None):
        """
        Constructor de la clase, inicializa la sesión de Spark
        """
        print(">>> [init] Inicializando ETL...")

        env["SPARK_CLASSPATH"] = self.DRIVER_PATH

        env[
            "PYSPARK_SUBMIT_ARGS"
        ] = f"--driver-class-path {self.DRIVER_PATH} --jars {self.DRIVER_PATH} pyspark-shell"

        # Crear sesión de Spark
        self.spark = (
            SparkSession.builder.master("local[1]")
            .appName("ETL Spark" if job_name is None else job_name)
            .config("spark.jars", self.DRIVER_PATH)
            .config("spark.executor.extraClassPath", self.DRIVER_PATH)
            .getOrCreate()
        )

        try:
            # Conectar a Redshift
            print(">>> [init] Conectando a Redshift...")
            self.conn_redshift = connect(
                host=REDSHIFT_HOST,
                port=REDSHIFT_PORT,
                database=REDSHIFT_DB,
                user=REDSHIFT_USER,
                password=REDSHIFT_PASSWORD,
            )
            self.cur_redshift = self.conn_redshift.cursor()
            print(">>> [init] Conexión exitosa")
            # Cerrar la conexión
            self.cur_redshift.close()
            self.conn_redshift.close()
        except:
            print(">>> [init] No se pudo conectar a Redshift")

    def execute(self, process_date: str):
        """
        Método principal que ejecuta el ETL

        Args:
            process_date (str): Fecha de proceso en formato YYYY-MM-DD
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
