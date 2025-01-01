# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
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
from pyspark.sql import SparkSession

# Step 2: Make the API call
url = "https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"

response = requests.get(url)

# Step 3: Parse the JSON response
if response.status_code == 200:
    json_data = response.json()
else:
    raise Exception(f"API call failed with status code {response.status_code}")

# Step 4: Convert JSON data to Spark DataFrame
# Assuming the API returns a list of dictionaries
data = json_data["results"]  # Adjust key as per API structure
df = spark.createDataFrame(data)

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.json('abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/SourceFilesInfo/APIData/')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
