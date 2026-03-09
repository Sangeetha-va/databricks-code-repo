from pyspark import pipelines as dp

@dp.table()
def silver_salesforce_table():
    df1=spark.readStream.table("lakeflow_pl_cat.lakeflow_pl_sch.account")
    return df1
