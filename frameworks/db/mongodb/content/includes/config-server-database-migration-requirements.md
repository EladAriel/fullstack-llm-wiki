---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/config-server-database-migration-requirements.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If the embedded config server is also the primary of one of the cluster's databases, then you must manually move the databases to a new shard after migrating all data from the shard. See the :dbcommand:`movePrimary` command and the `remove-shards-from-cluster-tutorial` for more information.
