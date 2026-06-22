---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2dsphere/query/proximity-to-geojson.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# Query for Locations Near a Point on a Sphere

You can query for location data that appears near a specified point on a sphere.

To query for location data near a specified point, use the :query:`$near` operator:

```javascript
db.<collection>.find( {
   <location field> : {
      $near : {
         $geometry : {
            type : "Point",
            coordinates : [ <longitude>, <latitude> ]
         },
         $maxDistance : <distance in meters>
      }
    }
 } )
```

## About this Task

- .. include:: /includes/indexes/geojson-lat-long.rst
- Specify distance in the `$maxDistance` field in **meters**.
## Before You Begin

#. .. include:: /includes/indexes/geojson-sample-docs.rst

The values in the `loc` field are `GeoJSON points <geojson-point>`.

#. .. include:: /includes/indexes/near-requires-geospatial-index.rst

Create a 2dsphere index on the `loc` field:

```javascript
   db.places.createIndex( { "loc": "2dsphere" } )
```

## Procedure

Use `$near` to query the collection. The following `$near` query returns documents that have a `loc` field within 5000 meters of a GeoJSON point located at `[ -73.92, 40.78 ]`:

```javascript
db.places.find( {
   loc: {
      $near: {
         $geometry: {
            type: "Point",
            coordinates: [ -73.92, 40.78 ]
         },
         $maxDistance : 5000
      }
   }
} )
```

Output:

```javascript
[
  {
    _id: ObjectId("63f7c3b15e5eefbdfef81cab"),
    loc: { type: 'Point', coordinates: [ -73.88, 40.78 ] },
    name: 'La Guardia Airport',
    category: 'Airport'
  },
  {
    _id: ObjectId("63f7c3b15e5eefbdfef81caa"),
    loc: { type: 'Point', coordinates: [ -73.97, 40.77 ] },
    name: 'Central Park',
    category: 'Park'
  }
]
```

Results are sorted by distance from the queried point, from nearest to farthest.

## Learn More

- :query:`$near`
- :query:`$nearSphere`
- :pipeline:`$geoNear`
- `geojson-point`
- `geospatial-restrictions`
