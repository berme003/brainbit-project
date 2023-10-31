import pandas as pd

# Load the data from the CSV files
user1_data = pd.read_csv('parsed_data.csv')
user2_data = pd.read_csv('parsed_data2.csv')

# Ensure both dataframes have the same number of columns
num_columns = min(len(user1_data.columns), len(user2_data.columns))
user1_data = user1_data[user1_data.columns[:num_columns]]
user2_data = user2_data[user2_data.columns[:num_columns]]

# Calculate the mean for each column in both dataframes
mean_values_user1 = user1_data.mean()
mean_values_user2 = user2_data.mean()

# Replace 0 values in both dataframes with the respective column mean
for column in user1_data.columns:
    user1_data[column] = user1_data[column].apply(lambda x: mean_values_user1[column] if x == 0 else x)
    user2_data[column] = user2_data[column].apply(lambda x: mean_values_user2[column] if x == 0 else x)

# Calculate the percentage difference for each electrode with absolute values
results = {
    'O1': (abs(abs(user1_data['O1']) - abs(user2_data['O1'])) / (abs(abs(user1_data['O1']) + abs(user2_data['O1'])) / 2)) * 100,
    'O2': (abs(abs(user1_data['O2']) - abs(user2_data['O2'])) / (abs(abs(user1_data['O2']) + abs(user2_data['O2'])) / 2)) * 100,
    'T3': (abs(abs(user1_data['T3']) - abs(user2_data['T3'])) / (abs(abs(user1_data['T3']) + abs(user2_data['T3'])) / 2)) * 100,
    'T4': (abs(abs(user1_data['T4']) - abs(user2_data['T4'])) / (abs(abs(user1_data['T4']) + abs(user2_data['T4'])) / 2)) * 100
}

# Create a DataFrame to store the results
result_df = pd.DataFrame(results)

# Save the results to a new CSV file
result_df.to_csv('percentage_difference.csv', index=False)
