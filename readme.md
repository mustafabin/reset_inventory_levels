# Inventory CSV Data Modifier

This script is designed to modify a CSV file containing inventory data. It reads the data from the input CSV file, updates specified columns with new values, and then saves the modified data to a new CSV file.

## Prerequisites

* Python 3.x
* Pandas library

## Usage

1. Make sure you have Python and the Pandas library installed.
2. Place the input CSV file (`inventory_export_1.csv`) in the same directory as the script.
3. Run the script using the following command:

   ```python
   python modify_inventory.py
   ```
4. The script will read the data from the input CSV file, update the columns specified in `headers_to_edit` list with default values of 0, and save the modified data to a new CSV file (`modified_levels.csv`).

## Configuration

You can customize the script by editing the following variables:

* `headers_to_edit`: List of headers/columns that you want to update with new values.
* `csv_path`: Path to the input CSV file.
* `modified_csv_path`: Path to save the modified CSV file.

## Example

Suppose the input CSV file (`inventory_export_1.csv`) contains the following data:

| Product | Incoming | Unavailable | Committed | Available | On hand |
| ------- | -------- | ----------- | --------- | --------- | ------- |
| Item A  | 10       | 5           | 3         | 2         | 15      |
| Item B  | 8        | 2           | 1         | 5         | 10      |

Running the script will update the specified columns with default values of 0 and save the modified data to `modified_levels.csv`.
