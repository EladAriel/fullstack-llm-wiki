---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/job_scheduler/node_checks_job_settings.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Node checks job settings object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the node_checks_job_settings object used with Redis Software REST API calls.
linkTitle: node_checks_job_settings
weight: $weight
---

| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the node checks schedule |
| enabled | boolean (default: true) | Indicates whether this job is enabled |
