---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-support-online-transition-from-replset-to-sharded-cluster.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB supports online transition from a replica set to a 1-shard cluster by allowing commands to be run directly against a shard. However, once the cluster has more than one shard, only the `listed commands <node-direct-commands>` can be run directly against the shard without the maintenance-only `directShardOperations` role.
