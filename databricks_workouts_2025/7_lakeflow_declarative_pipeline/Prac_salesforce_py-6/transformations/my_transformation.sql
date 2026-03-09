CREATE OR REFRESH STREAMING TABLE logistic_dp_catalog.logistic_dp_schema.account_silver
AS
SELECT
  *,
  upper(Industry) AS Industry_upper
FROM STREAM(lakeflow_pl_cat.lakeflow_pl_sch.account);