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

import requests
import pandas as pd

# Step 1: Define the API endpoint and parameters
url = "https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"

# Step 2: Make the API request
response = requests.get(url)

# Step 3: Check the response status and parse the JSON
if response.status_code == 200:
    json_data = response.json()  # Parse JSON response
else:
    raise Exception(f"API call failed with status code {response.status_code}")

# Step 4: Convert JSON data to Pandas DataFrame
# Assuming the API returns a list of dictionaries
data = json_data["results"]  # Adjust key based on API response structure
df = pd.DataFrame(data)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

df.to_json("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/SourceFilesInfo/Temp.json", orient="records", indent=4)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

df_read = pd.read_json("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/SourceFilesInfo/Temp.json")
print(df_read)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
