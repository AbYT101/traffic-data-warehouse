import psycopg2
import csv

def load_data_to_database(csv_file_path, database_table):
    # Database connection parameters
    db_params = {
        'host': 'your_database_host',
        'database': 'your_database_name',
        'user': 'your_database_user',
        'password': 'your_database_password',
        'port': 'your_database_port'
    }

    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Open CSV file and load data into database
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                # Assuming the order of columns in CSV matches database table
                cursor.execute(
                    f"INSERT INTO {database_table} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    row
                )

        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()
        print("Data loaded successfully.")
    
    except (Exception, psycopg2.Error) as error:
        print("Error loading data to database:", error)

# Example usage
if __name__ == "__main__":
    # Specify CSV file path and database table
    csv_file_path = "path/to/your/csv/file.csv"
    database_table = "your_database_table"

    # Load data to database
    load_data_to_database(csv_file_path, database_table)
