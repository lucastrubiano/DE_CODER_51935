from datetime import timedelta,datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator


def _imprimir_pais():
    print('El pais es: Argentina')

def _imprimir_nombres():
    print('Lucas Ezequiel')

def _imprimir_apellido():
    print('Trubiano')

default_args={
    'owner': 'Lucas T',
    'start_date': datetime(2023,6,1),
    'schedule_interval': '@daily',
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
    'catchup': False,
}

with DAG(
    dag_id='dag_comision_jueves',
    default_args=default_args,
    description='DAG con python operators para imprimir mensajes',
    ) as dag:

    imprimir_pais= PythonOperator(
        task_id='imprimir_pais',
        python_callable=_imprimir_pais
    )
    imprimir_nombres= PythonOperator(
        task_id='imprimir_nombres',
        python_callable=_imprimir_nombres
    )
    imprimir_apellido= PythonOperator(
        task_id='imprimir_apellido',
        python_callable=_imprimir_apellido
    )

    imprimir_pais >> imprimir_nombres >> imprimir_apellido
