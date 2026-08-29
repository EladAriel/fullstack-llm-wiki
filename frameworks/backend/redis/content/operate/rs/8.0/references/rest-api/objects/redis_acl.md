---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/redis_acl.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.671451Z"
---
# Redis_Acl

---
Title: Redis ACL object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a Redis access control list (ACL)
linkTitle: redis_acl
weight: $weight
url: '/operate/rs/8.0/references/rest-api/objects/redis_acl/'
---

An API object that represents a Redis [access control list (ACL)]({{< relref "/operate/rs/8.0/security/access-control/create-db-roles" >}})

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | integer | Object's unique ID |
| account_id | integer | SM account ID |
| acl | string | Redis ACL's string |
| action_uid | string | Action UID. If it exists, progress can be tracked by the `GET`&nbsp;`/actions/{uid}` API (read-only) |
| name | string | Redis ACL's name |
| min_version | string | Minimum database version that supports this ACL. Read only |
| max_version | string | Maximum database version that supports this ACL. Read only |

