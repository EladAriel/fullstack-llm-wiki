---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2d/create/define-location-precision.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================

# Define Location Precision for a 2d Index

In a 2d index, location precision is defined by the size in bits of the `geohash` values used to store the indexed data. By default, 2d indexes use 26 bits of precision, which is equivalent to approximately two feet (60 centimeters).

Location precision affects performance for insert and read operations.

To change the default precision, specify a `bits` value when you create the 2d index. You can specify a `bits` value between 1 and 32, inclusive.

```javascript
db.<collection>.createIndex(
   { <location field>: "2d" },
   { bits: <bit precision> }
)
```

## About this Task

Location precision affects query performance:

- Lower precision improves performance for insert and update operations,
and uses less storage.

- Higher precision improves performance for read operations because
queries scan smaller portions of the index to return results.

Location precision does not affect query accuracy. Grid coordinates are always used in the final query processing.

## Before You Begin

.. include:: /includes/indexes/2d-sample-docs.rst

## Procedure

Create a 2d index on the `address` field. Specify a location precision of `32` bits:

```javascript
db.contacts.createIndex(
   { address: "2d" },
   { bits: 32 }
)
```

## Next Steps

.. include:: /includes/indexes/2d-index-create-next-steps.rst

## Learn More

- `geospatial-indexes-geohash`
- `geospatial-geometry`
- `geospatial-legacy`
