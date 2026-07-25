---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/requests/bdbs/modules/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Database modules requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Redis module requests
headerRange: '[1-2]'
hideListLinks: true
linkTitle: modules
weight: $weight
url: '/operate/rs/8.0/references/rest-api/requests/bdbs/modules/'
---

## Configure module
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{< relref "/operate/rs/8.0/references/rest-api/requests/bdbs/modules/config#post-bdb-modules-config" >}}) | `/v1/bdbs/{uid}/modules/config` | Configure module |

## Upgrade module
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{< relref "/operate/rs/8.0/references/rest-api/requests/bdbs/modules/upgrade#post-bdb-modules-upgrade" >}}) | `/v1/bdbs/{uid}/modules/upgrade` | Upgrade module |