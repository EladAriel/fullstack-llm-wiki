---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/oss-cluster-api-intro.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.097055Z"
---
# Oss Cluster Api Intro

OSS Cluster API reduces access times and latency with near-linear scalability.
The OSS Cluster API provides a simple mechanism for Redis clients to know the cluster topology.

Clients must first connect to the master node to get the cluster topology,
and then they connect directly to the Redis proxy on each node that hosts a master shard.

{{< note >}}
You must use a client that supports the cluster API to connect to a database
that has the cluster API enabled.
{{< /note >}}
