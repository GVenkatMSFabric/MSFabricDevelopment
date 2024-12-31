# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "5d2cf12f-f00e-411b-b2de-9bf4fd2584ef",
# META       "default_lakehouse_name": "SourceDataLakehouse",
# META       "default_lakehouse_workspace_id": "321a063b-1b4e-408b-be9d-34293a175ad9",
# META       "known_lakehouses": [
# META         {
# META           "id": "5b9f77a2-8b6d-4400-a5a7-1f9f8bcdac66"
# META         },
# META         {
# META           "id": "5d2cf12f-f00e-411b-b2de-9bf4fd2584ef"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

notebookutils.notebook.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.run("TestNoteBookInfo", 90)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.run("TestNoteBookInfo", 90,{"EmployeeName":"Gaddam Rithvik"})

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.run("TestNoteBookInfo", 90,{"EmployeeName":"MS Fabric Testing"},"321a063b-1b4e-408b-be9d-34293a175ad9")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.runMultiple(["TestNoteBookInfo", "RunNotebookSample"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# run multiple notebooks with parameters
DAG = {
    "activities": [
        {
            "name": "TestNoteBookInfo", # activity name, must be unique
            "path": "TestNoteBookInfo", # notebook path
            "timeoutPerCellInSeconds": 90, # max timeout for each cell, default to 90 seconds
            "args": {"EmployeeName": "changed value"}, # notebook parameters
        },
        {
            "name": "RunNotebookSample",
            "path": "RunNotebookSample",
            "timeoutPerCellInSeconds": 120,
            "args": {"EmpId": "43"}
        }
    ],
    "timeoutInSeconds": 43200, # max timeout for the entire DAG, default to 12 hours
    "concurrency": 50 # max number of notebooks to run concurrently, default to 50
}
notebookutils.notebook.runMultiple(DAG, {"displayDAGViaGraphviz": False})

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.validateDAG(DAG)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.exit("Currently We are existing this Notebook..")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.update("TestNoteBookInfo", "TestNoteBookInfo_UpdatedOne")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.delete("TestNoteBookInfo_UpdatedOne")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.notebook.list("321a063b-1b4e-408b-be9d-34293a175ad9")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.credentials.help()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.mount( 
 "abfss://SalesReport@onelake.dfs.fabric.microsoft.com/SourceDataLakehouse.Lakehouse", 
 "/MainLakeHouse"
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.getMountPath("/MainLakeHouse")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.ls(f"file://{notebookutils.fs.getMountPath('/MainLakeHouse')}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.mkdirs(f"file://{notebookutils.fs.getMountPath('/MainLakeHouse')}/TestSourceMount")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.fs.mounts()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.create("FabricLakehouseInfo", "TestDataInformation")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.get("FabricLakehouseInfo", "321a063b-1b4e-408b-be9d-34293a175ad9")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.getWithProperties("FabricLakehouseInfo", "321a063b-1b4e-408b-be9d-34293a175ad9")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.update("FabricLakehouseInfo", "FabricLakehouseInfo_New", "Updated description", "321a063b-1b4e-408b-be9d-34293a175ad9")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.delete("FabricLakehouseInfo_New", "321a063b-1b4e-408b-be9d-34293a175ad9")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.list("321a063b-1b4e-408b-be9d-34293a175ad9")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.lakehouse.listTables("SourceDataLakehouse", "321a063b-1b4e-408b-be9d-34293a175ad9") # Schema enabled means it will not display list of the Tables

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.runtime.context

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.session.stop()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
