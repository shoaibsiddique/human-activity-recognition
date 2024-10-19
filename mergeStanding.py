import pandas as pd
import os

# Define folder path for "Standing" activity
standing_folder = "Standing/"

# List of file names for the "Standing" activity
standing_files = [
    "log-2024.10.10.19.26.55.txt",
    "log-2024.10.11.20.59.01.txt",
    "log-2024.10.14.09.41.00.txt",
    "log-2024.10.14.10.03.25.txt"
]

# Create an empty list to store DataFrames
df_list = []

# Iterate over each file, load it, and merge
for file in standing_files:
    file_path = os.path.join(standing_folder, file)  # Join folder path and file name
    df = pd.read_csv(file_path, sep=",", header=0)  # Load the file
    df['Activity'] = 'Standing'  # Add a column for the activity label
    df_list.append(df)  # Add DataFrame to the list

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined DataFrame to a new CSV file for future use
combined_df.to_csv("combined_standing_data.csv", index=False)

# Display the first few rows to confirm the merge was successful
print(combined_df.head())
