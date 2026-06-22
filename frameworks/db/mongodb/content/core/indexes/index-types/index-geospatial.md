---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-geospatial.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Geospatial Indexes

.. include:: /includes/geospatial-indexes-intro.rst

To learn more about geospatial data and query operations, see `/geospatial-queries`.

## Use Cases

If your application frequently queries a field that contains geospatial data, you can create a geospatial index to improve performance for those queries.

Certain query operations require a geospatial index. If you want to query with the :query:`$near` or :query:`$nearSphere` operators or the :pipeline:`$geoNear` aggregation stage, you must create a geospatial index. For details, see `geospatial-operators` and `geospatial-aggregation`.

For example, consider a `subway` collection with documents containing a `location` field, which specifies the coordinates of subway stations in a city. You often run queries with the :query:`$geoWithin` operator to return a list of stations within a specific area. To improve performance for this query, you can create a geospatial index on the `location` field. After creating the index, you can query using the :query:`$near` operator to return a list of nearby stations, sorted from nearest to farthest.

## Get Started

To create a geospatial index and run geospatial queries, see:

- `2dsphere-index-create`
- `2dsphere-index-query`
- `2d-index-create`
- `2d-index-query`
## Details

This section describes details about geospatial indexes.

### Sharded Collections

.. include:: /includes/extracts/geospatial-index-shard-key-restriction-general.rst

You can use geospatial `query operators <geospatial-operators>` and `aggregation stages <geospatial-aggregation>` to query for geospatial data on sharded collections.

### Covered Queries

.. include:: /includes/fact-geospatial-index-covered-query.rst

### Spherical Queries

.. include::  /includes/extracts/geospatial-queries-longitude-values.rst

However, you can use the `2dsphere` index for both spherical queries and two-dimensional queries. For two-dimensional queries, the `2dsphere` index converts data stored as legacy coordinate pairs to the `GeoJSON Point <geojson-point>` type.

## Learn More

For sample geospatial query operations, see `Geospatial Query Examples <geospatial-query-examples>`.

## Contents

- 2dsphere </core/indexes/index-types/geospatial/2dsphere>
- 2d </core/indexes/index-types/geospatial/2d>
- Restrictions </core/indexes/index-types/geospatial/restrictions>
