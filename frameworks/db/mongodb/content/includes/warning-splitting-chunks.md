---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-splitting-chunks.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** Be careful when splitting data in a sharded collection to create
new chunks. When you shard a collection that has existing data,
MongoDB automatically creates chunks to evenly distribute the
collection. To split data effectively in a sharded cluster you must
consider the number of documents in a chunk and the average
document size to create a uniform chunk size. When chunks have
irregular sizes, shards may have an equal number of chunks but have
very different data sizes. Avoid creating splits that lead to a
collection with differently sized chunks.
