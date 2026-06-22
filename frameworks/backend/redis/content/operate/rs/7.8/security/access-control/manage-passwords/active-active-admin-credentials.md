---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/security/access-control/manage-passwords/active-active-admin-credentials.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Update admin credentials for Active-Active databases
alwaysopen: false
categories:
- docs
- operate
- rs
description: Update admin credentials for Active-Active databases.
linkTitle: Update Active-Active admin credentials
weight: 90
url: '/operate/rs/7.8/security/access-control/manage-passwords/active-active-admin-credentials/'
---

Active-Active databases use administrator credentials to manage operations.

To update the administrator user password on a cluster with Active-Active databases:

1. From the user management page, update the administrator user password on the clusters you want to update.

1. For each participating cluster _and_ each Active-Active database, update the admin user credentials to match the changes in step 1. 

{{<warning>}}
Do not perform any management operations on the databases until these steps are complete.
{{</warning>}}
