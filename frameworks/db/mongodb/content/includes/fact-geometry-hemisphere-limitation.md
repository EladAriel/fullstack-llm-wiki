---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-geometry-hemisphere-limitation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For |geo-operator-method|, if you specify a single-ringed polygon that has an area greater than a single hemisphere, include the custom MongoDB coordinate reference system in the :query:`$geometry <$geometry>` expression. Otherwise, |geo-operator-method| queries for the complementary geometry. For all other GeoJSON polygons with areas greater than a hemisphere, |geo-operator-method| queries for the complementary geometry.
