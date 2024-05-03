import pandas as pd
import sys
from datetime import datetime
import csv

import sys
import os

# Get the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)


def read_csv_from_project(filename):
    # Get the absolute path of the parent directory
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Construct the path to the CSV file in the parent directory
    csv_file_path = os.path.join(parent_directory, filename)
    
    # Check if the file exists
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"File '{filename}' not found in the parent directory.")        
    
    return csv_file_path


def load_vehicle_data(csv_file):
    vehicle_data = []
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                try:
                    track_id = int(row[0])
                    type_vehicle = row[1]
                    traveled_distance = float(row[2])
                    avg_speed = float(row[3])
                    vehicle_data.append({
                        'track_id': track_id,
                        'type': type_vehicle,
                        'traveled_distance': traveled_distance,
                        'avg_speed': avg_speed
                    })
                except (IndexError, ValueError) as e:
                    print(f"Error parsing vehicle data: {e}")
    except Exception as e:
        print(f"Error loading vehicle data from CSV: {e}")
    return vehicle_data


def load_vehicle_path_data(csv_file):
    vehicle_path_data = []
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                try:
                    track_id = int(row[0])
                    for i in range(4, len(row), 6):
                        # Check if any field is empty or contains only whitespace
                        if any(not field.strip() for field in row[i:i+6]):
                            continue
                        lat = float(row[i])
                        lon = float(row[i+1])
                        speed = float(row[i+2])
                        lon_acc = float(row[i+3])
                        lat_acc = float(row[i+4])
                        time = float(row[i+5])

                        vehicle_path_data.append({
                            'track_id': track_id,
                            'lat': lat,
                            'lon': lon,
                            'speed': speed,
                            'lon_acc': lon_acc,
                            'lat_acc': lat_acc,
                            'time': time
                        })
                except (IndexError, ValueError) as e:
                    print(f"Error parsing vehicle path data: {e}")
    except Exception as e:
        print(f"Error loading vehicle path data from CSV: {e}")
    return vehicle_path_data



filename = 'data/traffic-data.csv'
csv_data = read_csv_from_project(filename)
print(csv_data)

vehicle_data = load_vehicle_data(csv_data)
vehicle_path_data = load_vehicle_path_data(csv_data)

print(vehicle_data)
print(vehicle_path_data)