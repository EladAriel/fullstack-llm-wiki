---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-reshard-init-shard-mongosh.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When you run the :method:`sh.shardCollection` method, the balancer begins distributing the collection data to other shards in the cluster. A single shard can only participate in one chunk migration at a time. When MongoDB succeeds in copying a range of data from one shard to another, the range on the donor shard is marked for removal by the range deleter. This process is slow and resource intensive.

Starting in MongoDB 8.0, if your deployment meets the `resource requirements <reshard-to-same-key-req>`, it's recommended that you use the :method:`sh.shardAndDistributeCollection` method to shard the collection. This method wraps the :dbcommand:`shardCollection` and :dbcommand:`reshardCollection` commands to shard the collection and immediately reshard it to the same key. This causes MongoDB to rebalance data across the shards without waiting on the balancer.

For more information, see `reshard-to-same-key`.
