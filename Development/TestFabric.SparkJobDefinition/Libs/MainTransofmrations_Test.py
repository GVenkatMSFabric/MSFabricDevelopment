def run(spark_session):
    print("log from Main Tranformations")
    parquetFilePath = "Files/ExtractExceltoCSV/Employee_Employee.csv"
    # deltaTablePath = SaveToLH + "/Tables/" + tableName
    deltaTablePath = "MainTransformationData"

    df = spark_session.read.option("header", "true").format("csv").load(parquetFilePath)
    df.write.mode("append").format("delta").saveAsTable(deltaTablePath)