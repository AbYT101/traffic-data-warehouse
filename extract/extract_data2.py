import pandas as pd
import os


def extract_data(csv_file):
    # Get the directory path of the current script file
    current_dir = os.path.dirname(__file__)
    # Construct the full path to the CSV file
    csv_file_path = os.path.join(current_dir, "./data_files/traffic-data.csv")   

    # Read CSV into DataFrame
    df = pd.read_csv(csv_file_path, delimiter=';', header=None)

    print(df.head())

    # Rename columns
    df.columns = ['track_id', 'type', 'traveled_d', 'avg_speed', 'lat', 'lon', 'speed', 'lon_acc', 'lat_acc', 'time']

    # Extract trajectory data
    trajectory_data = df[['track_id', 'lat', 'lon', 'speed', 'lon_acc', 'lat_acc', 'time']]

    # Extract vehicle information
    vehicle_info = df[['track_id', 'type', 'traveled_d', 'avg_speed']]

    return trajectory_data, vehicle_info

# Example usage:
trajectory_data, vehicle_info = extract_data('sample_data.csv')
print("Trajectory Data:")
print(trajectory_data.head())
print("\nVehicle Information:")
print(vehicle_info.head())
