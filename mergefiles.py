import pandas as pd
import os

# Function to extract the correct date from the filename
def extract_date_from_filename(filename):
    # The filename is in the format 'log-YYYY.MM.DD.HH.MM.SS.txt'
    # Use string slicing to capture the date part correctly
    parts = filename.split('-')[1]  # Extract the "YYYY.MM.DD.HH.MM.SS" part
    year, month, day = parts[:4], parts[5:7], parts[8:10]  # Extract year, month, and day
    return f"{year}-{month}-{day}"  # Format as "YYYY-MM-DD"

# Function to merge all files in a folder and include the LogDate column
def merge_activity_files(folder_path, activity_label, output_filename):
    # List all txt files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    # Create an empty list to store DataFrames
    df_list = []

    # Iterate over each file in the folder, load it, and merge
    for file in files:
        file_path = os.path.join(folder_path, file)  # Full file path
        df = pd.read_csv(file_path, sep=",", header=0)  # Load the file
        df['Activity'] = activity_label  # Add a column for the activity label
        df['LogDate'] = extract_date_from_filename(file)  # Add a column for the logging date
        df_list.append(df)  # Add DataFrame to the list

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)

    # Save the combined DataFrame to a new CSV file for future use
    combined_df.to_csv(output_filename, index=False)

    # Display the first few rows to confirm the merge was successful
    print(f"Combined data for {activity_label}:")
    print(combined_df.head())

# Paths to activity folders (relative to your root folder)
root_folder = r"D:\Shoaib_GDrive\UPWork\Imran Husain - Techoryze (1)\ML Training Human Data\MLTraining"

# Define paths for each activity folder
standing_folder = os.path.join(root_folder, "Standing")
running_folder = os.path.join(root_folder, "Running")
walking_folder = os.path.join(root_folder, "Walking")

# Merge "Standing" files
merge_activity_files(standing_folder, "Standing", "combined_standing_data.csv")

# Merge "Running" files
merge_activity_files(running_folder, "Running", "combined_running_data.csv")

# Merge "Walking" files
merge_activity_files(walking_folder, "Walking", "combined_walking_data.csv")
