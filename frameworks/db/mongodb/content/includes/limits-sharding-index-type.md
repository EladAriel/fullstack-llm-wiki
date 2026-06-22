---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/limits-sharding-index-type.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A `shard key` index can be an ascending index on the shard key, a compound index that starts with the shard key and specifies ascending order for the shard key, or a `hashed index <index-type-hashed>`.

A `shard key` index cannot be:

- A descending index on the shard key
- A `partial index <index-type-partial>`
- Any of the following index types:
- `Geospatial <index-feature-geospatial>`
- `Multikey <index-type-multikey>`
- `Text <index-type-text>`
- `Wildcard <wildcard-index-core>`
