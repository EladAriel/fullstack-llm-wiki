---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/shard-placement-intro.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

In addition to the shard placement policy, considerations that determine shard placement are:

- Separation of master and replica shards
- Available persistence and Auto Tiering storage
- [Rack-zone awareness]({{< relref "/operate/rs/clusters/configure/rack-zone-awareness" >}})
- Memory available to host the database when fully populated

The shard placement policies are:

- `dense` - Place as many shards as possible on the smallest number of nodes to reduce the latency between the proxy and the database shards;
    Recommended for Redis on RAM databases to optimize memory resources
- `sparse` - Spread the shards across as many nodes in the cluster as possible to spread the traffic across cluster nodes;
    Recommended for databases with Auto Tiering enabled to optimize disk resources

When you create a Redis Software cluster, the default shard placement policy (`dense`) is assigned to all databases that you create on the cluster.

You can:

- Change the default shard placement policy for the cluster to `sparse` so that the cluster applies that policy to all databases that you create
- Change the shard placement policy for each database after the database is created