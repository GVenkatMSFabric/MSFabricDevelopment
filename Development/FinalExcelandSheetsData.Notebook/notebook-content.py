# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.11"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "5b9f77a2-8b6d-4400-a5a7-1f9f8bcdac66",
# META       "default_lakehouse_name": "TempLakehouse",
# META       "default_lakehouse_workspace_id": "636a293c-b141-4586-887c-b60d7f65acb8"
# META     }
# META   }
# META }

# CELL ********************

import pandas as pd
import glob

# Path to the directory containing Excel files
file_path = "/lakehouse/default/Files/MultiExcelData/*.xlsx"

# Get list of all Excel files in the directory
excel_files = glob.glob(file_path)

# Dictionary to store data from each file and sheet
all_data = {}

for file in excel_files:
    # Read all sheets from the current Excel file
    sheets_dict = pd.read_excel(file, sheet_name=None)
    
    # Add data to the all_data dictionary
    all_data[file] = sheets_dict

# Example: Access data from a specific file and sheet
for file, sheets in all_data.items():
    for sheet_name, df in sheets.items():
        print(f"File: {file}, Sheet: {sheet_name}")
        print(df.head())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

combined_data = []

for file in excel_files:
    # Read all sheets from the current Excel file
    sheets_dict = pd.read_excel(file, sheet_name=None)
    
    for sheet_name, df in sheets_dict.items():
        # Add file name and sheet name as columns for context
        df["File Name"] = file
        df["Sheet Name"] = sheet_name
        combined_data.append(df)

# Combine all DataFrames into one
final_df = pd.concat(combined_data, ignore_index=True)

display(final_df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

specific_sheets = ["Dept", "Sales"]
combined_data = []

for file in excel_files:
    # Read specific sheets
    sheets_dict = pd.read_excel(file, sheet_name=specific_sheets)
    
    for sheet_name, df in sheets_dict.items():
        # Add file name and sheet name as columns for context
        df["File Name"] = file
        df["Sheet Name"] = sheet_name
        combined_data.append(df)

# Combine all DataFrames into one
final_df = pd.concat(combined_data, ignore_index=True)
display(final_df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
