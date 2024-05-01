from sqlalchemy import create_engine, Table, Column, MetaData
import pandas as pd

def load_data_to_postgres():
    # Define SQLAlchemy engine
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/traffic-data')

    # Load CSV file into a DataFrame
    df = pd.read_csv('../../extract/data_files/traffic-data.csv')

    # Specify table name and metadata
    metadata = MetaData()
    table = Table('traffic-data', metadata, autoload=True, autoload_with=engine)

    # Insert data into the PostgreSQL table
    with engine.connect() as conn:
        df.to_sql('traffic-data', conn, if_exists='append', index=False)

load_data_task = PythonOperator(
    task_id='load_data_to_postgres',
    python_callable=load_data_to_postgres,
    dag=dag
)
