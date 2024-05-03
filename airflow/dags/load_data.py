from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.python import PythonOperator
import sys
import os


# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Get the grandparent directory
grandparent_dir = os.path.dirname(parent_dir)

# Add the grandparent directory to the system path
sys.path.insert(0, grandparent_dir)

from models.models import Vehicle, VehiclePath
from utils.db_utils import DatabaseManager
from extract.extract import extract_data_from_csv


# Connection profile
database_name = "airflow"
vehicle_table_name = "vehicle"
vehicle_path_table_name = "vehicle_path"
csv_file_path = "extract/data-files/traffic-data.csv"


# Define the connection string
connection_string = 'postgresql+psycopg2://airflow:airflow@localhost:5432/airflow'

# Create an instance of DatabaseManager
db_manager = DatabaseManager(connection_string)

def create_database():
    try:
        db_manager.create_database()
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")

def load_data_into_database():
    try:
        vehicle, vehicle_path = extract_data_from_csv()
        veh = db_manager.insert_data(Vehicle, vehicle)
        path = db_manager.insert_data(VehiclePath, vehicle_path)
        print(veh)
        print(path)
     
    except Exception as e:
        print(f"An error occurred: {e}")

create_database()
load_data_into_database()

# default_args = {
#     'owner': 'Abraham Teka',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 5, 1),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }


# dag = DAG(
#     'create_db_and_load_data_multiple_tables_dag',
#     default_args=default_args,
#     description='A DAG to create a database and load data from CSV into multiple tables',
#     schedule_interval=timedelta(days=1),
# )


# create_db_task = PythonOperator(
#     task_id='create_database',
#     python_callable=create_database,
#     dag=dag,
# )


# load_data_task = PythonOperator(
#     task_id='load_data_into_database',
#     python_callable=load_data_into_database,
#     dag=dag,
# )


# create_db_task >> load_data_task