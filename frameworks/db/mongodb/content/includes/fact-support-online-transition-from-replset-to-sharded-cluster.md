---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-support-online-transition-from-replset-to-sharded-cluster.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB supports online transition from a replica set to a 1-shard cluster by allowing commands to be run directly against a shard. However, once the cluster has more than one shard, only the `listed commands <node-direct-commands>` can be run directly against the shard without the maintenance-only `directShardOperations` role.
