---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================

# Time Series Indexes

Indexes on time series collections generally behave like indexes on regular collections, but with several additional considerations and limitations.

.. include:: /includes/time-series-secondary-indexes-downgrade-FCV.rst

Starting in version 6.0, you can add a secondary index to any field in a time series collection. MongoDB indexes time series collections by `buckets <timeseries-bucketing>` of documents as opposed to individual documents. Time series buckets contain documents with shared metaField values, ordered by timeField values that are close together. MongoDB indexes the minimum and maximum values of all fields, except the metaField. Indexing buckets instead of individual documents reduces index size and improves query efficiency.

> **Tip:** To improve query performance, you can manually :ref:`add secondary
indexes <timeseries-add-secondary-index>` to any field in your time
series collection.

## Clustered Collection

By default, MongoDB clusters time series collections based on bucket time.

## Compound Indexes

.. versionadded:: 6.3

Starting in MongoDB 6.3, MongoDB creates a default  `compound index <index-type-compound>` on both the metaField and timeField of a time series collection. MongoDB uses this index to improve query performance and speed.

You can add a `compound index <index-type-compound>` on the `timeField`, `metaField`, or measurement fields.

## Partial Indexes

.. versionadded:: 6.0

Starting in MongoDB 6.0, you can use the :query:`$or`, :query:`$in`, and :query:`$geoWithin` operators with `partial indexes <index-type-partial>` on a time series collection.

You cannot create `partial indexes <index-type-partial>` on the metaField and timeField.

## TTL Indexes

.. versionadded:: 7.0

Starting in MongoDB 7.0, you can create a `TTL <index-feature-ttl>` index with a `partialFilterExpression` that relies only on the metaField. In versions prior to 6.3, you can only create TTL indexes based on the `expireAfterSeconds` parameter.

If your time series collection doesn't use the `expireAfterSeconds` option to expire documents, creating a partial TTL index sets an expiration time for matching documents only. If the collection uses `expireAfterSeconds` for all documents, you can use a partial TTL index to expire matching documents sooner.

## Prohibited Indexes

MongoDB does not allow the following index types on time series collections:

- `Text indexes <index-type-text>`
- `2d indexes <2d-index>`
- `Unique indexes <index-type-unique>`
You cannot create sparse indexes on the metaField.

## Indexing Best Practices

.. include:: /includes/time-series/fact-index-best-practices.rst

For more information and examples, see `timeseries-add-secondary-index`.

## Contents

- Add Secondary Indexes </core/timeseries/timeseries-secondary-index>
