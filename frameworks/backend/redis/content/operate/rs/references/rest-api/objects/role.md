---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/role.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Role object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a role
linkTitle: role
weight: $weight
---

An API object that represents a role.

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | integer | Role's unique ID |
| account_id | integer | SM account ID |
| action_uid | string | Action UID. If it exists, progress can be tracked by the GET /actions/{uid} API (read-only) |
| management | 'admin'<br />'db_member'<br />'db_viewer'<br />'cluster_member'<br />'cluster_viewer'<br />'user_manager'<br />'none' | [Management role]({{< relref "/operate/rs/references/rest-api/permissions#roles" >}}) |
| name | string | Role's name |
