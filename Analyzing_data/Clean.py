import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('percentage_difference.csv')

# Remove empty rows at the end of the dataframe
data = data.dropna(how='all')

# Initialize variables to count the number of averages under 100 for each column
column_counts = {'O1': 0, 'O2': 0, 'T3': 0, 'T4': 0}
column_totals = {'O1': 0, 'O2': 0, 'T3': 0, 'T4': 0}

# Initialize lists to store the averages for each column
averages = {'O1': [], 'O2': [], 'T3': [], 'T4': []}

# Calculate the total number of rows
total_rows = len(data)

# Iterate over each column
for column in data.columns:
    if column != 'Group':
        # Initialize an index variable
        i = 0
        # Iterate over the rows in steps of 10
        while i + 10 <= total_rows:
            rows = data[column].iloc[i:i+10]
            average = rows.mean()
            averages[column].append(average)
            column_totals[column] += 1
            if average < 30:
                column_counts[column] += 1
            i += 10

# Create bar charts for each column
for column in data.columns:
    if column != 'Group':
        plt.figure(figsize=(8, 6))
        plt.bar(range(len(averages[column])), averages[column])
        plt.xlabel('Groups of 10 Rows')
        plt.ylabel(f'Average of {column}')
        plt.title(f'Average of {column} for Every 10 Rows')
        plt.show()

# Display the counts for each column
for column, count in column_counts.items():
    print(f"Number of averages under 30 for {column}: {count} out of {column_totals[column]}")
