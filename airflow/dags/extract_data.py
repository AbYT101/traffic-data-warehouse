from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'Abraham Teka',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    'extract_data_dag',
    default_args=default_args,
    description='A DAG to extract data form the database',
    schedule_interval=None,
)

# Define BashOperator tasks for each environment
# Production Task
prod_load_data = BashOperator(
    task_id='prod_load_data',
    bash_command='python /path/to/your/load_script.py --environment prod',
    dag=dag,
)

# Development Task
dev_load_data = BashOperator(
    task_id='dev_load_data',
    bash_command='python /path/to/your/load_script.py --environment dev',
    dag=dag,
)

# Staging Task
staging_load_data = BashOperator(
    task_id='staging_load_data',
    bash_command='python /path/to/your/load_script.py --environment staging',
    dag=dag,
)

# Define task dependencies
staging_load_data >> dev_load_data >> prod_load_data
