import pandas as pd

def process_percentage_difference(file_name):
    data = pd.read_csv(file_name)
    column_counts = {col: 0 for col in data.columns if col != 'Group'}
    total_groups = 0

    for i in range(0, len(data), 10):
        group_data = data.iloc[i:i+10]

        for col in column_counts:
            if (group_data[col] < 100).all():
                column_counts[col] += 1

        total_groups += 1

    for column, count in column_counts.items():
        print(f"Number of averages under 100 for {column}: {count} out of {total_groups}")

# Example usage
process_percentage_difference('percentage_difference.csv')
