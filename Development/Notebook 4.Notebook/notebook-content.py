# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

!pip install semantic-link --q 
import json
import sempy.fabric as fabric
from sempy.fabric.exceptions import FabricHTTPException, WorkspaceNotFoundException
import pandas as pd
import json

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Retrieve the workspace ID
workspace_id = spark.conf.get("trident.workspace.id")

print(f"The current workspace ID is: {workspace_id}")

# METADATA ********************

# META {
# META   "language": "python",
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
