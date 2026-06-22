---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/compatibility/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Enterprise compatibility with Redis Open Source
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
description: Redis Enterprise compatibility with Redis Open Source.
hideListLinks: true
linkTitle: Redis Open Source compatibility
weight: $weight
tocEmbedHeaders: true
url: '/operate/rs/7.22/references/compatibility/'
---
Both Redis Enterprise Software and [Redis Cloud]({{< relref "/operate/rc" >}}) are compatible with Redis Open Source. 

{{< embed-md "rc-rs-oss-compatibility.md"  >}}

## RESP compatibility

Redis Enterprise Software and Redis Cloud support RESP2 and RESP3. See [RESP compatibility with Redis Enterprise]({{< relref "/operate/rs/7.22/references/compatibility/resp" >}}) for more information.

## Client-side caching compatibility

Redis Software and Redis Cloud support [client-side caching]({{<relref "/develop/clients/client-side-caching">}}) for databases with Redis versions 7.4 or later. See [Client-side caching compatibility with Redis Software and Redis Cloud]({{<relref "/operate/rs/7.22/references/compatibility/client-side-caching">}}) for more information about compatibility and configuration options.

## Compatibility with open source Redis Cluster API

Redis Enterprise supports [Redis OSS Cluster API]({{< relref "/operate/rs/7.22/clusters/optimize/oss-cluster-api" >}}) if it is enabled for a database. For more information, see [Enable OSS Cluster API]({{< relref "/operate/rs/7.22/databases/configure/oss-cluster-api" >}}).
