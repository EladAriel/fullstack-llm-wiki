---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/centerSphere.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# $centerSphere (query predicate operator)

## Definition

## Behavior

.. include:: /includes/note-geospatial-index-must-exist.rst

Both `2dsphere <2dsphere-index>` and `2d <2d-index>` geospatial indexes support :query:`$centerSphere`.

## Example

The following example queries grid coordinates and returns all documents within a 10 mile radius of longitude `88 W` and latitude `30 N`. The query converts the distance to radians by dividing by the approximate equatorial radius of the earth, 3963.2 miles:

```javascript
db.places.find( {
  loc: { $geoWithin: { $centerSphere: [ [ -88, 30 ], 10/3963.2 ] } }
} )
```
