---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-collection-introduction.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In a collection resharding operation, a shard can be a:

- **donor**, which currently stores `chunks <chunk>` for the
sharded collection.

- **recipient**, which stores new chunks for the sharded collection
based on the `shard keys <shard key>` and `zones <zone-sharding>`.

A shard can be donor and a recipient at the same time.

The config server primary is always the resharding coordinator and starts each phase of the resharding operation.
