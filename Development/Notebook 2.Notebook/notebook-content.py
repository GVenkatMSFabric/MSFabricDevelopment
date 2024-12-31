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

df = spark.read.json(path="abfss://DeptSales@onelake.dfs.fabric.microsoft.com/TempLakehouse.Lakehouse/Files/JsonFilesData/ExecuteJsonData/Executionjsondata.json",multiLine=True)
display(df)
df.printSchema()

from pyspark.sql.functions import explode,col
df2 = df.withColumn("DataInformation",explode("datasets"))\
        .withColumn("CustomerId",col("DataInformation.CustomerId"))\
        .withColumn("OrderDetailsId",col("DataInformation.OrderDetailId"))\
        .withColumn("OrderDate",col("DataInformation.orderDate"))\
        .withColumn("StreetName",col("DataInformation.DeliveryData.streetName"))\
        .withColumn("CityName",col("DataInformation.DeliveryData.CityName"))\
        .withColumn("StateName",col("DataInformation.DeliveryData.StateName"))\
        .withColumn("PinCode",col("DataInformation.DeliveryData.PinCode"))\
        .withColumn("CountryName",col("DataInformation.DeliveryData.country"))\
        .withColumn("ProductInfo",explode("DataInformation.orderDetails"))\
        .withColumn("ProductName",col("ProductInfo.ProductNumber"))\
        .withColumn("NoItems",col("ProductInfo.NoofItems"))\
        .withColumn("sequence",col("ProductInfo.sequence"))\
        .withColumn("TotalGross",col("ProductInfo.TotalCost.TotalGross"))\
        .withColumn("TotalNet",col("ProductInfo.TotalCost.TotalNet"))\
        .withColumn("TotalTax",col("ProductInfo.TotalCost.TotalTax"))\
        .drop("datasets","DataInformation","ProductInfo")
display(df2)
df2.printSchema()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
