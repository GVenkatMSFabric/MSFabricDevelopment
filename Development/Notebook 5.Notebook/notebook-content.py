# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# How to create Fabric DW in this WorkSpace
!pip install semantic-link --q 
import json
import sempy.fabric as fabric
from sempy.fabric.exceptions import FabricHTTPException, WorkspaceNotFoundException

workspace_id=spark.conf.get("trident.workspace.id")

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/warehouses"
payload = {
  "displayName": "FabricDW_Test",
  "description": "This is Demo Notebook Purpose."
    }
# Call the REST API
response = client.post(uri,json= payload)
display(response)

data = json.loads(response.text)
display(data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Returns the list of Fabric DW in this WorkSpace
!pip install semantic-link --q 
import json
import sempy.fabric as fabric

workspace_id=spark.conf.get("trident.workspace.id")

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/warehouses"

# Call the REST API
response = client.get(uri)
display(response)

data = json.loads(response.text)
display(data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

!pip install semantic-link --q 
import json
import sempy.fabric as fabric

workspace_id=spark.conf.get("trident.workspace.id")
warehouseId = 'c1d662ec-5a6f-45fc-bd20-861c9db22fa6'

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/warehouses/{warehouseId}"

# Call the REST API
response = client.delete(uri)
display(response)

data = json.loads(response.text)
display(data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

!pip install semantic-link --q 
import json
import sempy.fabric as fabric

workspace_id=spark.conf.get("trident.workspace.id")
warehouseId = '15b0fafe-7d7d-47e6-9475-5541b89f2542'

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/warehouses/{warehouseId}"

# Call the REST API
response = client.get(uri)
display(response)

data = json.loads(response.text)
display(data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

!pip install semantic-link --q 
import json
import sempy.fabric as fabric

workspace_id=spark.conf.get("trident.workspace.id")
warehouseId = '15b0fafe-7d7d-47e6-9475-5541b89f2542'

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/warehouses/{warehouseId}"
payload = {
  "displayName": "Temp_FabricDW",
  "description": "This is Updated the Fabric Data Warehouse Name"
    }

# Call the REST API
response = client.patch(uri,json=payload)
display(response)

data = json.loads(response.text)
display(data)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
