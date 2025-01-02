# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************


notebookutils.notebook.help()

notebookutils.notebook.run("TestNoteBookInfo", 90)

notebookutils.notebook.run("TestNoteBookInfo", 90,{"EmployeeName":"Gaddam Rithvik"})

notebookutils.notebook.run("TestNoteBookInfo", 90,{"EmployeeName":"MS Fabric Testing"},"321a063b-1b4e-408b-be9d-34293a175ad9")

notebookutils.notebook.runMultiple(["TestNoteBookInfo", "RunNotebookSample"])

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

notebookutils.notebook.validateDAG(DAG)

notebookutils.notebook.exit("Currently We are existing this Notebook..")

notebookutils.notebook.update("TestNoteBookInfo", "TestNoteBookInfo_UpdatedOne")

notebookutils.notebook.delete("TestNoteBookInfo_UpdatedOne")

notebookutils.notebook.list("321a063b-1b4e-408b-be9d-34293a175ad9")

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
