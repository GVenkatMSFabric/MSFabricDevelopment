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
# META       "default_lakehouse_workspace_id": "636a293c-b141-4586-887c-b60d7f65acb8",
# META       "known_lakehouses": [
# META         {
# META           "id": "5b9f77a2-8b6d-4400-a5a7-1f9f8bcdac66"
# META         },
# META         {
# META           "id": "22e80c9d-3f63-4efa-ac27-62f4a663e367"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import SparkSession
 
# Read from Lakehouse 1
df = spark.read.csv("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/SalesLakehouse.Lakehouse/Files/Development/DemoSales/Emp.csv",header=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read from Lakehouse 2
df = spark.read.csv("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/FinalCSVData/Sales.csv",header=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from notebookutils import mssparkutils
mssparkutils.fs.mounts()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#To get the default lakehouse attached to the notebook

for mp in mssparkutils.fs.mounts():
    if mp.mountPoint == '/default':
        print(f"Default Lakehouse is: {mp.source}")

# abfss://<workspace_id>@onelake.dfs.fabric.microsoft.com/<lakehouse_id>

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

storage_options = {"bearer_token": notebookutils.credentials.getToken("storage"), "use_fabric_endpoint": "true"}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

mssparkutils.fs.mount("abfss://636a293c-b141-4586-887c-b60d7f65acb8@onelake.dfs.fabric.microsoft.com/<lakehouse_id>", "<mountPoint>") #mountPoint such as '/lakehouse/default'


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************



# Set your access token
access_token =  notebookutils.credentials.getToken("storage") 

# API endpoint to list workspaces
url = "https://app.powerbi.com/home?experience=power-bi"

headers = {
    "Authorization": f"Bearer {access_token}"
}

# Get workspaces
response = requests.get(url, headers=headers)
workspaces = response.json()

# Print workspaces and their IDs
for workspace in workspaces['value']:
    print(f"Workspace Name: {workspace['name']}, Workspace ID: {workspace['id']}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# Get Lakehouses in a specific workspace
workspace_id = "your_workspace_id_here"
lakehouse_url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/items"

lakehouse_response = requests.get(lakehouse_url, headers=headers)
lakehouses = lakehouse_response.json()

# Print Lakehouses and their IDs
for lakehouse in lakehouses['value']:
    print(f"Lakehouse Name: {lakehouse['name']}, Lakehouse ID: {lakehouse['id']}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
