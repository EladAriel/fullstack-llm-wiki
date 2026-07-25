---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-reshard-init-shard.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When you run the :dbcommand:`shardCollection` command, the balancer begins distributing the collection data to other shards in the cluster. A single shard can only participate in one chunk migration at a time. When MongoDB succeeds in copying a range of data from one shard to another, the range on the donor shard is marked for removal by the range deleter. This process is slow and resource intensive.

Starting in MongoDB 8.0, if your deployment meets the `resource requirements <reshard-to-same-key-req>`, it's recommended you use the :dbcommand:`reshardCollection` command to perform this initial balancing of data by resharding to the same key. This causes MongoDB to rebalance data across the shards without waiting on the balancer.

To use the :dbcommand:`reshardCollection` command to perform the initial balancing:

#. Use the :dbcommand:`shardCollection` command to configure the collection as a sharded collection.

#. Use the :dbcommand:`reshardCollection` to reshard to the same shard key by setting the `forceRedistribution` option to `true`. MongoDB then balances the data across the shards.

For more information, see `reshard-to-same-key`.
