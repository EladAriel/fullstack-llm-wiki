---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/bdbs/modules/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.404614Z"
---
# _Index

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
url: '/operate/rs/7.22/references/rest-api/requests/bdbs/modules/'
---

## Configure module
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{< relref "/operate/rs/7.22/references/rest-api/requests/bdbs/modules/config#post-bdb-modules-config" >}}) | `/v1/bdbs/{uid}/modules/config` | Configure module |

## Upgrade module
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{< relref "/operate/rs/7.22/references/rest-api/requests/bdbs/modules/upgrade#post-bdb-modules-upgrade" >}}) | `/v1/bdbs/{uid}/modules/upgrade` | Upgrade module |