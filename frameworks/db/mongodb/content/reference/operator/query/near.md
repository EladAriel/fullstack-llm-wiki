---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/near.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# $near (query predicate operator)

## Definition

## Behavior

### Special Indexes Restriction

.. include:: /includes/fact-geo-near-special-indexes.rst

### Sort Operation

.. include:: /includes/fact-geo-near-returns-sorted-results.rst

### Validation

.. include:: /includes/fact-geo-near-geojson-validation.rst

## Examples

### Query on GeoJSON Data

.. include:: /includes/example-near-minDistance.rst

### Query on Legacy Coordinates

.. include::  /includes/extracts/geospatial-long-lat-values.rst

Consider a collection `legacy2d` that has a `2d` index.

The following example returns documents that are at most `0.10` radians from the specified legacy coordinate pair, sorted from nearest to farthest:

```javascript
db.legacy2d.find(
   { location : { $near : [ -73.9667, 40.78 ], $maxDistance: 0.10 } }
)
```
