---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/requests/bdbs/modules/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
url: '/operate/rs/7.8/references/rest-api/requests/bdbs/modules/'
---

## Configure module
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{< relref "/operate/rs/7.8/references/rest-api/requests/bdbs/modules/config#post-bdb-modules-config" >}}) | `/v1/bdbs/{uid}/modules/config` | Configure module |

## Upgrade module
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{< relref "/operate/rs/7.8/references/rest-api/requests/bdbs/modules/upgrade#post-bdb-modules-upgrade" >}}) | `/v1/bdbs/{uid}/modules/upgrade` | Upgrade module |
