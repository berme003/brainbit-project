import re
import matplotlib.pyplot as plt
import numpy as np

# Define a regular expression pattern to match the data in each row
pattern = r"O1=([-+]?\d*\.\d+|\d+), O2=([-+]?\d*\.\d+|\d+), T3=([-+]?\d*\.\d+|\d+), T4=([-+]?\d*\.\d+|\d+)"

# Initialize lists to store the EEG data for each electrode
o1_data = []
o2_data = []
t3_data = []
t4_data = []

# Open and read the CSV file
with open('HeadbandData.csv', 'r') as file:
    for line in file:
        # Use regex to find EEG data in each row
        match = re.search(pattern, line)
        if match:
            # Extract EEG amplitudes for each electrode
            o1, o2, t3, t4 = map(float, match.groups())
            o1_data.append(o1)
            o2_data.append(o2)
            t3_data.append(t3)
            t4_data.append(t4)

# Create time points for the x-axis
time_points = np.arange(len(o1_data))

# Plot EEG data for each electrode
plt.figure(figsize=(12, 6))
plt.plot(time_points, o1_data, label='O1')
plt.plot(time_points, o2_data, label='O2')
plt.plot(time_points, t3_data, label='T3')
plt.plot(time_points, t4_data, label='T4')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('EEG Amplitude (V)')
plt.title('EEG Data for O1, O2, T3, and T4 Electrodes')
plt.legend()

# Show the plot
plt.show()


