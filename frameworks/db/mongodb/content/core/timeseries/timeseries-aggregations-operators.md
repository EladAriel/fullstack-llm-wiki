---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-aggregations-operators.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# Aggregation and Operator Considerations

Some aggregation stages and operators require special considerations when you use them with `time series collections <manual-timeseries-landing>`.

### $geoNear

Time series collections only support the :pipeline:`$geoNear` aggregation stage for sorting `geospatial data <geospatial-queries>` from queries against `2dsphere <2dsphere-index>` indexes. You can't use the :query:`$near` and :query:`$nearSphere` operators on time series collections.

.. include:: /includes/fact-geoNear-timeseries-query-restriction.rst

.. include:: /includes/fact-geoNear-timeseries-key-required.rst

### $merge

You cannot use the :pipeline:`$merge` aggregation stage to add data from another collection to a time series collection.

### $out

Starting in MongoDB 7.0, you can use the :pipeline:`$out` aggregation stage to write documents to a time series collection. For more information, see `migrate-data-into-a-timeseries-collection`.

### Frequently Used Operations

The following aggregation pipeline operators and stages are often used to analyze time series data:

- :expression:`$dateAdd`: Adds a specified amount of time to a Date
object.

- :expression:`$dateDiff`: Returns the time difference between two dates.
- :expression:`$dateTrunc`: Returns a date that has been truncated to
the specific unit.

- :pipeline:`$setWindowFields`: Runs calculations on documents in a
given window.

### Examples
