from datetime import datetime
from email import message
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator

email_success = 'SUCCESS'
email_failure = 'FAILURE'

import smtplib

def simular_error():
    raise Exception('Error')

def enviar_error():
    enviar(email_failure)

def enviar_success():
    enviar(email_success)

def enviar(subject):
    try:
        x=smtplib.SMTP('smtp.gmail.com',587)
        x.starttls()
        x.login(Variable.get('SMTP_EMAIL_FROM'),Variable.get('SMTP_PASSWORD'))
        subject=f'El dag termino en: {subject}'
        body_text=subject
        message='Subject: {}\n\n{}'.format(subject,body_text)
        x.sendmail(Variable.get('SMTP_EMAIL_FROM'),Variable.get('SMTP_EMAIL_TO'),message)
        print('Exito al enviar el mail')
    except Exception as exception:
        print(exception)
        print('Fallo al enviar el mail')

default_args={
    'owner': 'Lucas T',
    'start_date': datetime(2023,7,11),
    'retries': 0,
    'catchup': False,
}

with DAG(
    dag_id='dag_smtp_email_automatico',
    default_args=default_args,
    schedule_interval='@daily') as dag:

    tarea_0=PythonOperator(
        task_id='random_error',
        python_callable=simular_error,
    )

    tarea_1=PythonOperator(
        task_id='dag_envio_error',
        python_callable=enviar_error,
        trigger_rule='all_failed'
    )
    
    tarea_2=PythonOperator(
        task_id='dag_envio_success',
        python_callable=enviar_success,
        trigger_rule='all_success'
    )

    tarea_0 >> [tarea_1,tarea_2]
