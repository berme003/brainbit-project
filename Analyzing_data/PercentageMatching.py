import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('percentage_difference.csv')

# Remove empty rows at the end of the dataframe
data = data.dropna(how='all')

# Initialize dictionaries to store the counts of averages under the specified range for each column
range_counts = {'O1': 0, 'O2': 0, 'T3': 0, 'T4': 0}

# Define the specified range for each column
range_specifications = {'O1': (0, 30), 'O2': (0, 30), 'T3': (0, 30), 'T4': (0, 30)}

# Calculate the total number of rows
total_rows = len(data)

# Iterate over each column
for column in data.columns:
    if column != 'Group':
        # Get the specified range for the current column
        min_range, max_range = range_specifications[column]

        # Count the number of averages within the specified range
        column_counts = data[(data[column] >= min_range) & (data[column] <= max_range)].shape[0]
        range_counts[column] = column_counts

# Create a bar chart to display the range counts for each column
plt.figure(figsize=(8, 6))
plt.bar(range(len(range_counts)), range_counts.values())
plt.xticks(range(len(range_counts)), range_counts.keys())
plt.xlabel('Columns')
plt.ylabel('Number of Averages in Specified Range')
plt.title('Number of Averages in Specified Range for Each Column')
plt.show()

# Display the total counts for each column
for column, count in range_counts.items():
    total = total_rows
    print(f"Total number of averages in the specified range for {column}: {count} out of {total}")
