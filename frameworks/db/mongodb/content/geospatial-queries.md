---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/geospatial-queries.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Geospatial Queries

MongoDB supports query operations on geospatial data. This section introduces MongoDB geospatial features.

## Geospatial Data

In MongoDB, you can store geospatial data as GeoJSON objects or as legacy coordinate pairs.

### GeoJSON Objects

To calculate geometry over an Earth-like sphere, store your location data as `GeoJSON objects <geospatial-indexes-store-geojson>`.

.. include:: /includes/extracts/geojson-specification-geospatial.rst

### Legacy Coordinate Pairs

Use legacy coordinate pairs for flat (Euclidean) calculations with a `geo-2d` index. To perform spherical calculations, convert legacy pairs to a GeoJSON `Point` and use a `geo-2dsphere` index.

.. include:: /includes/fact-legacy-coordinates-specification.rst

## Geospatial Indexes

.. include:: /includes/geospatial-indexes-intro.rst

For more information on geospatial indexes, see `geospatial-index`.

## Geospatial Queries

> **Note:** .. include::  /includes/extracts/geospatial-queries-longitude-values.rst

If an indexed document contains both legacy coordinate fields and a GeoJSON object in the same `location` subdocument, MongoDB selects the indexed representation based on the server version:

- MongoDB earlier than 8.2 indexes the first supported representation
according to field order. If the first two fields are numeric, MongoDB interprets them as a legacy `[longitude, latitude]` pair and ignores any GeoJSON fields that appear later.

- MongoDB 8.2 and later always indexes the GeoJSON representation
when the subdocument contains any GeoJSON object, regardless of field order.

### Geospatial Query Operators

MongoDB provides the following geospatial query operators. For more details, including examples, see the respective reference pages.

.. include:: /includes/geospatial-query-predicate-operators.rst

> **Note:** .. include:: /includes/time-series/fact-time-series-geodata.rst

### Geospatial Aggregation Stage

MongoDB provides the following geospatial `aggregation pipeline stage <aggregation-pipeline>`:

For more details, including examples, see :pipeline:`$geoNear` reference page.

## Geospatial Models

MongoDB geospatial queries can interpret geometry on a flat surface or a sphere.

`2dsphere` indexes support only spherical queries (that is, queries that interpret geometries on a spherical surface).

`2d` indexes support flat queries (that is, queries that interpret geometries on a flat surface) and some spherical queries. While `2d` indexes support some spherical queries, the use of `2d` indexes for these spherical queries can result in error. If possible, use `2dsphere` indexes for spherical queries.

The following table lists the geospatial query operators, supported query, used by each geospatial operations:

## Perform Geospatial Queries in Atlas

## Examples

.. include:: /includes/sample-data-usage.rst

The `sample_mflix.theaters` collection has a `2dsphere` index. The following query uses the :query:`$near` operator to return documents sorted from nearest to farthest. The query returns documents at least 1000 meters and at most 100000 meters from the specified GeoJSON point:

The following operation uses the :pipeline:`$geoNear` aggregation operation to return documents that match the query filter `{ "location.address.state": "NY" }`, sorted in order of nearest to farthest to the specified GeoJSON point:

## Contents

- Find Restaurants </tutorial/geospatial-tutorial>
- GeoJSON Objects </reference/geojson>
