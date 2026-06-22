---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-create-collection-java.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You must first configure the settings for your time series collection:

### Configure a Time Series Collection

You then create your collection with the configured settings using the `db.createCollection()` method.

The following example uses a database named `timeseries` and stores a reference to it under `timeSeriesDB`. It then create a timeseries collection named `weather` in that database and stores a reference to it under the same name:
