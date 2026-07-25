---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/role.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
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
| resources | array of objects | Optional list of resource scopes that limit a `db_member` or `db_viewer` management role to specific databases. Each scope has a `type` (currently only `db`) and a `uids` array of database IDs the role applies to. If omitted or empty, the role applies to all databases. Example: `[{"type": "db", "uids": ["1", "2"]}]` |
