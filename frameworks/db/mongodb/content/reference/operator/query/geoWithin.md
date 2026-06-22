---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/geoWithin.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# $geoWithin (query predicate operator)

## Definition

## Behavior

### Geospatial Indexes

:query:`$geoWithin` does not require a geospatial index. However, a geospatial index will improve query performance. Both `2dsphere <2dsphere-index>` and `2d <2d-index>` geospatial indexes support :query:`$geoWithin`.

### Unsorted Results

The :query:`$geoWithin` operator does not return sorted results. As such, MongoDB can return :query:`$geoWithin` queries more quickly than geospatial :query:`$near` or :query:`$nearSphere` queries, which sort results.

### Degenerate Geometry

:query:`$geoWithin` does not guarantee that it will consider a piece of geometry to contain its component geometry, or another polygon sharing its component geometry.

### "Big" Polygons

.. include:: /includes/fact-geometry-hemisphere-limitation.rst

## Examples

### Within a Polygon

The following example selects all `loc` data that exist entirely within a GeoJSON `geojson-polygon`. The area of the polygon is less than the area of a single hemisphere:

```javascript
db.places.find(
   {
     loc: {
       $geoWithin: {
          $geometry: {
             type : "Polygon" ,
             coordinates: [ [ [ 0, 0 ], [ 3, 6 ], [ 6, 1 ], [ 0, 0 ] ] ]
          }
       }
     }
   }
)
```

For single-ringed polygons with areas greater than a single hemisphere, see `geowithin-big-polygon`.

### Within a "Big" Polygon

To query with a single-ringed GeoJSON polygon whose area is greater than a single hemisphere, the :query:`$geometry` expression must specify the custom MongoDB coordinate reference system. For example:

```javascript
db.places.find(
   {
     loc: {
       $geoWithin: {
          $geometry: {
             type : "Polygon" ,
             coordinates: [
               [
                 [ -100, 60 ], [ -100, 0 ], [ -100, -60 ], [ 100, -60 ], [ 100, 60 ], [ -100, 60 ]
               ]
             ],
             crs: {
                type: "name",
                properties: { name: "urn:x-mongodb:crs:strictwinding:EPSG:4326" }
             }
          }
       }
     }
   }
)
```
