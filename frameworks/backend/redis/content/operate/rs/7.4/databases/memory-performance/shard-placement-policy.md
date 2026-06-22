---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/databases/memory-performance/shard-placement-policy.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Shard placement policy
alwaysopen: false
categories:
- docs
- operate
- rs
description: Detailed info about the shard placement policy.
linkTitle: Shard placement policy
weight: 30
url: '/operate/rs/7.4/databases/memory-performance/shard-placement-policy/'
---
In Redis Enterprise Software, the location of master and replica shards on the cluster nodes can impact the database and node performance.
Master shards and their corresponding replica shards are always placed on separate nodes for data resiliency.
The shard placement policy helps to maintain optimal performance and resiliency.

{{< embed-md "shard-placement-intro.md"  >}}

## Shard placement policies

### Dense shard placement policy

In the dense policy, the cluster places the database shards on as few nodes as possible.
When the node is not able to host all of the shards, some shards are moved to another node to maintain optimal node health.

For example, for a database with two master and two replica shards on a cluster with three nodes and a dense shard placement policy,
the two master shards are hosted on one node and the two replica shards are hosted on another node.

For Redis on RAM databases without the OSS cluster API enabled, use the dense policy to optimize performance.

{{< image filename="/images/rs/dense_placement.png" >}}

*Figure: Three nodes with two master shards (red) and two replica shards (white) with a dense placement policy*

### Sparse shard placement policy

In the sparse policy, the cluster places shards on as many nodes as possible to distribute the shards of a database across all available nodes.
When all nodes have database shards, the shards are distributed evenly across the nodes to maintain optimal node health.

For example, for a database with two master and two replica shards on a cluster with three nodes and a sparse shard placement policy:

- Node 1 hosts one of the master shards
- Node 2 hosts the replica for the first master shard
- Node 3 hosts the second master shard
- Node 1 hosts for the replica shard for master shard 2

For Redis on RAM databases with OSS cluster API enabled and for databases with Auto Tiering enabled, use the sparse policy to optimize performance.

{{< image filename="/images/rs/sparse_placement.png" >}}

*Figure: Three nodes with two master shards (red) and two replica shards (white) with a sparse placement policy*

## Related articles

You can [configure the shard placement policy]({{< relref "/operate/rs/7.4/databases/configure/shard-placement.md" >}}) for each database.
