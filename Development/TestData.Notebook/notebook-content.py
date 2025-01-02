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

notebookutils.fs.ls("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/JsonFilesData") 

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************



notebookutils.fs.ls("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/JsonFilesData") 

notebookutils.fs.ls("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/JsonFilesData/TestData/")

notebookutils.fs.ls("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/JsonFilesData/TestData/TestFile.json")

notebookutils.fs.ls("Files")

notebookutils.fs.ls("Files/JsonFilesData/ExecuteJsonData")

notebookutils.fs.ls("Files/JsonFilesData/MainData/MainData.json")

files = notebookutils.fs.ls('abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/JsonFilesData/ExecuteJsonData')
for file in files:
    print(file.name, file.isDir, file.isFile, file.path, file.size)
	
files = notebookutils.fs.ls('Files/JsonFilesData/ExecuteJsonData')
for file in files:
    print(file.name, file.isDir, file.isFile, file.path, file.size)
	
notebookutils.fs.mkdirs('Files/SourceFilesInfo')

notebookutils.fs.mkdirs("abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/TempSourceInfo")

notebookutils.fs.cp('Files/JsonFilesData/TestData/', 'Files/TempSourceInfo/', True)

notebookutils.fs.cp('Files/FinalCSVData/Sales.csv', 'Files/TempSourceInfo/', True)

notebookutils.fs.mv('Files/FinalCSVData', 'Files/SourceFilesInfo', True)

notebookutils.fs.mv('Files/TempSourceInfo/Sales.csv', 'Files/JsonFilesData',True)

notebookutils.fs.rm('Files/TempSourceInfo', True)

notebookutils.fs.rm('Files/SourceFilesInfo/FinalCSVData/Sales.csv', True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
