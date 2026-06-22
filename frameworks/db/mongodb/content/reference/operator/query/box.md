---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/box.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $box (query predicate operator)

## Definition

## Behavior

The query calculates distances using flat (planar) geometry.

.. include:: /includes/note-geospatial-index-must-exist.rst

Only the `2d <2d-index>` geospatial index supports :query:`$box`.

## Example

The following example query returns all documents that are within the box having points at: `[ 0 , 0 ]`, `[ 0 , 100 ]`, `[ 100 , 0 ]`, and `[ 100 , 100 ]`.

```javascript
db.places.find( {
   loc: { $geoWithin: { $box:  [ [ 0, 0 ], [ 100, 100 ] ] } }
} )
```
