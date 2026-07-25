---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/box.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
