from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'Abraham Teka',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_transformations',
    default_args=default_args,
    description='Run dbt transformations',
    schedule_interval='@daily',
)

def run_dbt():
    subprocess.run(['dbt', 'run', '--profile=my_dwh_profile'])

def generate_dbt_docs():
    subprocess.run(['dbt', 'docs', 'generate', '--profile=my_dwh_profile'])

def serve_dbt_docs():
    subprocess.run(['dbt', 'docs', 'serve', '--profile=my_dwh_profile', '--port', '8080'])

# Define PythonOperators to execute dbt commands
run_dbt_command = PythonOperator(
    task_id='run_dbt_command',
    python_callable=run_dbt,
    dag=dag,
)

generate_dbt_docs = PythonOperator(
    task_id='generate_dbt_docs',
    python_callable=generate_dbt_docs,
    dag=dag,
)

serve_dbt_docs = PythonOperator(
    task_id='serve_dbt_docs',
    python_callable=serve_dbt_docs,
    dag=dag,
)

# Set task dependencies
run_dbt_command >> generate_dbt_docs >> serve_dbt_docs
