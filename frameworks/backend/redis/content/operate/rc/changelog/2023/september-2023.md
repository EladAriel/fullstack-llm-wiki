---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/2023/september-2023.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.311930Z"
---
# September 2023

---
Title: Redis Cloud changelog (September 2023)
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  September 2023.
highlights: RESP protocol selection
linktitle: September 2023
tags:
- changelog
weight: 78
aliases:
  - /operate/rc/changelog/september-2023
---

## New features

### RESP protocol selection

For all databases using Redis 7.2, you can now choose between the RESP2 and RESP3 protocols when you [create a database]({{< relref "/operate/rc/databases/create-database" >}}). For more information about the different RESP versions, see the [Redis serialization protocol specification]({{< relref "/develop/reference/protocol-spec" >}}#resp-versions).

### Opt-in to Redis 7.2

{{< embed-md "rc-opt-in-to-72.md" >}}

