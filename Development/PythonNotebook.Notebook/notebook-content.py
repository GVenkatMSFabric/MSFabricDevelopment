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

!pip install semantic-link --q 
import json
import sempy.fabric as fabric
from sempy.fabric.exceptions import FabricHTTPException, WorkspaceNotFoundException
import pandas as pd
import json

workspace_id='636a293c-b141-4586-887c-b60d7f65acb8'

#Instantiate the client
client = fabric.FabricRestClient()
uri = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/notebooks"

# Call the REST API
response = client.get(uri)

data = json.loads(response.text)
df = pd.DataFrame(data["value"])
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
