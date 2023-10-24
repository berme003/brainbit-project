import matplotlib.pyplot as plt
import numpy as np

# Sample EEG data
data = [
    [0.4, -0.40000038147009037, 0.03477939107836826, -0.4],
    [0.4, -0.40000038147009037, 0.04727902152921823, -0.4],
    [0.4, -0.40000038147009037, 0.050899554156831894, -0.4],
    [0.4, -0.40000038147009037, 0.0510742674582171, -0.4],
    [0.4, -0.40000038147009037, 0.05039105452638104, -0.4],
    [0.4, -0.3875007510192404, 0.04942822401831057, -0.39642905848413323]
]

# Create time points for the x-axis
time_points = np.arange(len(data))

# Plot EEG data for each electrode
plt.figure(figsize=(12, 6))
plt.plot(time_points, [d[0] for d in data], label='O1')
plt.plot(time_points, [d[1] for d in data], label='O2')
plt.plot(time_points, [d[2] for d in data], label='T3')
plt.plot(time_points, [d[3] for d in data], label='T4')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('EEG Amplitude (V)')
plt.title('EEG Data for O1, O2, T3, and T4 Electrodes')
plt.legend()

# Show the plot
plt.show()
