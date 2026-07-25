---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-cannot-connect-directly-to-shards.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.0, you can only run `certain commands <node-direct-commands>` on nodes in sharded clusters. If you attempt to connect directly to a node and run an unsupported command, MongoDB returns an error:

```none
"You are connecting to a sharded cluster improperly by connecting directly 
to a shard. Please connect to the cluster via a router (mongos)."
```

To run a non-supported database command directly against a node in a sharded cluster, you must either connect to `mongos` or have the maintenance-only `directShardOperations` role.
