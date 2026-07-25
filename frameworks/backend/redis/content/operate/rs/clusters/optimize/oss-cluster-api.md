---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/clusters/optimize/oss-cluster-api.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: "OSS Cluster API"
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
- kubernetes
description: Use the Redis OSS Cluster API to improve performance and keep applications current with cluster topology changes.
linktitle: "Redis OSS Cluster API"
weight: $weight
---
{{< embed-md "oss-cluster-api-intro.md"  >}}

You can use the Redis OSS Cluster API along with other Redis Enterprise Software high availability
to get high performance with low latency
and let applications stay current with cluster topology changes, including add node, remove node, and node failover.

For more about working with the OSS Cluster API in Redis Software, see [Enable OSS Cluster API]({{< relref "/operate/rs/databases/configure/oss-cluster-api" >}}). 

To learn how to enable OSS Cluster API in Redis Cloud, see [Clustering Redis databases]({{< relref "/operate/rc/databases/configuration/clustering#cluster-api" >}}).

To enable OSS Cluster API in Kubernetes, see [Enable cluster-aware clients (OSS Cluster API)]({{< relref "/operate/kubernetes/networking/cluster-aware-clients" >}}).
