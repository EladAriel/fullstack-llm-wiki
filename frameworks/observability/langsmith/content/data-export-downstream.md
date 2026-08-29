---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/data-export-downstream.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.634530Z"
---
# Data Export Downstream

---
title: Import exported data
description: Import LangSmith bulk-exported Parquet data into BigQuery, Snowflake, Redshift, Clickhouse, or DuckDB.
---

Importing data from S3 and Parquet format is commonly supported by the majority of analytical systems. See below for documentation links:

## BigQuery

To import your data into BigQuery, see [Loading Data from Parquet](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet) and also
[Hive Partitioned loads](https://cloud.google.com/bigquery/docs/hive-partitioned-loads-gcs).

## Snowflake

You can load data into Snowflake from S3 by following the [Load from Cloud Document](https://docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial).

## RedShift

You can COPY data from S3 or Parquet into Amazon Redshift by following the [AWS COPY command documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html).

## Clickhouse

You can directly query data in S3 / Parquet format in Clickhouse. As an example, if using GCS, you can query the data as follows:

```sql
SELECT count(distinct id) FROM s3('https://storage.googleapis.com/<bucket>/<prefix>/export_id=<export_id>/**',
 'access_key_id', 'access_secret', 'Parquet')
```

See [Clickhouse S3 Integration Documentation](https://clickhouse.com/docs/en/engines/table-engines/integrations/s3) for more information.

## DuckDB

You can query the data from S3 in-memory with SQL using DuckDB. See [S3 import Documentation](https://duckdb.org/docs/guides/network_cloud_storage/s3_import.html).
