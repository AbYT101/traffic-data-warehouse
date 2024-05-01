import os
import sys
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

cwd=os.getcwd()
sys.path.append(f'../scripts/')
sys.path.append(f'../pgsql/')
sys.path.append(f'../temp_storage/')
sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))

# Add the parent directory to the system path

import utils.db_utils

from extract.extractor import DataExtractor

data_extractor=DataExtractor()

# def separate_data(ti):
# data_extractor.separate(file_name='20181024_d1_0830_0900.csv',number=5)

def extract_data(ti):

    loaded_df_name=data_extractor.extract_data(file_name='20181024_d1_0830_0900.csv',return_json=True)
    trajectory_file_name,vehicle_file_name=loaded_df_name
   
    ti.xcom_push(key="trajectory",value=trajectory_file_name)
    ti.xcom_push(key="vehicle",value=vehicle_file_name)

def create_table():
    db_util.create_table()

def populate__vehicles_table(ti):
    trajectory_file_name = ti.xcom_pull(key="trajectory",task_ids='extract_from_file')
    # vehicle_file_name = ti.xcom_pull(key="vehicle",task_ids='extract_from_file')
    # trajectory_data,vehicle_data=combined_df['trajectory'], combined_df['vehicle']
    db_util.insert_to_table(trajectory_file_name, 'trajectories',from_file=True)
    # db_util.insert_to_table(vehicle_file_name, 'vehicles',from_file=True)

def populate_trajectory_table(ti):
    # trajectory_file_name = ti.xcom_pull(key="trajectory",task_ids='extract_from_file')
    vehicle_file_name = ti.xcom_pull(key="vehicle",task_ids='extract_from_file')
    # trajectory_data,vehicle_data=combined_df['trajectory'], combined_df['vehicle']
    # db_util.insert_to_table(trajectory_file_name, 'trajectories',from_file=True)
    db_util.insert_to_table(vehicle_file_name, 'vehicles',from_file=True)

def clear_memory_vehicle(ti):
    trajectory_file_name = ti.xcom_pull(key="trajectory",task_ids='extract_from_file')
    # vehicle_file_name = ti.xcom_pull(key="vehicle",task_ids='extract_from_file')

    os.remove(f'../temp_storage/{trajectory_file_name}')
    # os.remove(f'../temp_storage/{vehicle_file_name}')

def clear_memory_trajectory(ti):
    # trajectory_file_name = ti.xcom_pull(key="trajectory",task_ids='extract_from_file')
    vehicle_file_name = ti.xcom_pull(key="vehicle",task_ids='extract_from_file')

    # os.remove(f'../temp_storage/{trajectory_file_name}')
    os.remove(f'../temp_storage/{vehicle_file_name}')

# Specifing the default_args
default_args = {
    'owner': 'Abraham',
    'depends_on_past': False,
    'email': ['aberrhamyirsaw@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    dag_id='extractor_loader_pg',
    default_args=default_args,
    description='this loads our data to the database',
    start_date=datetime(2024,5,1,4),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    read_data = PythonOperator(
        task_id='extract_from_file',
        python_callable = extract_data,
    ) 
    
    create_tables = PythonOperator(
        task_id='create_table',
        python_callable = create_table
    )
    
    populate_vehicles = PythonOperator(
        task_id='load_vehicle_data',
        python_callable = populate__vehicles_table
    )
    
    populate_trajectory = PythonOperator(
        task_id='load_trajectory_data',
        python_callable = populate_trajectory_table
    ) 

    clear_temp_vehicle_data = PythonOperator(
        task_id='delete_temp_vehicle_files',
        python_callable = clear_memory_vehicle
    )
    clear_temp_trajectory_data = PythonOperator(
        task_id='delete_temp_trajectory_files',
        python_callable = clear_memory_trajectory
    )

    [read_data,create_tables]>>populate_vehicles>>clear_temp_vehicle_data,populate_vehicles>>populate_trajectory>>clear_temp_trajectory_data
    