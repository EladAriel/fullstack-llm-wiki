---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/job_scheduler/rotate_ccs_job_settings.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Rotate CCS job settings object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the rotate_ccs_job_settings object used with Redis Software REST API calls.
linkTitle: rotate_ccs_job_settings
weight: $weight
url: '/operate/rs/8.0/references/rest-api/objects/job_scheduler/rotate_ccs_job_settings/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the CCS rotation schedule |
| enabled | boolean (default: true) | Indicates whether this job is enabled |
| file_suffix | string (default:&nbsp;5min) | String added to the end of the rotated RDB files |
| rotate_max_num | integer, (range:&nbsp;1-100) (default:&nbsp;24) | The maximum number of saved RDB files |
