---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/timeseries-removal-csharp.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you create a `time series collection <manual-timeseries-collection>`, you can set up automatic removal of documents older than a specified number of seconds by using the `expireAfterSeconds` property:

The expiration threshold is the `timeField` field value plus the specified number of seconds. Consider the following document in the `weather24h` collection:

The document has a timestamp of `"2021-11-19T18:00:00Z"` and the `expireAfterSeconds` value is set to 86400 seconds (one day), so the document will expire from the database at `"2021-11-20T18:00:00Z"`.

> **Note:** Once all documents in a bucket are expired, the background task that removes expired
buckets removes the bucket during the next run. See
`timeseries-collection-delete-operations-timing` for more
information.

## Create or Change Expiration Time

To enable automatic removal of documents on a `time series collection <manual-timeseries-collection>` that doesn't have an expiration, or to modify the expiration time on an existing collection, change the `expireAfterSeconds` parameter value, using the :dbcommand:`collMod` command:

## Retrieve the Current Value of `expireAfterSeconds`

To retrieve the current value of `expireAfterSeconds`, use the `ListCollectionsAsync` method. The result document contains the `options.expireAfterSeconds` field for the timeseries collection.

## Disable Automatic Removal

To disable automatic removal, use the :dbcommand:`collMod` command to set `expireAfterSeconds` to `off`:
