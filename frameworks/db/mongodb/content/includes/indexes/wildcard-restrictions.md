---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-restrictions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Wildcard indexes do not support:

- `2d (Geospatial) indexes <2d-index-internals>`
- `2dsphere (Geospatial) indexes <2dsphere-index>`
- `Hashed indexes <index-type-hashed>`
- `Time to Live (TTL) indexes <index-feature-ttl>`
- `Text indexes <index-feature-text>`
- `Unique indexes <index-type-unique>`
Wildcard indexes are `sparse <index-type-sparse>` indexes. They do not support queries when an indexed field does not exist. A wildcard index will index the document if the wildcard field has a `null` value.

Starting in MongoDB 7.0, wildcard indexes support ascending (`1`) and descending (`-1`) sort order. Earlier versions only supported ascending order.
