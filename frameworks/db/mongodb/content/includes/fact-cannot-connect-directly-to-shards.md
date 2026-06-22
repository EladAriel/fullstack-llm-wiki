---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-cannot-connect-directly-to-shards.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.0, you can only run `certain commands <node-direct-commands>` on nodes in sharded clusters. If you attempt to connect directly to a node and run an unsupported command, MongoDB returns an error:

```none
"You are connecting to a sharded cluster improperly by connecting directly 
to a shard. Please connect to the cluster via a router (mongos)."
```

To run a non-supported database command directly against a node in a sharded cluster, you must either connect to `mongos` or have the maintenance-only `directShardOperations` role.
