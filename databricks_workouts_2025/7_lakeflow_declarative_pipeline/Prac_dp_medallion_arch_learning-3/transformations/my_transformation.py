from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name="dp_prac_catalog.dp_prac_schema.mbronze_drugtbl",cluster_by=["uniqueid"])

def mbronze_drugtbl():
    return spark.read.table("dp_prac_catalog.dp_prac_schema.bronze_drug_info")

@dp.view(name="msilver_drugvw")

@dp.expect_all_or_drop({"rating_is_valid":"rating<=10","nonull_drugname":"drugname is not null"})
#@dp.expect_all_or_fail({"rating_is_valid":"rating<=10","nonull_drugname":"drugname is not null"})
#@dp.expect_all({"rating_is_valid":"rating<=10","nonull_drugname":"drugname is not null"})
@dp.expect("useful_cnt_is_valid","usefulcount >0")

def msilver_drugvw():
   return (spark.read.table("dp_prac_catalog.dp_prac_schema.mbronze_drugtbl").filter("usefulcount > 0"))

@dp.materialized_view(name="mgold_drugmv")
def mgold_drugmv():
    df1 = spark.read.table("msilver_drugvw")
    return (
        df1.groupBy("drugname")
        .agg(
            F.sum("usefulcount").alias("total_usefulcount"),
            F.avg("rating").alias("avg_rating")
        )
    )
