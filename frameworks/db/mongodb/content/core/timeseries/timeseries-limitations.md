---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-limitations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# Time Series Collection Limitations

`Time series collections <manual-timeseries-collection>` generally behave like regular collections with several limitations.

## Unsupported Features

MongoDB does not support the following features with time series collections:

- :atlas:`{+fts+} </atlas-search>`
- `Change streams <changeStreams>`
- `{+csfle+} <manual-csfle-feature>`
- :atlas:`Database Triggers </atlas-ui/triggers/database-triggers>`
- `Schema validation rules <schema-validation-overview>`
- :dbcommand:`reIndex`
- :dbcommand:`renameCollection`
## Aggregation $merge

You cannot use the :pipeline:`$merge` aggregation stage to add data from another collection to a time series collection. Use the :pipeline:`$out` aggregation stage to write documents to a time series collection.

You can use :pipeline:`$merge` to move data from a time series collection to another collection.

## distinct Command

## Geospatial Queries

.. include:: /includes/time-series/fact-time-series-geodata.rst

### $geoNear

.. include:: /includes/fact-geoNear-timeseries-query-restriction.rst

.. include:: /includes/fact-geoNear-timeseries-key-required.rst

## Document Size

The maximum size for documents within a time series collection is 4 MB.

## Extended Date Range

If your time series collection contains  documents with `timeField` timestamps before `1970-01-01T00:00:00.000Z` or after `2038-01-19T03:14:07.000Z`, create an index on the `timeField` to optimize queries.

## Updates

Update commands must meet the following requirements:

.. include:: /includes/time-series/fact-update-limitations.rst

To automatically delete old data, `set up automatic removal (TTL) <set-up-automatic-removal>`.

## Indexes

### Default Index

MongoDB does not create an index on the `_id field when you create a time series collection. This differs from regular collections which have an index on the id field by default. Commands that specify a hint on the id field on time series collections return an error unless you manually create an index on the id` field.

### Hint on "_id_" Index

Starting in MongoDB 8.3, creating an index with the name of `"_id_"` or specifying a hint of `"_id_"` on time series collections returns an error.

### Time Series Secondary Indexes

MongoDB partially supports the following indexes on time series collections:

- You can only create `multikey indexes <index-type-multikey>` on the `metaField`.
- You can only create `2d indexes <2d-index>` on the `metaField`.
- You can only create `sparse indexes <index-type-sparse>` on the `metaField`.
MongoDB doesn't support the following index types on time series collections:

- `Text indexes <index-type-text>`
- `Unique indexes <index-type-unique>`
.. include:: /includes/time-series-secondary-indexes-downgrade-FCV.rst

## Capped Collections

You cannot create a time series collection as a `capped collection <manual-capped-collection>`.

## Modification of Collection Type

You can only set the collection type when you create a collection:

- You cannot convert an existing collection into a time series collection.
- You cannot convert a time series collection into a different collection type.
To move data from an existing collection to a time series collection, `migrate data into a time series collection <migrate-data-into-a-timeseries-collection>`.

## timeField and metaField

Starting in MongoDB 8.3, you cannot create a `timeField` that starts with a `$` character.

You can only set a collection's `timeField` and `metaField` parameters when you create the collection. You cannot modify these parameters later.

## Granularity

### Bucket Size

For any configuration of granularity parameters, the maximum size of a bucket is 1000 measurements or 125KB of data, whichever is lower. MongoDB may also enforce a lower maximum size for high cardinality data with many unique values, so that the working set of buckets fits within the `WiredTiger cache <storage-wiredtiger>`.

Modifying Bucket Parameters ```````````````````````````

Once you set a collection's `granularity` or the custom bucketing parameters `bucketMaxSpanSeconds` and `bucketRoundingSeconds`, you can increase the time span covered by a bucket, but not decrease it. Use the :dbcommand:`collMod` command to modify the parameters.

For more information on modifying time series intervals, see `Change Time Series Granularity <change-granularity>`.

> **Note:** `bucketMaxSpanSeconds` and `bucketRoundingSeconds` must be
equal. If you modify one parameter, you must also set the other to
the same value.

## Sharding

Time series collections are subject to several sharding limitations.

### Sharding Administration Commands

You cannot run sharding administration commands on sharded time series collections.

### Shard Key Fields

.. include:: /includes/time-series/fact-shard-key-limitations.rst

.. include:: /includes/time-series/timeseries-timeField-deprecated.rst

### Resharding

.. include:: /includes/time-series/reshard-timeseries.rst

For more information, see `sharding-resharding`.

### Zone Sharding

.. include:: /includes/fact-zone-timeseries-support

## Transactions

You cannot write to time series collections in `transactions <transactions>`.

> **Note:** MongoDB supports reads from time series collections in transactions.

## Views

Time series collections are writable non-materialized `views <views-landing-page>`. Limitations for views apply to time series collections.

## Snapshot Isolation

Read operations on time series collections with read concern `"snapshot"` guarantee snapshot isolation only in the absence of concurrent drop or rename operations on collections in the read operation. Re-creating a time series collection on the same namespace with different granularity setting does not yield full snapshot isolation.
