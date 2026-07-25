---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/geospatial-indexes-intro.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Geospatial indexes support queries on data stored as `GeoJSON <geospatial-geojson>` objects or `legacy coordinate pairs <geospatial-legacy>`. You can use geospatial indexes to improve performance for queries on geospatial data or to run certain geospatial queries.

MongoDB provides two types of geospatial indexes:

- `2dsphere-index`, which support queries that interpret
geometry on a sphere.

- `2d-index`, which support queries that interpret geometry
on a flat surface.
