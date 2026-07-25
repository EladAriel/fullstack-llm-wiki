---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/split-chunks-in-sharded-cluster.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# Split Chunks in a Sharded Cluster

MongoDB automatically splits `chunks <chunk>` to ensure a fair distribution of data across the cluster and the `AutoMerger <automerger-concept>` automatically merges adjacent chunks residing on the same shard.

To split chunks manually, use the :dbcommand:`split` command with either fields `middle` or `find`. :binary:`~bin.mongosh` provides the helper methods :method:`sh.splitFind()` and :method:`sh.splitAt()`.

:method:`~sh.splitFind()` splits the chunk that contains the first document returned that matches this query into two equally sized chunks. You must specify the full namespace (i.e. "`<database>.<collection>`") of the sharded collection to :method:`~sh.splitFind()`. The query in :method:`~sh.splitFind()` does not need to use the shard key, though it nearly always makes sense to do so.

Use :method:`~sh.splitAt()` to split a chunk in two, using the queried document as the lower bound in the new chunk:

> **Note:** :method:`~sh.splitAt()` does not necessarily split the chunk
into two equally sized chunks. The split occurs at the location of
the document matching the query, regardless of where that document is
in the chunk.

> **Seealso:** `initial-chunks-empty-collection`
