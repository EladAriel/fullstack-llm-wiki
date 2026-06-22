---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/limits-sharding-maximum-documents-range.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

By default, MongoDB cannot move a range if the number of documents in the range is greater than 2 times the result of dividing the configured `range size <sharding-range-size>` by the average document size. If MongoDB can move a sub-range of a chunk and reduce the size to less than that, the balancer does so by migrating a range. :method:`db.collection.stats()` includes the `avgObjSize` field, which represents the average document size in the collection.

For chunks that are `too large to migrate <migration-chunk-size-limit>`:

- The balancer setting `attemptToBalanceJumboChunks` allows the
balancer to migrate chunks too large to move as long as the chunks are not labeled `jumbo <jumbo-chunk>`. See `balance-chunks-that-exceed-size-limit` for details.

When issuing :dbcommand:`moveRange` and :dbcommand:`moveChunk` commands, it's possible to specify the `forceJumbo <moverange-forceJumbo>` option to allow for the migration of ranges that are too large to move. The ranges may or may not be labeled `jumbo <jumbo-chunk>`.
