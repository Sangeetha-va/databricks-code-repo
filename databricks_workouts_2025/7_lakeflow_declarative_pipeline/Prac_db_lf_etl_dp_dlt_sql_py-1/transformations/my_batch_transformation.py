from pyspark import pipelines as dp

@dp.table(name="dp_prac_catalog.dp_prac_schema.Bronze_shipments")
def return_df():
    df1= spark.read.table("lakeflow_pl_cat.lakeflow_pl_sch.shipments") # batch 
    return df1

# we mostly get data directly from external database like mysql just like foreign catalog, for learning purpose we are using same unity catalog data. 
# if external database is used we can only perform batch load while from unity catalog table we can perform batch and streaming load.
#external table send the entire data and DLT handles to load only incremental/insert/update/delete data
#Streaming data will load data in continuous fashion and predominantly load only increamental data ie only insert (fact table). 