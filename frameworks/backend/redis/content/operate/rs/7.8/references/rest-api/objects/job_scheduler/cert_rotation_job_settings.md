---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/job_scheduler/cert_rotation_job_settings.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.505758Z"
---
# Cert_Rotation_Job_Settings

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
url: '/operate/rs/7.8/references/rest-api/objects/job_scheduler/cert_rotation_job_settings/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| cron_expression              | string | [CRON expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that defines the certificate rotation schedule |
| enabled | boolean (default: true) | Indicates whether this job is enabled |
| expiry_days_before_rotation  | integer, (range:&nbsp;1-90) (default:&nbsp;60) | Number of days before a certificate expires before rotation |
