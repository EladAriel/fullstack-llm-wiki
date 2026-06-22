---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding-database-migration-requirements.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Each database in a sharded cluster has a primary shard. If the shard you want to drain is also the primary of one of the cluster's databases, then you must manually move the databases to a new shard after migrating all data from the shard. See the :dbcommand:`movePrimary` command and the `remove-shards-from-cluster-tutorial` for more information.
