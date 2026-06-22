---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2dsphere/create.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Create a 2dsphere Index

.. include:: /includes/indexes/2dsphere-index-intro.rst

To create a 2dsphere index, use the :method:`db.collection.createIndex()` method and specify the string `"2dsphere"` as the index type:

.. include:: /includes/indexes/code-examples/create-2dsphere-index.rst

The values in the `<location field>` must be either:

- `GeoJSON objects <geospatial-geojson>`
- `Legacy coordinate pairs <geospatial-legacy>`
## Before You Begin

.. include:: /includes/indexes/geojson-sample-docs.rst

The values in the `loc` field are `GeoJSON points <geojson-point>`.

## Procedure

The following operation creates a 2dsphere index on the location field `loc`:

```javascript
db.places.createIndex( { loc : "2dsphere" } )
```

## Next Steps

After you create a 2dsphere index, you can use the index for geospatial queries. To learn more, see `2dsphere-index-query`.

## Learn More

- `2dsphere-index`
- `geospatial-queries`
- `geospatial-restrictions`
