---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/centerSphere.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
