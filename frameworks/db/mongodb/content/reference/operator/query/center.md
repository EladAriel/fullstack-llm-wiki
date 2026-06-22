---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/center.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $center (query predicate operator)

## Definition

## Behavior

The query calculates distances using flat (planar) geometry.

.. include:: /includes/note-geospatial-index-must-exist.rst

Only the `2d <2d-index>` geospatial index supports :query:`$center`.

## Example

The following example query returns all documents that have coordinates that exist within the circle centered on `[ -74, 40.74 ]` and with a radius of `10`:

```javascript
db.places.find(
   { loc: { $geoWithin: { $center: [ [-74, 40.74], 10 ] } } }
)
```
