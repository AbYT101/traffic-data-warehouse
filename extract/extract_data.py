import pandas as pd

def extract_data(csv_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Determine the number of repeated sequences (n)
    num_cols = len(df.columns)
    num_repeated_values = num_cols - 4  # Subtracting the first 4 unique values
    n = num_repeated_values // 6  # Each sequence contains 6 values
    
    # Extract unique vehicle information into a DataFrame
    vehicle_info_df = df.iloc[:, :4].copy()
    
    # Extract trajectory data into a DataFrame
    trajectory_data = df.iloc[:, 4:].values.reshape(-1, 6*n)  # Reshape to 2D array
    trajectory_columns = ['lat', 'lon', 'speed', 'lon_acc', 'lat_acc', 'time']
    trajectory_df = pd.DataFrame(trajectory_data, columns=trajectory_columns)
    
    # Append 'track_id' to each row to keep track of vehicle identity
    vehicle_info_df['track_id'] = df['track_id']
    trajectory_df['track_id'] = df['track_id'].repeat(n)
    
    return vehicle_info_df, trajectory_df

# Example usage:
vehicle_info, trajectory_data = extract_data('your_file.csv')

# Now you have two DataFrames: vehicle_info and trajectory_data
# You can perform further analysis or manipulation on these DataFrames as needed.
