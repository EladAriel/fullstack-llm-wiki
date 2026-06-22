---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/mergeability.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`mergeAllChunksOnShard` finds and merges all mergeable chunks for a collection on the same shard. Two or more contiguous chunks in the same collection are **mergeable** when they meet all of these conditions:

- They are owned by the same shard.
- They are not `jumbo <jumbo-chunk>` chunks. `jumbo` chunks are
not mergeable because they cannot participate in migrations.

- Their history can be purged safely, without breaking transactions and
snapshot reads:

- The last migration involving the chunk happened at least as many
seconds ago as the value of :parameter:`minSnapshotHistoryWindowInSeconds`.

- The last migration involving the chunk happened at least as many
seconds ago as the value of :parameter:`transactionLifetimeLimitSeconds`.
