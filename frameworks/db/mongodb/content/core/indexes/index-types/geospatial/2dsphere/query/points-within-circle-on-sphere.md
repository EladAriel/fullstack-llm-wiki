---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2dsphere/query/points-within-circle-on-sphere.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Query for Locations within a Circle on a Sphere

You can query for location data within a circle on the surface of a sphere. Use these queries to return data within a [spherical cap](https://en.wikipedia.org/w/index.php?title=Spherical_cap&oldid=1107980309)_.

To query for location data within a circle on a sphere, use :query:`$geoWithin` with the :query:`$centerSphere` operator. In the `$centerSphere` operator, specify the coordinates and radius of the circle to query within:

```javascript
db.<collection>.find( {
   <location field> : {
      $geoWithin : {
         $centerSphere: [
            [ <longitude>, <latitude> ],
            <radius>
         ]
       }
    }
 } )
```

## About this Task

- .. include:: /includes/indexes/geojson-lat-long.rst
- In the `$centerSphere` operator, specify the circle's radius in
**radians**. To convert other units to and from radians, see `calculate-distance-spherical-geometry`.

- This example calculates distance in kilometers. To convert
kilometers to radians, divide the kilometer value by `6378.1`.

- .. include:: /includes/indexes/geospatial-index-not-required.rst
## Before You Begin

.. include:: /includes/indexes/geojson-sample-docs.rst

## Procedure

To query the collection, use `$geoWithin` with the `$centerSphere` operator:

```javascript
db.places.find( {
   loc: {
      $geoWithin: {
         $centerSphere: [
            [ -1.76, 51.16 ],
            10 / 6378.1
         ]
      }
   }
} )
```

The query returns documents where the `loc` field is within a 10 kilometer radius of a point at longitude `-1.76`, latitude `51.16`.

Output:

```javascript
[
   {
     _id: ObjectId("63fd205e4a08b5e248c03e32"),
     loc: { type: 'Point', coordinates: [ -1.83, 51.18 ] },
     name: 'Stonehenge',
     category: 'Monument'
   }
]
```

## Learn More

- :query:`$geoWithin`
- :query:`$centerSphere`
- `2dsphere-query-geojson-objects-polygon`
- `2dsphere-query-intersection`
- `2dsphere-query-geojson-proximity`
- `geospatial-restrictions`
