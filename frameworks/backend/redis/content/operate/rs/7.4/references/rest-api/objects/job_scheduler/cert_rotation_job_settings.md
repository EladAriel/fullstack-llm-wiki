---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/job_scheduler/cert_rotation_job_settings.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Certificate rotation job settings object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the cert_rotation_job_settings object used with Redis Enterprise
  Software REST API calls.
linkTitle: cert_rotation_job_settings
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/job_scheduler/cert_rotation_job_settings/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression              | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the certificate rotation schedule |
| expiry_days_before_rotation  | integer, (range:&nbsp;1-90) (default:&nbsp;60) | Number of days before a certificate expires before rotation |
