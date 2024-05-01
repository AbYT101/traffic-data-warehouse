import pandas as pd
import os
import sys

# Get the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from extract.extractor import DataExtractor

# Get the path of the CSV file in the same folder as the DAG script
csv_file_path = os.path.join(os.path.dirname(__file__), 'traffic-data.csv')


# Step 1: Read CSV file
file_path = "path/to/your/csv/file.csv"
df = pd.read_csv(csv_file_path, delimiter=';')

# Step 2: Handle missing values
# For demonstration purposes, let's fill missing values with zeros
df.fillna(0, inplace=True)

# Step 3: Correct data types
# Assuming the first four columns are numeric except for the first column (trackID)
numeric_columns = df.columns[1:4] + df.columns[5:]  # Exclude the first column (trackID)
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

# Convert time-related columns to datetime format if applicable
# Assuming the time-related columns start from the 5th column
time_columns = df.columns[4::6]  # Assuming trajectory data starts from the 5th column and repeats every 6 columns
df[time_columns] = df[time_columns].apply(pd.to_datetime, unit='s')  # Assuming time is in seconds

# Step 4: Separate trajectory data and vehicle information
# Assuming the first four columns are vehicle information and the rest are trajectory data
vehicle_info_columns = df.columns[:4]
trajectory_columns = df.columns[4:]

# Create separate dataframes for vehicle information and trajectory data
vehicle_info_df = df[vehicle_info_columns]
trajectory_df = df[trajectory_columns]

# Step 5: Save cleaned and transformed dataframes to new CSV files
vehicle_info_output_file_path = os.path.join(os.path.dirname(__file__), 'vehicle-info.csv')
trajectory_output_file_path = os.path.join(os.path.dirname(__file__), 'trajectory_data.csv')
vehicle_info_df.to_csv(vehicle_info_output_file_path, index=False)
trajectory_df.to_csv(trajectory_output_file_path, index=False)

# Optional: Display the first few rows of the new dataframes
print("Vehicle Information DataFrame:")
print(vehicle_info_df.head())

print("\nTrajectory Data DataFrame:")
print(trajectory_df.head())


