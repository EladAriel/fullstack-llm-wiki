---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/defragment-sharded-collections-status.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Defragmentation uses the following phases to reduce the number of chunks in a collection and improve performance:

1. Merge chunks on the same shard that can be merged.
#. Migrate smaller chunks to other shards. A small chunk is one that contains data less than 25% of the `chunkSize` setting. #. Merge remaining chunks on the same shard that can be merged.
