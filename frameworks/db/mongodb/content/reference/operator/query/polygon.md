---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/polygon.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# $polygon (query predicate operator)

## Definition

## Behavior

The :query:`$polygon` operator calculates distances using flat (planar) geometry.

.. include:: /includes/note-geospatial-index-must-exist.rst

Only the `2d <2d-index>` geospatial index supports the :query:`$polygon` operator.

## Example

The following query returns all documents that have coordinates that exist within the polygon defined by `[ 0 , 0 ]`, `[ 3 , 6 ]`, and `[ 6 , 0 ]`:

```javascript
db.places.find(
  {
     loc: {
       $geoWithin: { $polygon: [ [ 0 , 0 ], [ 3 , 6 ], [ 6 , 0 ] ] }
     }
  }
)
```
