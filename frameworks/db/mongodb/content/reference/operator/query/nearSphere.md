---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/nearSphere.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# $nearSphere (query predicate operator)

## Definition

## Behavior

### Special Indexes Restriction

.. include:: /includes/fact-geo-near-special-indexes.rst

### Sort Operation

.. include:: /includes/fact-geo-near-returns-sorted-results.rst

### Validation

.. include:: /includes/fact-geo-near-geojson-validation.rst

## Examples

### Specify Center Point Using GeoJSON

.. include:: /includes/example-nearSphere-minDistance.rst

### Specify Center Point Using Legacy Coordinates

`2d` Index ````````````

Consider a collection `legacyPlaces` that contains documents with legacy coordinates pairs in the `location` field and has a `2d <2d-index>` index.

Then, the following example returns those documents whose `location` is at most `0.10` radians from the specified point, ordered from nearest to farthest:

```javascript
db.legacyPlaces.find(
   { location : { $nearSphere : [ -73.9667, 40.78 ], $maxDistance: 0.10 } }
)
```

`2dsphere` Index ``````````````````

If the collection has a `2dsphere` index instead, you can also specify the optional :query:`$minDistance` specification. For example, the following example returns the documents whose `location` is at least `0.0004` radians from the specified point, ordered from nearest to farthest:

```javascript
db.legacyPlaces.find(
   { location : { $nearSphere : [ -73.9667, 40.78 ], $minDistance: 0.0004 } }
)
```
