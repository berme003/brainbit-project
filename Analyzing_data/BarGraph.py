import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('percentage_difference.csv')

# Initialize a dictionary to store counts for each column
column_counts = {col: 0 for col in data.columns if col != 'Group'}

# Initialize a variable to store the total number of groups of 10
total_groups = 0

# Iterate over the data
for i in range(0, len(data), 10):
    group_data = data.iloc[i:i+10]

    for col in column_counts:
        if (group_data[col] < 100).all():
            column_counts[col] += 1

    total_groups += 1

# Display the counts for each column
for column, count in column_counts.items():
    print(f"Number of averages under 100 for {column}: {count} out of {total_groups}")
