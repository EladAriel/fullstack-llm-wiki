---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-dropDatabase-shardedCluster.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you intend to create a new database with the same name as the dropped database, you must run the :dbcommand:`dropDatabase` command on a :binary:`~bin.mongos`.

This ensures that all cluster nodes refresh their metadata cache, which includes the location of the `primary shard<primary-shard>` for the new database. Otherwise, you may miss data on reads, and may not write data to the correct shard. To recover, you must manually intervene.
