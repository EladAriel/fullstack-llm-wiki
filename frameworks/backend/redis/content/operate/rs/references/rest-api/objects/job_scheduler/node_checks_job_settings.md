---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/job_scheduler/node_checks_job_settings.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
