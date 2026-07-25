---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/map-reduce-concurrency.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================

# Map-Reduce Concurrency

> **Note:** .. include:: /includes/fact-use-aggregation-not-map-reduce.rst

The map-reduce operation is composed of many tasks, including reads from the input collection, executions of the `map` function, executions of the `reduce` function, writes to a temporary collection during processing, and writes to the output collection.

During the operation, map-reduce takes the following locks:

- The read phase takes a read lock.  It yields every 100 documents.
- The insert into the temporary collection takes a write lock for a
single write.

- If the output collection does not exist, the creation of the output
collection takes a write lock.

- If the output collection exists, then the output actions (i.e.
`merge`, `replace`, `reduce`) take a write lock. This write lock is global, and blocks all operations on the :binary:`~bin.mongod` instance.
