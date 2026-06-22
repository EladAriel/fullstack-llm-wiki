---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/bdb/status.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: BDB status field
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the bdb status field used with Redis Software REST
  API calls.
linkTitle: status
weight: $weight
---

The BDB status field is a read-only field that represents the database status.

Possible status values:

| Status | Description | Possible next status |
|--------|-------------|----------------------|
| 'active' | Database is active and no special action is in progress | 'active-change-pending' <br />'import-pending' <br />'delete-pending' |
| 'active-change-pending' | |'active' |
| 'creation-failed' | Initial database creation failed | |
| 'delete-pending' | Database deletion is in progress | |
| 'import-pending' | Dataset import is in progress | 'active' |
| 'pending' | Temporary status during database creation | 'active'<br />'creation-failed' |
| 'recovery' | Not currently relevant (intended for future use) | |

{{< image filename="/images/rs/rest-api-bdb-status.png#no-click" alt="BDB status" >}}
