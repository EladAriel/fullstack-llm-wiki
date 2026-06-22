---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/geospatial-indexes-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Geospatial indexes support queries on data stored as `GeoJSON <geospatial-geojson>` objects or `legacy coordinate pairs <geospatial-legacy>`. You can use geospatial indexes to improve performance for queries on geospatial data or to run certain geospatial queries.

MongoDB provides two types of geospatial indexes:

- `2dsphere-index`, which support queries that interpret
geometry on a sphere.

- `2d-index`, which support queries that interpret geometry
on a flat surface.
