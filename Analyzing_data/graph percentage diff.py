import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('percentage_difference.csv')

# Separate the columns
O1 = data['O1']
O2 = data['O2']
T3 = data['T3']
T4 = data['T4']

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(O1, label='O1')
plt.plot(O2, label='O2')
plt.plot(T3, label='T3')
plt.plot(T4, label='T4')

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Sample Data')
plt.legend()

# Show the plot
plt.show()
