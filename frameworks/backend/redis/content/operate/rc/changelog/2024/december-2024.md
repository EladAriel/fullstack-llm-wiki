---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/2024/december-2024.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Cloud changelog (December 2024)
aliases:
- /operate/rc/changelog/december-2024/
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  December 2024.
highlights: Logs Viewer API role
linktitle: December 2024
tags:
- changelog
weight: 38
---

## New features

### Logs Viewer role

You can now add a user with the **Logs Viewer** role in the [Access Management]({{< relref "/operate/rc/security/access-control/access-management" >}}) screen. Logs Viewers can only use the [Redis Cloud API]({{< relref "/operate/rc/api" >}}) [`GET logs/`](https://api.redislabs.com/v1/swagger-ui/index.html#/Account/getAccountSystemLogs) endpoint. 

See [Team Management roles]({{< relref "/operate/rc/security/access-control/access-management#team-management-roles" >}}) to see an overview of user roles and their permissions.

### Redis Flex preview on Redis Cloud Essentials

Redis Flex is now available in Preview on Redis Cloud Essentials.

Redis Flex databases have a tiered solid state drive (SSD) and RAM architecture. Using SSDs instead of RAM significantly reduces infrastructure costs, which means developers can build applications that require large datasets using the same Redis API.

See [Create a Redis Flex database]({{< relref "/operate/rc/databases/create-database/create-flex-database" >}}) for more info.