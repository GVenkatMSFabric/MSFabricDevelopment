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

# Path to the Excel file
file_path = "/lakehouse/default/Files/ExcelSourceInfo/Dept_PythonTest.xlsx"

# Read all sheets
sheets_dict = pd.read_excel(file_path, sheet_name=None)

# Access data from each sheet
for sheet_name, df in sheets_dict.items():
    print(f"Sheet Name: {sheet_name}")
    print(df.head()) 

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

specific_sheets = pd.read_excel(file_path, sheet_name=[0, 1])   
 
sheet0_df = specific_sheets[0]
sheet1_df = specific_sheets[1]

print(sheet0_df.head())
print(sheet1_df.head())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

combined_df = pd.concat(sheets_dict.values(), ignore_index=True)
display(combined_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
