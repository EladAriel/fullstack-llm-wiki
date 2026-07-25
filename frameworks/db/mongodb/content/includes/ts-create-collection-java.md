---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-create-collection-java.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You must first configure the settings for your time series collection:

### Configure a Time Series Collection

You then create your collection with the configured settings using the `db.createCollection()` method.

The following example uses a database named `timeseries` and stores a reference to it under `timeSeriesDB`. It then create a timeseries collection named `weather` in that database and stores a reference to it under the same name:
