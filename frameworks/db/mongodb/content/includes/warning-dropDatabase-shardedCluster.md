---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-dropDatabase-shardedCluster.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you intend to create a new database with the same name as the dropped database, you must run the :dbcommand:`dropDatabase` command on a :binary:`~bin.mongos`.

This ensures that all cluster nodes refresh their metadata cache, which includes the location of the `primary shard<primary-shard>` for the new database. Otherwise, you may miss data on reads, and may not write data to the correct shard. To recover, you must manually intervene.
