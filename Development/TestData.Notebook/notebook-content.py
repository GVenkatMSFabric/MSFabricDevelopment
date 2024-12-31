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
import json

# Load the JSON file
file_path = '/lakehouse/default/Files/JsonFilesData/TestData/TestFile.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Flatten the JSON data
employee_data = pd.json_normalize(data["Employee"])

# Normalize nested "AttributeData" field
attribute_data = pd.json_normalize(data["Employee"], 'AttributeData', ['EmpId', 'EmpName'])

# Normalize nested "Department" within "AttributeData"
department_data = pd.json_normalize(data["Employee"], 
                                    record_path=['AttributeData', 'Department'], 
                                    meta=['EmpId', 'EmpName'])
department_data['Id'] = attribute_data['Id']
department_data['Name'] = attribute_data['Name']
display(department_data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

import os
import pandas as pd
import json

# Directory containing the JSON files
directory_path = '/lakehouse/default/Files/JsonFilesData/TestData/'  # Adjust as per your file location

# Lists to store processed data from all files
employee_data_list = []
attribute_data_list = []
department_data_list = []

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):  # Process only JSON files
        file_path = os.path.join(directory_path, filename)
        
        # Load the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Flatten the main "Employee" field
        employee_data = pd.json_normalize(data["Employee"])
        employee_data_list.append(employee_data)
        
        # Normalize the "AttributeData" field
        attribute_data = pd.json_normalize(data["Employee"], 'AttributeData', ['EmpId', 'EmpName'])
        attribute_data_list.append(attribute_data)
        
        # Normalize the "Department" field inside "AttributeData"
        department_data = pd.json_normalize(data["Employee"], 
                                            record_path=['AttributeData', 'Department'], 
                                            meta=['EmpId', 'EmpName'])
        department_data['Id'] = attribute_data['Id']
        department_data['Name'] = attribute_data['Name']
        department_data_list.append(department_data)

# Combine all data into single DataFrames
# employee_data = pd.concat(employee_data_list, ignore_index=True)
# attribute_data = pd.concat(attribute_data_list, ignore_index=True)
department_data = pd.concat(department_data_list, ignore_index=True)

display(department_data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
