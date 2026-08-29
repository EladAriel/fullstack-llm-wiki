---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/how-many-databases-software.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.095920Z"
---
# How Many Databases Software

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