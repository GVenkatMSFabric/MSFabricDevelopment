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

# Retrieve the workspace ID
workspace_id = spark.conf.get("trident.workspace.id")

Name = spark.conf.get('trident.workspace.name')
print(Name)
print(f"The current workspace ID is: {workspace_id}")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

c

workspace_id=spark.conf.get("trident.workspace.id")
print(workspace_id)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

!pip install semantic-link --q 
import json
import sempy.fabric as fabric
from sempy.fabric.exceptions import FabricHTTPException, WorkspaceNotFoundException
import pandas as pd
import json

workspace_id=spark.conf.get("trident.workspace.id")

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/notebooks"

# Call the REST API
response = client.get(uri)

data = json.loads(response.text)
df = pd.DataFrame(data["value"])
df.write.format('delta').mode('overwrite').saveAsTable('EmpAPIInformation')
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

!pip install semantic-link --q 
import json
import sempy.fabric as fabric
from sempy.fabric.exceptions import FabricHTTPException, WorkspaceNotFoundException
import pandas as pd
import json

workspace_id=spark.conf.get("trident.workspace.id")

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/notebooks"

# Call the REST API
response = client.get(uri)

data = json.loads(response.text)
df = spark.createDataFrame(data["value"])
df.write.format('delta').mode('overwrite').saveAsTable('EmpAPIInformation')
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM EmpAPIInformation

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import sempy.fabric as fabric

# Get the id of this notebooks workspace
workspace_id = fabric.get_notebook_workspace_id()  
# You can also get this with fabric.get_workspace_id()

# From all workspaces, filter by Id and then just get the Name
workspaces = fabric.list_workspaces()
workspace_row = workspaces[workspaces.Id == workspace_id]

workspace_name = workspace_row['Name']
print(workspace_name)
print(workspace_id)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
