---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharded-clusters-users.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In general, to create users for a sharded clusters, connect to the :binary:`~bin.mongos` and add the sharded cluster users.

However, some maintenance operations require direct connections to specific shards in a sharded cluster. To perform these operations, you must connect directly to the shard and authenticate as a shard-local administrative user.

Shard-local users exist only in the specific shard and should only be used for shard-specific maintenance and configuration. You cannot connect to the `mongos` with shard-local users.
