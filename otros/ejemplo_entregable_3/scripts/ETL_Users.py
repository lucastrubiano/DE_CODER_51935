# Este script está pensado para correr en Spark y hacer el proceso de ETL de la tabla users

import requests
from datetime import datetime, timedelta
from os import environ as env

import yfinance
print("andando con yfinance")

from pyspark.sql.functions import concat, col, lit, when, expr, to_date

from commons import ETL_Spark

class ETL_Users(ETL_Spark):
    def __init__(self, job_name=None):
        super().__init__(job_name)
        self.process_date = datetime.now().strftime("%Y-%m-%d")

    def run(self):
        process_date = "2023-07-09"  # datetime.now().strftime("%Y-%m-%d")
        self.execute(process_date)

    def extract(self):
        """
        Extrae datos de la API
        """
        print(">>> [E] Extrayendo datos de la API...")

        response = requests.get("https://randomuser.me/api/?results=2")
        if response.status_code == 200:
            data = response.json()["results"]
            print(data)
        else:
            print("Error al extraer datos de la API")
            data = []
            raise Exception("Error al extraer datos de la API")

        df = self.spark.read.json(
            self.spark.sparkContext.parallelize(data), multiLine=True
        )
        df.printSchema()
        df.show()

        return df

    def transform(self, df_original):
        """
        Transforma los datos
        """
        print(">>> [T] Transformando datos...")

        df = (
            df_original.select("name", "gender", "dob.age", "email", "nat")
            .withColumnRenamed("nat", "nationality")
        )

        df = df.withColumn(
            "name", concat(col("name.first"), lit(" "), col("name.last"))
        )
        df = df.withColumn(
            "gender", expr("case when gender = 'male' then 'M' else 'F' end")
        )

        df = df.withColumn("is_under_20", df.age < 20)
        df = df.withColumn("is_over_40", df.age > 40)

        df.printSchema()
        df.show()

        return df

    def load(self, df_final):
        """
        Carga los datos transformados en Redshift
        """
        print(">>> [L] Cargando datos en Redshift...")

        # add process_date column
        df_final = df_final.withColumn("process_date", lit(self.process_date))

        df_final.write \
            .format("jdbc") \
            .option("url", env['REDSHIFT_URL']) \
            .option("dbtable", f"{env['REDSHIFT_SCHEMA']}.users") \
            .option("user", env['REDSHIFT_USER']) \
            .option("password", env['REDSHIFT_PASSWORD']) \
            .option("driver", "org.postgresql.Driver") \
            .mode("append") \
            .save()
        
        print(">>> [L] Datos cargados exitosamente")


if __name__ == "__main__":
    print("Corriendo script")
    etl = ETL_Users()
    etl.run()
