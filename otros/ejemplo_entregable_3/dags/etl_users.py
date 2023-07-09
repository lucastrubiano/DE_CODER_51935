# Este es el DAG que orquesta el ETL de la tabla users

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.spark_operator import SparkSubmitOperator
from airflow.operators.batch_operator import BashOperator

from datetime import datetime, timedelta

defaul_args = {
    'owner': 'Lucas Trubiano',
    'start_date': datetime(2023, 7, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

dag = DAG(
    dag_id='etl_users',
    default_args=defaul_args,
    description='ETL de la tabla users',
    schedule_interval='@daily',
    catchup=False
)

# Tareas

extract = BashOperator(
    task_id='extract',
    bash_command='python3 /opt/airflow/dags/otros/ejemplo_entregable_3/src/extract.py',
    dag=dag
)


