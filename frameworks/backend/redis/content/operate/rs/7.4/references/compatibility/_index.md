---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/compatibility/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.743171Z"
---
# _Index

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
url: '/operate/rs/7.4/references/compatibility/'
---
Both Redis Enterprise Software and [Redis Cloud]({{< relref "/operate/rc" >}}) are compatible with Redis Open Source. 

{{< embed-md "rc-rs-oss-compatibility.md"  >}}

## RESP compatibility

Redis Enterprise Software and Redis Cloud support RESP2 and RESP3. See [RESP compatibility with Redis Enterprise]({{< relref "/operate/rs/7.4/references/compatibility/resp" >}}) for more information.

## Compatibility with open source Redis Cluster API

Redis Enterprise supports [Redis OSS Cluster API]({{< relref "/operate/rs/7.4/clusters/optimize/oss-cluster-api" >}}) if it is enabled for a database. For more information, see [Enable OSS Cluster API]({{< relref "/operate/rs/7.4/databases/configure/oss-cluster-api" >}}).
