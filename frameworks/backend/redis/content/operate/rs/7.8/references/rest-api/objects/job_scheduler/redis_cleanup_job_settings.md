---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/job_scheduler/redis_cleanup_job_settings.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.504872Z"
---
# Redis_Cleanup_Job_Settings

---
Title: Redis cleanup job settings object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the redis_cleanup_job_settings object used with Redis Enterprise
  Software REST API calls.
linkTitle: redis_cleanup_job_settings
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/job_scheduler/redis_cleanup_job_settings/'
---

Deprecated and replaced with `persistence_cleanup_scan_interval`.

| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the Redis cleanup schedule |
