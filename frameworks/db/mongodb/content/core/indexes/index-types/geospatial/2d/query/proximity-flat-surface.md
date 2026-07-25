---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2d/query/proximity-flat-surface.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================================

# Query for Locations Near a Point on a Flat Surface

You can query for location data that appears near a specified point on a flat surface.

To query for location data near a specified point, use the :query:`$near` operator:

```javascript
db.<collection>.find( {
   <location field> : {
      $near : [ <longitude>, <latitude> ],
      $maxDistance : <distance in meters>
   }
} )
```

## About this Task

- When specifying coordinate pairs in the `$near` operator, list the
**longitude** first, and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
inclusive.

- Valid latitude values are between `-90` and `90`, both
inclusive.

- Specify distance in the `$maxDistance` field in **meters**.
## Before you Begin

#. .. include:: /includes/indexes/2d-sample-docs.rst

#. .. include:: /includes/indexes/near-requires-geospatial-index.rst

Create a 2d index on the `address` field:

```javascript
   db.contacts.createIndex( { address: "2d" } )
```

## Procedure

Use `$near` to query the collection. The following `$near` query returns documents that have an `address` field within 50 meters of the coordinate pair `[ -73.92, 40.78 ]`:

```javascript
db.contacts.find( {
   address: {
      $near: [ -73.92, 40.78 ],
      $maxDistance : 50
   }
} )
```

Output:

```javascript
[
   {
     _id: ObjectId("640a3dd9c639b6f094b00e89"),
     name: 'Georgine Lestaw',
     phone: '714-555-0107',
     address: [ -74, 44.74 ]
   }
]
```

Results are sorted by distance from the queried point, from nearest to farthest.

## Learn More

- :query:`$near`
- :pipeline:`$geoNear`
- `geospatial-restrictions`
- To perform proximity queries on a spherical surface, see
`2dsphere-query-geojson-proximity`.
