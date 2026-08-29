---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/cluster/logrotate_settings.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.407317Z"
---
# Logrotate_Settings

---
Title: Logrotate settings object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the logrotate_settings object used with Redis Enterprise Software REST API calls.
linkTitle: logrotate_settings
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/cluster/logrotate_settings/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| maxage | integer (default: 7) | Remove rotated logs older than the specified number of days |
| maxsize | string (default: 200M) | The log will rotate after it reaches the specified size |
| rotate | integer (default: 10) | Determines how many times the log will be rotated. If set to 0, old versions are removed rather than rotated. |