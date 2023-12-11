import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_name):
    data = pd.read_csv(file_name)
    return data.dropna(how='all')

def count_averages_in_range(data, range_specifications):
    range_counts = {column: 0 for column in data.columns if column != 'Group'}
    total_rows = len(data)

    for column in data.columns:
        if column != 'Group':
            min_range, max_range = range_specifications[column]
            column_counts = data[(data[column] >= min_range) & (data[column] <= max_range)].shape[0]
            range_counts[column] = column_counts

    return range_counts, total_rows

def plot_range_counts(range_counts):
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(range_counts)), range_counts.values())
    plt.xticks(range(len(range_counts)), range_counts.keys())
    plt.xlabel('Columns')
    plt.ylabel('Number of Averages in Specified Range')
    plt.title('Number of Averages in Specified Range for Each Column')
    plt.show()

def display_total_counts(range_counts, total_rows):
    for column, count in range_counts.items():
        total = total_rows
        print(f"Total number of averages in the specified range for {column}: {count} out of {total}")

# Example usage
file_name = 'percentage_difference.csv'
data = load_data(file_name)

range_specifications = {'O1': (0, 30), 'O2': (0, 30), 'T3': (0, 30), 'T4': (0, 30)}
range_counts, total_rows = count_averages_in_range(data, range_specifications)

plot_range_counts(range_counts)
display_total_counts(range_counts, total_rows)
