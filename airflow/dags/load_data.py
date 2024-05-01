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
    'load_data_dag',
    default_args=default_args,
    description='A DAG to load data files into the database',
    schedule_interval=None,
)

# Define BashOperator tasks for each environment
# Production Task
# transform_data = BashOperator(
#     task_id='prod_load_data',
#     bash_command='python /path/to/your/load_script.py --environment prod',
#     dag=dag,
# )

# Development Task
transform_data_dbt = BashOperator(
    task_id='transform_data_dbt',
    bash_command='python /path/to/your/load_script.py --environment dev',
    dag=dag,
)

# Development Task
load_data_dev = BashOperator(
    task_id='load_data_dev',
    bash_command='python /path/to/your/load_script.py --environment dev',
    dag=dag,
)

# Development Task
load_data_staging = BashOperator(
    task_id='load_data_staging',
    bash_command='python /path/to/your/load_script.py --environment dev',
    dag=dag,
)

# Staging Task
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='python /path/to/your/load_script.py --environment staging',
    dag=dag,
)



# Define task dependencies
extract_data >> [load_data_staging, load_data_dev] >> transform_data_dbt
