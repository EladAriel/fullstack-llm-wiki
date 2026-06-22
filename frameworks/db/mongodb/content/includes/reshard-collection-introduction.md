---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-collection-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In a collection resharding operation, a shard can be a:

- **donor**, which currently stores `chunks <chunk>` for the
sharded collection.

- **recipient**, which stores new chunks for the sharded collection
based on the `shard keys <shard key>` and `zones <zone-sharding>`.

A shard can be donor and a recipient at the same time.

The config server primary is always the resharding coordinator and starts each phase of the resharding operation.
