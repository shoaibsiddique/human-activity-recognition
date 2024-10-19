import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the datasets
standing_data = pd.read_csv('combined_standing_data.csv')
running_data = pd.read_csv('combined_running_data.csv')
walking_data = pd.read_csv('combined_walking_data.csv')

# Create a sidebar for activity selection
activity = st.sidebar.selectbox("Select Activity", ["Standing", "Running", "Walking"])

# Load the selected dataset
if activity == "Standing":
    data = standing_data
elif activity == "Running":
    data = running_data
else:
    data = walking_data

# Show the first few rows of the dataset
st.write(f"### {activity} Data")
st.write(data.head())

# Individual Plots for Acceleration Data
st.write(f"### {activity}: Acceleration Data Over Time")

# Accel X Plot
st.write("#### Accel X (m/s²)")
fig, ax = plt.subplots()
ax.plot(data['MS'], data['Accel X (m/s²)'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Acceleration X (m/s²)')
st.pyplot(fig)

# Accel Y Plot
st.write("#### Accel Y (m/s²)")
fig, ax = plt.subplots()
ax.plot(data['MS'], data['Accel Y (m/s²)'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Acceleration Y (m/s²)')
st.pyplot(fig)

# Accel Z Plot
st.write("#### Accel Z (m/s²)")
fig, ax = plt.subplots()
ax.plot(data['MS'], data['Accel Z (m/s²)'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Acceleration Z (m/s²)')
st.pyplot(fig)

# Individual Plots for Gyroscope Data
st.write(f"### {activity}: Gyroscope Data Over Time")

# Gyro X Plot
st.write("#### Gyro X (°/s)")
fig, ax = plt.subplots()
ax.plot(data['MS'], data['Gyro X (°/s)'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Gyroscope X (°/s)')
st.pyplot(fig)

# Gyro Y Plot
st.write("#### Gyro Y (°/s)")
fig, ax = plt.subplots()
ax.plot(data['MS'], data['Gyro Y (°/s)'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Gyroscope Y (°/s)')
st.pyplot(fig)

# Gyro Z Plot
st.write("#### Gyro Z (°/s)")
fig, ax = plt.subplots()
ax.plot(data['MS'], data['Gyro Z (°/s)'])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Gyroscope Z (°/s)')
st.pyplot(fig)

# Optional: Add summary statistics or outlier detection as needed
