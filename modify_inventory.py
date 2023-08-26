import pandas as pd

headers_to_edit = ['Incoming','Unavailable','Committed','Available', 'On hand']

csv_path = 'inventory_export_1.csv'
print("Reading CSV file from path: " + csv_path)
data = pd.read_csv(csv_path)


for header in headers_to_edit:
    data[header] = 0

# Save the modified DataFrame back to a CSV file
modified_csv_path = 'modified_levels.csv'
print("Saving new CSV file to: " + modified_csv_path)
data.to_csv(modified_csv_path, index=False)

print("Fields edited and saved successfully.")
