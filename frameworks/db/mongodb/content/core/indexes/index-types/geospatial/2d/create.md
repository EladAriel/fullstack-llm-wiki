---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2d/create.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Create a 2d Index

2d indexes support queries on location data in a `flat, Euclidean plane <geospatial-geometry>`.

To create a 2d index, use the :method:`db.collection.createIndex()` method. The index type is `"2d"`:

.. include:: /includes/indexes/code-examples/create-2d-index.rst

## About this Task

- The values in the `<location field>` must be :ref:`legacy coordinate
pairs <geospatial-legacy>`.

- When specifying legacy coordinate pairs, list the **longitude** first,
and then **latitude**.

- Valid longitude values are between `-180` and `180`, both
inclusive.

- Valid latitude values are between `-90` and `90`, both
inclusive.

## Before You Begin

.. include:: /includes/indexes/2d-sample-docs.rst

## Procedure

Create a 2d index on the `address` field:

```javascript
db.contacts.createIndex( { address : "2d" } )
```

## Next Steps

After you create a 2d index, you can use your 2d index to support calculations on location data. To see examples of queries that use 2d indexes, see:

- `2d-index-proximity-query`
## Learn More

- `2d-index-define-location-precision`
- `2d-index-define-location-range`
- `geospatial-restrictions`
- To create an index that supports calculations on spherical surfaces,
see `2dsphere-index`.

## Contents

- Location Precision </core/indexes/index-types/geospatial/2d/create/define-location-precision>
- Location Range </core/indexes/index-types/geospatial/2d/create/define-location-range>
