CREATE OR REFRESH STREAMING TABLE dp_prac_catalog.dp_prac_schema.silver_drug_info
(
  CONSTRAINT valid_drug_id EXPECT (uniqueid IS NOT NULL) ON VIOLATION DROP ROW
)
TBLPROPERTIES (
    pipelines.autoOptimize.enabled = "true",
    delta.enableChangeDataFeed = "true"
    )
AS SELECT *,
_metadata.file_path AS source_file,
current_timestamp() AS ingestion_time
FROM STREAM(dp_prac_catalog.dp_prac_schema.bronze_drug_info);


CREATE OR REFRESH MATERIALIZED VIEW dp_prac_catalog.dp_prac_schema.gold_drug_mv
CLUSTER BY(uniqueid)
COMMENT "cleaned and optimize drug data for reporting"
TBLPROPERTIES (
    delta.enableDeletionVectors = "true"
)
AS SELECT *, 
upper(drugname) AS drug_name_clean
FROM (dp_prac_catalog.dp_prac_schema.silver_drug_info);