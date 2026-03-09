from pyspark import pipelines as dp

@dp.table(name="dp_prac_catalog.dp_prac_schema.Bronze_shipments")
def return_df():
    df1= spark.readStream.table("lakeflow_pl_cat.lakeflow_pl_sch.shipments") # streaming
    return df1