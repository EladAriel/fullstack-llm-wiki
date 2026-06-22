---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/geospatial/2dsphere.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# 2dsphere Indexes

.. include:: /includes/indexes/2dsphere-index-intro.rst

The values of the indexed field must be either:

- `GeoJSON objects <geospatial-geojson>`
- `Legacy coordinate pairs <geospatial-legacy>`
For legacy coordinate pairs, the 2dsphere index converts the data to `GeoJSON points <geojson-point>`.

To create a 2dsphere index, specify the string `2dsphere` as the index type:

.. include:: /includes/indexes/code-examples/create-2dsphere-index.rst

> **Note:** When `creating a a 2dsphere index <2dsphere-index-create>`, the first
value, or longitude, must be between -180 and 180, inclusive. The second value,
or latitude, must be between -90 and 90, inclusive. These coordinates "wrap"
around the sphere. For example, -179.9 and +179.9 are near neighbors.

## Use Cases

Use 2dsphere indexes to query and perform calculations on location data where the data points appear on Earth, or another spherical surface. For example:

- A food delivery application uses 2dsphere indexes to support
searches for nearby restaurants.

- A route planning application uses 2dsphere indexes to calculate
the shortest distance between rest stops.

- A city planner uses 2dsphere indexes to find parks that exist within
city limits.

## Get Started

To learn how to create and query 2dsphere indexes, see:

- `2dsphere-index-create`
- `2dsphere-query-geojson-objects-polygon`
- `2dsphere-query-geojson-proximity`
- `2dsphere-query-intersection`
- `2dsphere-query-points-within-circle-on-sphere`
## Details

2dsphere indexes are always `sparse <index-type-sparse>` and have special behaviors when created as part of a `compound index <index-type-compound>`.

### `sparse` Property

2dsphere indexes are always `sparse <index-type-sparse>`. When you create a 2dsphere index, MongoDB ignores the `sparse` option.

If an existing or newly inserted document does not contain a 2dsphere index field (or the field is `null` or an empty array), MongoDB does not add an entry for the document to the index.

### Compound 2dsphere Indexes

- For a compound index that includes a 2dsphere index key along with
keys of other types, only the 2dsphere index field determines whether the index references a document.

- A compound 2dsphere index can reference multiple location and
non-location fields. In contrast, a compound `2d <2d-index>` index can only reference one location field and one other field.

### 2dsphereIndexVersion

.. include:: /includes/fact-2dsphereIndexVersion-4.rst

## Learn More

- `geospatial-queries`
- `geospatial-query-operators`
- `geospatial-tutorial-restaurants`
- `geospatial-restrictions`
## Contents

- Create </core/indexes/index-types/geospatial/2dsphere/create>
- Query </core/indexes/index-types/geospatial/2dsphere/query>
- Versions </core/indexes/index-types/geospatial/2dsphere/2dsphere-index-versions>
