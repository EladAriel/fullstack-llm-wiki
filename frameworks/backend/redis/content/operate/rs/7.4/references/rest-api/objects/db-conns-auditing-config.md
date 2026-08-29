---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/db-conns-auditing-config.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.755220Z"
---
# Db Conns Auditing Config

---
Title: Database connection auditing configuration object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object for database connection auditing settings
linkTitle: db_conns_auditing_config
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/db-conns-auditing-config/'
---

Database connection auditing configuration

| Name | Type/Value | Description |
|------|------------|-------------|
| audit_address | string | TCP/IP address where one can listen for notifications. |
| audit_port | integer | Port where one can listen for notifications. |
| audit_protocol | `TCP`<br />`local` | Protocol used to process notifications. For production systems, `TCP` is the only valid value. |
| audit_reconnect_interval | integer | Interval (in seconds) between attempts to reconnect to the listener. Default is 1 second. |
| audit_reconnect_max_attempts | integer | Maximum number of attempts to reconnect. Default is 0 (infinite). |
