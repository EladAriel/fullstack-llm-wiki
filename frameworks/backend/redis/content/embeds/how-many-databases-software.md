---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/how-many-databases-software.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

The number of databases is unlimited. The limiting factor is the
available memory in the cluster, and the number of shards in the
subscription.

Note that the impact of the specific database configuration on the 
number of shards it consumes. For example:

- Enabling database replication, without enabling database clustering, 
  creates two shards: a master shard and a replica shard.
- Enabling database clustering creates as many database shards as you 
  configure.
- Enabling both database replication and database clustering creates 
  double the number of database shards you configure.