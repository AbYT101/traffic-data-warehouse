from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base 

class DatabaseManager:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def create_database(self, database_name):
        try:
            # Create database if not exists
            self.engine.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
            print(f"Database '{database_name}' created successfully.")
        except Exception as e:
           print(f"Error creating database: {e}")

    def insert_data(self, table_type, data):      
        session = None
        try:           
            session = self.Session()

            # Bulk insert data
            session.bulk_insert_mappings(table_type, data)
            
            session.commit()
            print("Data inserted successfully.")
        except Exception as e:
            if session:
                session.rollback()
            print(f"Error inserting data into database: {e}")
        finally:
            # Close session if it was opened
            if session:
                session.close()
