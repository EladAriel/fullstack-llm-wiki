---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/defragment-sharded-collections-status.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Defragmentation uses the following phases to reduce the number of chunks in a collection and improve performance:

1. Merge chunks on the same shard that can be merged.
#. Migrate smaller chunks to other shards. A small chunk is one that contains data less than 25% of the `chunkSize` setting. #. Merge remaining chunks on the same shard that can be merged.
