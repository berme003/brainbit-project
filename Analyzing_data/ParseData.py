import re
import csv

# Define a regular expression pattern to match the data in each row
pattern = r"O1=([-+]?\d*\.\d+|\d+), O2=([-+]?\d*\.\d+|\d+), T3=([-+]?\d*\.\d+|\d+), T4=([-+]?\d*\.\d+|\d+)"

# Initialize lists to store the EEG data for each electrode
o1_data = []
o2_data = []
t3_data = []
t4_data = []

# Open and read the original CSV file
with open('HeadbandData.csv', 'r') as file:
    for line in file:
        # Use regex to find EEG data in each row
        match = re.search(pattern, line)
        if match:
            # Extract EEG amplitudes for each electrode
            o1, o2, t3, t4 = map(float, match.groups())
            o1_data.append(o1)
            o2_data.append(o2)
            t3_data.append(t3)
            t4_data.append(t4)

# Create a new CSV file to save the parsed data
output_file = 'parsed_data.csv'

# Write the data to the new CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['O1', 'O2', 'T3', 'T4'])
    # Write the data for each electrode in rows
    for o1, o2, t3, t4 in zip(o1_data, o2_data, t3_data, t4_data):
        writer.writerow([o1, o2, t3, t4])

print(f"Data has been saved to {output_file}.")
