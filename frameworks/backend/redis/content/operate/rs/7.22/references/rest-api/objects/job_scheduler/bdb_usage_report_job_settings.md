---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/job_scheduler/bdb_usage_report_job_settings.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.409165Z"
---
# Bdb_Usage_Report_Job_Settings

---
Title: BDB usage report job settings object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the bdb_usage_report_job_settings object used with Redis Enterprise Software REST API calls.
linkTitle: bdb_usage_report_job_settings
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/job_scheduler/bdb_usage_report_job_settings/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the database usage report schedule |
| enabled | boolean (default: true) | Indicates whether this job is enabled |
| file_retention_days | integer, 1-1000 (default: 365) | Number of days after a file is closed before it is deleted |
