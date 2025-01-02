import sys
import os
#import Constant
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf 


if __name__ == "__main__":

    #Spark session builder
    spark_session = (SparkSession
          .builder
          .appName("sjdsampleapp") 
          .config("spark.some.config.option", "some-value")
          .getOrCreate())
    
    spark_context = spark_session.sparkContext
    spark_context.setLogLevel("DEBUG")
      
    parquetFilePath = "Files/ExtractExceltoCSV/Employee_Employee.csv"
    #deltaTablePath = SaveToLH + "/Tables/" + tableName
    deltaTablePath = "SparkTableData"

    df = spark_session.read.option("header", "true").format("csv").load(parquetFilePath)
    df.write.mode('append').format('delta').saveAsTable(deltaTablePath)