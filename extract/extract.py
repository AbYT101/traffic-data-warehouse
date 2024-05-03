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

from utils.data_utils import read_csv_from_project, load_vehicle_data, load_vehicle_path_data



def extract_data_from_csv(filename = 'extract/data_files/traffic-data.csv'):
    csv_data = read_csv_from_project(filename)
    print(csv_data)

    vehicle_data = load_vehicle_data(csv_data)
    vehicle_path_data = load_vehicle_path_data(csv_data)

    return vehicle_data, vehicle_path_data

