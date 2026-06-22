---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/job_scheduler/bdb_usage_report_job_settings.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
