---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/clusters/optimize/oss-cluster-api.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: "OSS Cluster API"
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
description: Use the OSS Cluster API to improve performance and keep applications current with cluster topology changes.
linktitle: "OSS Cluster API"
weight: $weight
url: '/operate/rs/7.4/clusters/optimize/oss-cluster-api/'
---
{{< embed-md "oss-cluster-api-intro.md"  >}}

You can use the OSS Cluster API along with other Redis Enterprise Software high availability
to get high performance with low latency
and let applications stay current with cluster topology changes, including add node, remove node, and node failover.

For more about working with the OSS Cluster API in Redis Enterprise Software, see [Enable OSS Cluster API]({{< relref "/operate/rs/7.4/databases/configure/oss-cluster-api" >}}). 

To learn how to enable OSS Cluster API in Redis Cloud, see [Clustering Redis databases]({{< relref "/operate/rc/databases/configuration/clustering#cluster-api" >}}).
