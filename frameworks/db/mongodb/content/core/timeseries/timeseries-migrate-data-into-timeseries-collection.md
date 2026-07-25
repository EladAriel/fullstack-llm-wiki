---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-migrate-data-into-timeseries-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================================

# Migrate Data into a Time Series Collection

If your collection stores data that you want to compare across time intervals, use a time series collection to improve performance and storage. For more information on the benefits of time series collections, see `manual-timeseries-collection`.

You can use the following methods to migrate data from an existing collection into a `time series collection <manual-timeseries-collection>`:

- `Migrate with an Aggregation Pipeline <migrate-data-into-a-timeseries-collection-with-aggregation>`
- `Migrate with Database Tools <migrate-data-into-a-timeseries-collection-with-tools>`
- [Migrate with Relational Migrator](https://www.mongodb.com/docs/relational-migrator/mapping-rules/mapping-rule-options/time-series/)_
## Considerations

If you use MongoDB 7.0 or greater and already have your data in a MongoDB database, migrate with an `aggregation pipeline <migrate-data-into-a-timeseries-collection-with-aggregation>`.

If your data is in a relational database, use [Relational Migrator](https://www.mongodb.com/docs/relational-migrator/mapping-rules/mapping-rule-options/time-series/)_ to migrate your data into a time series collection.

If your deployment is not in one of those cases, use `Database Tools <migrate-data-into-a-timeseries-collection-with-tools>` to migrate your data.

## Contents

- Use Aggregation </core/timeseries/timeseries-migrate-with-aggregation>
- Use Tools </core/timeseries/timeseries-migrate-with-tools>
