---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-geometry-hemisphere-limitation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For |geo-operator-method|, if you specify a single-ringed polygon that has an area greater than a single hemisphere, include the custom MongoDB coordinate reference system in the :query:`$geometry <$geometry>` expression. Otherwise, |geo-operator-method| queries for the complementary geometry. For all other GeoJSON polygons with areas greater than a hemisphere, |geo-operator-method| queries for the complementary geometry.
