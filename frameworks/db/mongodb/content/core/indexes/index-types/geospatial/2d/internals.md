---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2d/internals.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# 2d Index Internals

This document explains the internals of `2d indexes <2d-index>`. This material is not necessary for normal operations or application development, but may be useful for troubleshooting and for further understanding.

## Geohash Values

When you create a geospatial index on a field that contains `legacy coordinate pairs <legacy coordinate pairs>`, MongoDB computes `geohash` values for the coordinate pairs within the specified `location range <2d-index-define-location-range>`, then indexes the geohash values.

To calculate a geohash value, MongoDB recursively divides a two-dimensional map into quadrants. Then, it assigns each quadrant a two-bit value. For example, a two-bit representation of four quadrants would be:

```javascript
01  11

00  10
```

These two-bit values (`00`, `01`, `10`, and `11`) represent each of the quadrants and all points within each quadrant. Each quadrant has a corresponding geohash value:

To provide additional precision, MongoDB can divide each quadrant into sub-quadrants. Each sub-quadrant has the geohash value of the containing quadrant concatenated with the value of the sub-quadrant. For example, the geohash for the top-right quadrant is `11`, and the geohash for the sub-quadrants would be (clockwise from the top left):

- `1101`
- `1111`
- `1110`
- `1100`
calculate a more precise geohash, continue dividing the sub-quadrant and concatenate the two-bit identifier for each division. The more "bits" in the hash identifier for a given point, the smaller possible area that the hash can describe and the higher the resolution of the geospatial index.

## Multi-Location Documents for 2d Indexes

While 2d indexes do not support more than one location field in a document, you can use a `multi-key index <index-type-multi-key>` to index multiple coordinate pairs in a single document. For example, in the following document, the `locs` field holds an array of coordinate pairs:

```javascript
db.places.insertOne( {
   locs : [
      [ 55.5 , 42.3 ],
      [ -74 , 44.74 ],
      { long : 55.5 , lat : 42.3 }
   ]
} )
```

The values in the `locs` array may be either:

- Arrays, as in `[ 55.5, 42.3 ]`.
- Embedded documents, as in `{ long : 55.5 , lat : 42.3 }`.
To index all of the coordinate pairs in the `locs` array, create a 2d index on the `locs` field:

```javascript
db.places.createIndex( { "locs": "2d" } )
```

### Embedded Multi-Location Documents

You can store location data as a field inside of an embedded document. For example, you can have an array of embedded documents where each embedded document has a field that contains location data.

In the following document, the `addresses` field is an array of embedded documents. The embedded documents contain a `loc` field, which is a coordinate pair:

```javascript
db.records.insertOne( {
   name : "John Smith",
   addresses : [
      {
         context : "home" ,
         loc : [ 55.5, 42.3 ]
      },
      {
         context : "work",
         loc : [ -74 , 44.74 ]
      }
   ]
} )
```

To index all of the `loc` values in the `addresses` array, create a 2d index on the `addresses.loc` field:

```javascript
db.records.createIndex( { "addresses.loc": "2d" } )
```

## Learn More

- `geospatial-legacy`
- `2dsphere-index-query`
- `index-type-multikey`
- `geospatial-restrictions`
