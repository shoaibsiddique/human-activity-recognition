import pandas as pd
import streamlit as st
import plotly.express as px

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

# Add a combined column of date and time for easier display
data['Date_Time'] = data['LogDate'] + ' | ' + data['MS'].astype(str) + ' ms'

# Display summary statistics on Streamlit and console
st.write(f"### {activity} Summary Statistics")
summary_stats = data.describe()
st.write(summary_stats)
print(f"\nSummary Statistics for {activity}:")
print(summary_stats)

# Outlier detection using Interquartile Range (IQR) method
numeric_data = data.select_dtypes(include=['float64', 'int64'])
Q1 = numeric_data.quantile(0.25)
Q3 = numeric_data.quantile(0.75)
IQR = Q3 - Q1

# Detect outliers: data points outside 1.5 * IQR are considered outliers
outliers = ((numeric_data < (Q1 - 1.5 * IQR)) | (numeric_data > (Q3 + 1.5 * IQR))).sum()

# Display outliers on Streamlit and console
st.write(f"### {activity} Outliers Detected")
st.write(outliers)
print(f"\nOutliers detected in {activity}:")
print(outliers)

# Plot individual graphs with Plotly
st.write(f"### {activity}: Interactive Acceleration Data Over Time")

# Accel X Plot with Plotly (including Date_Time in hover data)
fig_accel_x = px.line(data, x='MS', y='Accel X (m/s²)', title='Accel X (m/s²) over Time', 
                      hover_data={'LogDate': True, 'MS': True, 'Accel X (m/s²)': True}, 
                      labels={'MS': 'Time (ms)', 'Accel X (m/s²)': 'Accel X (m/s²)'})
st.plotly_chart(fig_accel_x)

# Accel Y Plot with Plotly (including Date_Time in hover data)
fig_accel_y = px.line(data, x='MS', y='Accel Y (m/s²)', title='Accel Y (m/s²) over Time', 
                      hover_data={'LogDate': True, 'MS': True, 'Accel Y (m/s²)': True}, 
                      labels={'MS': 'Time (ms)', 'Accel Y (m/s²)': 'Accel Y (m/s²)'})
st.plotly_chart(fig_accel_y)

# Accel Z Plot with Plotly (including Date_Time in hover data)
fig_accel_z = px.line(data, x='MS', y='Accel Z (m/s²)', title='Accel Z (m/s²) over Time', 
                      hover_data={'LogDate': True, 'MS': True, 'Accel Z (m/s²)': True}, 
                      labels={'MS': 'Time (ms)', 'Accel Z (m/s²)': 'Accel Z (m/s²)'})
st.plotly_chart(fig_accel_z)

st.write(f"### {activity}: Interactive Gyroscope Data Over Time")

# Gyro X Plot with Plotly (including Date_Time in hover data)
fig_gyro_x = px.line(data, x='MS', y='Gyro X (°/s)', title='Gyro X (°/s) over Time', 
                     hover_data={'LogDate': True, 'MS': True, 'Gyro X (°/s)': True}, 
                     labels={'MS': 'Time (ms)', 'Gyro X (°/s)': 'Gyro X (°/s)'})
st.plotly_chart(fig_gyro_x)

# Gyro Y Plot with Plotly (including Date_Time in hover data)
fig_gyro_y = px.line(data, x='MS', y='Gyro Y (°/s)', title='Gyro Y (°/s) over Time', 
                     hover_data={'LogDate': True, 'MS': True, 'Gyro Y (°/s)': True}, 
                     labels={'MS': 'Time (ms)', 'Gyro Y (°/s)': 'Gyro Y (°/s)'})
st.plotly_chart(fig_gyro_y)

# Gyro Z Plot with Plotly (including Date_Time in hover data)
fig_gyro_z = px.line(data, x='MS', y='Gyro Z (°/s)', title='Gyro Z (°/s) over Time', 
                     hover_data={'LogDate': True, 'MS': True, 'Gyro Z (°/s)': True}, 
                     labels={'MS': 'Time (ms)', 'Gyro Z (°/s)': 'Gyro Z (°/s)'})
st.plotly_chart(fig_gyro_z)

# Visualizing Outliers using Boxplots
st.write(f"### {activity}: Detecting Outliers using Boxplots")

# Boxplot for Acceleration Data
fig_accel_box = px.box(data, y=['Accel X (m/s²)', 'Accel Y (m/s²)', 'Accel Z (m/s²)'],
                       title='Acceleration Outliers (X, Y, Z)')
st.plotly_chart(fig_accel_box)

# Boxplot for Gyroscope Data
fig_gyro_box = px.box(data, y=['Gyro X (°/s)', 'Gyro Y (°/s)', 'Gyro Z (°/s)'],
                      title='Gyroscope Outliers (X, Y, Z)')
st.plotly_chart(fig_gyro_box)
