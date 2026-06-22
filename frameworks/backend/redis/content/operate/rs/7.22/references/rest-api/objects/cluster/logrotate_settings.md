---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/cluster/logrotate_settings.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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