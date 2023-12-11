import re
import csv

def parse_headband_data(input_file, output_file):
    pattern = r"O1=([-+]?\d*\.\d+|\d+), O2=([-+]?\d*\.\d+|\d+), T3=([-+]?\d*\.\d+|\d+), T4=([-+]?\d*\.\d+|\d+)"
    o1_data, o2_data, t3_data, t4_data = [], [], [], []

    with open(input_file, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                o1, o2, t3, t4 = map(float, match.groups())
                o1_data.append(o1)
                o2_data.append(o2)
                t3_data.append(t3)
                t4_data.append(t4)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['O1', 'O2', 'T3', 'T4'])
        for o1, o2, t3, t4 in zip(o1_data, o2_data, t3_data, t4_data):
            writer.writerow([o1, o2, t3, t4])

    print(f"Data has been saved to {output_file}.")

# Example usage
parse_headband_data('HeadbandData.csv', 'parsed_data.csv')
