# Este script está pensado para correr en Spark y hacer el proceso de ETL de la tabla users

import requests
import json
import os
from datetime import datetime, timedelta

from commons import ETL_Spark

class ETL_Users(ETL_Spark):

    def __init__(self, job_name=None):
        super().__init__(job_name)
    
    def run(self):
        process_date = "2023-07-09" # datetime.now().strftime("%Y-%m-%d")
        self.execute(process_date)

if __name__ == "__main__":
    print("Corriendo script")
    etl = ETL_Users()
    etl.run()