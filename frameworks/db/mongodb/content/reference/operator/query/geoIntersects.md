---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/geoIntersects.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================================

# $geoIntersects (query predicate operator)

## Definition

## Behavior

### Geospatial Indexes

:query:`$geoIntersects` uses spherical geometry. :query:`$geoIntersects` does not require a geospatial index. However, a geospatial index will improve query performance. Only the `2dsphere <2dsphere-index>` geospatial index supports :query:`$geoIntersects`.

### Degenerate Geometry

:query:`$geoIntersects` does not guarantee that it will consider a polygon to intersect with its own edges; its own vertices; or another polygon sharing vertices or edges but no interior space.

### "Big" Polygons

.. include:: /includes/fact-geometry-hemisphere-limitation.rst

## Examples

### Intersects a Polygon

The following example uses :query:`$geoIntersects` to select all `loc` data that intersect with the `geojson-polygon` defined by the `coordinates` array. The area of the polygon is less than the area of a single hemisphere:

```javascript
db.places.find(
   {
     loc: {
       $geoIntersects: {
          $geometry: {
             type: "Polygon" ,
             coordinates: [
               [ [ 0, 0 ], [ 3, 6 ], [ 6, 1 ], [ 0, 0 ] ]
             ]
          }
       }
     }
   }
)
```

For single-ringed polygons with areas greater than a single hemisphere, see `geointersects-big-polygon`.

### Intersects a "Big" Polygon

To query with a single-ringed GeoJSON polygon whose area is greater than a single hemisphere, the :query:`$geometry` expression must specify the custom MongoDB coordinate reference system. For example:

```javascript
db.places.find(
   {
     loc: {
       $geoIntersects: {
          $geometry: {
             type : "Polygon",
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
