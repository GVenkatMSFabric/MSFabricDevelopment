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

spark.conf.set("spark.microsoft.delta.properties.defaults.enableChangeDataFeed", "true")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.types import *
from datetime import datetime
SchemaData = StructType([
                    StructField('EmpId', IntegerType(), True),
                    StructField('EmpName', StringType(), True),
                    StructField('EmpSalary', IntegerType(), True),
                    StructField('TotalPrice', IntegerType(), True),
                    StructField('OrderDate', DateType(), True)])

DataValue = [(101,'Venkat',190, 315,datetime(2023, 11, 20)),
            (102,'Ramesh',4510, 101,datetime(2023, 11, 20)),
            (103,"Suresh",51,1125,datetime(2023, 11, 20))]

df = spark.createDataFrame(DataValue,SchemaData) \
            .write.mode("overwrite").format("delta").save("Tables/dbo/TempInformationData")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

NewRecord = [(104,'Koti',3432, 7350,datetime(2023, 11, 21))]

spark.createDataFrame(data=NewRecord, schema = SchemaData).write.format("delta").mode("append").saveAsTable("TempInformationData")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from delta.tables import *
from pyspark.sql.functions import *

deltaTable = DeltaTable.forPath(spark, 'Tables/dbo/TempInformationData')


deltaTable.update(
  condition = "EmpId = 101",
  set = { "EmpSalary": "939", "TotalPrice": "34548"  }
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from delta.tables import *
from pyspark.sql.functions import *

deltaTable = DeltaTable.forPath(spark, 'Tables/dbo/TempInformationData')

deltaTable.delete("EmpId = 102")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

NewRecord = [(45,'Ramesh',3432, 7350,datetime(2023, 11, 21)),(655,'Pavani',3432, 7350,datetime(2023, 11, 21))]

spark.createDataFrame(data=NewRecord, schema = SchemaData).write.format("delta").mode("append").saveAsTable("TempInformationData")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from delta.tables import *
from pyspark.sql.functions import *

deltaTable = DeltaTable.forPath(spark, 'Tables/dbo/TempInformationData')


deltaTable.update(
  condition = "EmpId = 103",
  set = { "EmpSalary": "7878", "TotalPrice": "34548"  }
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from delta.tables import *
from pyspark.sql.functions import *

deltaTable = DeltaTable.forPath(spark, 'Tables/dbo/TempInformationData')

deltaTable.delete("EmpId = 101")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("delta").table("TempInformationData")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
