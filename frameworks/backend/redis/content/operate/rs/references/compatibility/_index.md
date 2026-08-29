---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/compatibility/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.565263Z"
---
# _Index

---
Title: Redis Software compatibility with Redis Open Source
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
description: Redis Software compatibility with Redis Open Source.
hideListLinks: true
linkTitle: Redis Open Source compatibility
weight: $weight
tocEmbedHeaders: true
---
Both Redis Software and [Redis Cloud]({{< relref "/operate/rc" >}}) are compatible with Redis Open Source. 

If you're planning a move from a self-managed Redis Open Source deployment to Redis Software, see [Move from Redis Open Source to Redis Software]({{< relref "/operate/rs/installing-upgrading/move-from-open-source" >}}) for how configuration and deployment differ.

{{< embed-md "rc-rs-oss-compatibility.md"  >}}

## RESP compatibility

Redis Software and Redis Cloud support RESP2 and RESP3. See [RESP compatibility with Redis Software]({{< relref "/operate/rs/references/compatibility/resp" >}}) for more information.

## Client-side caching compatibility

Redis Software and Redis Cloud support [client-side caching]({{<relref "/develop/clients/client-side-caching">}}) for databases with Redis versions 7.4 or later. See [Client-side caching compatibility with Redis Software and Redis Cloud]({{<relref "/operate/rs/references/compatibility/client-side-caching">}}) for more information about compatibility and configuration options.

## Compatibility with open source Redis Cluster API

Redis Software supports [Redis OSS Cluster API]({{< relref "/operate/rs/clusters/optimize/oss-cluster-api" >}}) if it is enabled for a database. For more information, see [Enable OSS Cluster API]({{< relref "/operate/rs/databases/configure/oss-cluster-api" >}}).
