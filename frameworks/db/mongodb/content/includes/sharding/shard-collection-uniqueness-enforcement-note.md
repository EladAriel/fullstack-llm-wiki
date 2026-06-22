---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/shard-collection-uniqueness-enforcement-note.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** Sharded clusters do not enforce the uniqueness constraint on `_id` fields
across the cluster when the `_id` field is not the shard key.
If the `_id` field is not the shard key, the uniqueness constraint only
applies to the shard that stores the document. This means that two or more
documents can have the same `_id` value, provided they occur on different
shards.
For example, consider a sharded collection with shard key ``{x:
1} that spans two shards A and B. Because the id`` key is
not the shard key, the collection could have a document
with `_id` value `1` in shard A and another document with
`_id` value `1` in shard B.
In cases where the `_id` field is not the shard key, MongoDB expects
applications to ensure the uniqueness of `_id` values across the shards,
for example, by using a unique identifier to populate the `_id` field.
