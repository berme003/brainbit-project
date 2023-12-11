import pandas as pd

def load_and_clean_data(file_name):
    data = pd.read_csv(file_name)
    num_columns = min(len(data.columns), len(user2_data.columns))
    data = data[data.columns[:num_columns]]
    return data

def calculate_column_means(data):
    mean_values = data.mean()
    return mean_values

def replace_zero_values(data, mean_values):
    for column in data.columns:
        data[column] = data[column].apply(lambda x: mean_values[column] if x == 0 else x)
    return data

def calculate_percentage_difference(user1_data, user2_data):
    results = {}
    for column in user1_data.columns:
        numerator = abs(abs(user1_data[column]) - abs(user2_data[column]))
        denominator = abs(abs(user1_data[column]) + abs(user2_data[column])) / 2
        results[column] = (numerator / denominator) * 100
    return pd.DataFrame(results)

def save_results_to_csv(result_df, output_file):
    result_df.to_csv(output_file, index=False)
    print(f"Data has been saved to {output_file}.")

# Example usage
user1_data = load_and_clean_data('parsed_data.csv')
user2_data = load_and_clean_data('parsed_data2.csv')

mean_values_user1 = calculate_column_means(user1_data)
mean_values_user2 = calculate_column_means(user2_data)

user1_data = replace_zero_values(user1_data, mean_values_user1)
user2_data = replace_zero_values(user2_data, mean_values_user2)

result_df = calculate_percentage_difference(user1_data, user2_data)
save_results_to_csv(result_df, 'percentage_difference.csv')
