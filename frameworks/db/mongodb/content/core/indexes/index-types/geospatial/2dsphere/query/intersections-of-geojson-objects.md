---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2dsphere/query/intersections-of-geojson-objects.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================================

# Query for Locations that Intersect a GeoJSON Object

You can query for location data that intersects with a `GeoJSON object <geospatial-indexes-store-geojson>`. For example, consider an application that stores coordinates of gas stations. You can create a GeoJSON `LineString <geojson-linestring>` that represents a road trip, and query for gas stations that intersect with the road trip route.

To query for location data that intersects with a GeoJSON object, use the :query:`$geoIntersects` operator:

```javascript
db.<collection>.find( {
   <location field> : {
      $geoIntersects : {
         $geometry : {
            type : "<GeoJSON object type>",
            coordinates : [ <coordinates> ]
         }
       }
    }
 } )
```

## About this Task

- .. include:: /includes/indexes/geojson-lat-long.rst
- A location intersects with an object if it shares at least one point
with the specified object. This includes objects that have a shared edge.

- .. include:: /includes/indexes/geospatial-index-not-required.rst
## Before You Begin

Create a `gasStations` collection that contains these documents:

```javascript
db.gasStations.insertMany( [
   {
      loc: { type: "Point", coordinates: [ -106.31, 35.65 ] },
      state: "New Mexico",
      country: "United States",
      name: "Horizons Gas Station"
   },
   {
      loc: { type: "Point", coordinates: [ -122.62, 40.75 ] },
      state: "California",
      country: "United States",
      name: "Car and Truck Rest Area"
   },
   {
      loc: { type: "Point", coordinates: [ -72.71, 44.15 ] },
      state: "Vermont",
      country: "United States",
      name: "Ready Gas and Snacks"
   }
] )
```

## Procedure

The following `$geoIntersects` query specifies a `LineString` containing four points and returns documents that intersect with the line:

```javascript
db.gasStations.find( {
   loc: {
      $geoIntersects: {
         $geometry: {
            type: "LineString",
            coordinates: [
               [ -105.82, 33.87 ],
               [ -106.01, 34.09 ],
               [ -106.31, 35.65 ],
               [ -107.39, 35.98 ]
            ]
          }
      }
   }
} )
```

Output:

```javascript
[
   {
     _id: ObjectId("63f658d45e5eefbdfef81ca4"),
     loc: { type: 'Point', coordinates: [ -106.31, 35.65 ] },
     state: 'New Mexico',
     country: 'United States',
     name: 'Horizons Gas Station'
   }
]
```

## Learn More

- :query:`$geoIntersects`
- `geojson-linestring`
- `2dsphere-query-geojson-objects-polygon`
- `geospatial-restrictions`
