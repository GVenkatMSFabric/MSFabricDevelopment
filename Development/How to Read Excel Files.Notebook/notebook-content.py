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

import pandas as pd

ExcelFilePath = '/lakehouse/default/Files/ExcelSourceInfo/Dept.xlsx'
df = pd.read_excel(ExcelFilePath)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
import glob
import os

directory_path = '/lakehouse/default/Files/ExcelSourceInfo/'
ExcelFiles = glob.glob(os.path.join(directory_path, '*.xlsx'))

dataframes = []

for file in ExcelFiles:
    df = pd.read_excel(file)
    dataframes.append(df)

final_df = pd.concat(dataframes, ignore_index=True)
display(final_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
import glob
import os

directory_path = '/lakehouse/default/Files/ExcelSourceInfo/'  

AllExcelFiles = glob.glob(os.path.join(directory_path, '*.xlsx'))

files_to_read = ['Dept TestData.xlsx', 'Dept.xlsx']  

dataframes = []

for file in AllExcelFiles:
    if os.path.basename(file) in files_to_read:
        df = pd.read_excel(file)
        dataframes.append(df)

final_df = pd.concat(dataframes, ignore_index=True)

display(final_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
import glob 
import os
from pyspark.sql import SparkSession

directory_path = '/lakehouse/default/Files/ExcelSourceInfo/'  

AllExcelFiles = glob.glob(os.path.join(directory_path, '*.xlsx'))

files_to_read = ['Dept TestData.xlsx', 'Dept.xlsx']   

dataframes = []

for file in AllExcelFiles:
    if os.path.basename(file) in files_to_read:
        df = pd.read_excel(file)
        dataframes.append(df)

final_df = pd.concat(dataframes, ignore_index=True)
# Here Converting pandas data frame into Pyspark Data Frame

spark_df = spark.createDataFrame(final_df)
spark_df.write.format('delta').mode('append').saveAsTable('PySparkExcelData')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
