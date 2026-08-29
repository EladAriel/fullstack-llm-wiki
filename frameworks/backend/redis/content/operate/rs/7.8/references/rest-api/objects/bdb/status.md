---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/bdb/status.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.511044Z"
---
# Status

---
Title: BDB status field
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the bdb status field used with Redis Enterprise Software REST
  API calls.
linkTitle: status
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/bdb/status/'
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
