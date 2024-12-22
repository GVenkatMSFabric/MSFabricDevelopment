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
excel_file_path = "/lakehouse/default/Files/MultiExcelData/Dept_PythonTest.xlsx"

# Read all sheets into a dictionary
sheets_dict = pd.read_excel(excel_file_path, sheet_name=None)

# Loop through each sheet and save as a CSV file
for sheet_name, df in sheets_dict.items():
    # Sanitize sheet name for valid file naming
    sanitized_sheet_name = sheet_name.replace(" ", "_").replace("/", "_")
    
    # Create a file name for the CSV
    csv_file_name = f"{sanitized_sheet_name}.csv"
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_name, index=False)
    
    print(f"Saved {sheet_name} as {csv_file_name}")
    print(csv_file_name)
    output_dir = "abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/FinalCSVData/"
    csv_file_name = f"{output_dir}{csv_file_name}"
    print(csv_file_name)
    df.to_csv(csv_file_name, mode='w', header=True, index=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

import pandas as pd
import glob
import os

# Directory containing Excel files
excel_files_path = "/lakehouse/default/Files/TempExcelData/*.xlsx"

# Output directory for CSV files
output_dir = "abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/ExtractExceltoCSV/"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

# Get a list of all Excel files
excel_files = glob.glob(excel_files_path)

# Loop through each Excel file
for file in excel_files:
    # Read all sheets from the Excel file
    sheets_dict = pd.read_excel(file, sheet_name=None)
    
    # Loop through each sheet in the file
    for sheet_name, df in sheets_dict.items():
        # Sanitize sheet name to avoid file naming issues
        sanitized_sheet_name = sheet_name.replace(" ", "_").replace("/", "_")
        
        # Generate a unique CSV file name
        base_name = os.path.splitext(os.path.basename(file))[0]  # Get file name without extension
        csv_file_name = f"{output_dir}{base_name}_{sanitized_sheet_name}.csv"
        
        # Save the sheet as a CSV file
        df.to_csv(csv_file_name, index=False)
        
        print(f"Saved {sheet_name} from {file} as {csv_file_name}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
