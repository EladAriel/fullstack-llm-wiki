---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2d/query/points-within-a-shape.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================================

# Query for Locations within a Shape on a Flat Surface

To query for location data within a specified shape on a flat surface, use the :query:`$geoWithin` operator. To use `$geoWithin` with data that appears on a flat surface, use this syntax:

```javascript
db.<collection>.find( {
   <location field> : {
      $geoWithin : {
         <shape operator> : <coordinates>
      }
    }
 } )
```

Replace these values for your query:

## About this Task

`$geoWithin` does not require a geospatial index. However, a geospatial index improves query performance.

## Before You Begin

.. include:: /includes/indexes/2d-sample-docs.rst

## Procedure

Use `$geoWithin` to query the `contacts` collection. The following `$geoWithin` query uses the :query:`$box` operator to return documents that appear within a specified rectangle:

```javascript
db.contacts.find( {
   address: {
      $geoWithin: {
         $box: [ [ 49, 40 ], [ 60, 60 ] ]
      }
   }
} )
```

Output:

```javascript
[
  {
    _id: ObjectId("647e4e496cdaf4dc323ec92a"),
    name: 'Evander Otylia',
    phone: '202-555-0193',
    address: [ 55.5, 42.3 ]
  }
]
```

The values of the `$box` operator represent the bottom-left and top-right corners of of the rectangle to query within.

The `$geoWithin` query shown earlier returns documents that are within a rectangle that has these vertices:

- `[ 49, 40 ]`
- `[ 49, 60 ]`
- `[ 60, 60 ]`
- `[ 60, 40 ]`
## Learn More

To learn how to use the `$geoWithin` operator with other shapes, see these pages:

- To query within a polygon, see :query:`$polygon`.
- To query within a circle, see :query:`$center`.
