from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import extract, transform, load

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_flight_data(**kwargs):
    data = extract.get_flight_data()
    kwargs['ti'].xcom_push(key='flight_data', value=data)

def transform_flight_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='flight_data', task_ids='extract_flight_data')
    transformed_data = transform.process_flight_data(data)
    kwargs['ti'].xcom_push(key='transformed_data', value=transformed_data)

def load_flight_data(**kwargs):
    transformed_data = kwargs['ti'].xcom_pull(key='transformed_data', task_ids='transform_flight_data')
    load.save_flight_data(transformed_data)

with DAG('flight_etl_dag',
         default_args=default_args,
         schedule_interval='* * * * *',  # every 1 minute
         catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract_flight_data',
        python_callable=extract_flight_data,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id='transform_flight_data',
        python_callable=transform_flight_data,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id='load_flight_data',
        python_callable=load_flight_data,
        provide_context=True,
    )

    extract_task >> transform_task >> load_task
