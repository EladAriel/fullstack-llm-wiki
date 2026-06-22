---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/map-reduce-concurrency.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
