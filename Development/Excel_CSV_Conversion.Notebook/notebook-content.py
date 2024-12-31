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

excel_file_path = "/lakehouse/default/Files/MultiExcelData/Dept_PythonTest.xlsx"

sheets_dict = pd.read_excel(excel_file_path, sheet_name=None)

for sheet_name, df in sheets_dict.items():

    sanitized_sheet_name = sheet_name.replace(" ", "_").replace("/", "_")
    
    csv_file_name = f"{sanitized_sheet_name}.csv"
 
    df.to_csv(csv_file_name, index=False)
    
    output_dir = "abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/FinalCSVData/"
    csv_file_name = f"{output_dir}{csv_file_name}"
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

excel_files_path = "/lakehouse/default/Files/TempExcelData/*.xlsx"

output_dir = "abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/ExtractExceltoCSV/"
os.makedirs(output_dir, exist_ok=True)  

excel_files = glob.glob(excel_files_path)


for file in excel_files:

    sheets_dict = pd.read_excel(file, sheet_name=None)
    
    for sheet_name, df in sheets_dict.items():

        sanitized_sheet_name = sheet_name.replace(" ", "_").replace("/", "_")

        base_name = os.path.splitext(os.path.basename(file))[0]   
        csv_file_name = f"{output_dir}{base_name}_{sanitized_sheet_name}.csv"
        
        df.to_csv(csv_file_name, index=False)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
