---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/job_scheduler/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Job scheduler object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object for job scheduler settings
hideListLinks: true
linkTitle: job_scheduler
weight: $weight
---

An API object that represents the job scheduler settings in the cluster.

| Name | Type/Value | Description |
|------|------------|-------------|
| backup_job_settings | [backup_job_settings]({{< relref "/operate/rs/references/rest-api/objects/job_scheduler/backup_job_settings" >}}) object | Backup job settings |
| <span class="break-all">bdb_usage_report_job_settings</span> | <span class="break-all">[bdb_usage_report_job_settings]({{< relref "/operate/rs/references/rest-api/objects/job_scheduler/bdb_usage_report_job_settings" >}})</span> object | Job settings for database usage reports |
| <span class="break-all">cert_rotation_job_settings</span> | <span class="break-all">[cert_rotation_job_settings]({{< relref "/operate/rs/references/rest-api/objects/job_scheduler/cert_rotation_job_settings" >}})</span> object | Job settings for internal certificate rotation |
| <span class="break-all">log_rotation_job_settings</span> | <span class="break-all">[log_rotation_job_settings]({{< relref "/operate/rs/references/rest-api/objects/job_scheduler/log_rotation_job_settings" >}})</span> object | Log rotation job settings |
| <span class="break-all">node_checks_job_settings</span> | <span class="break-all">[node_checks_job_settings]({{< relref "/operate/rs/references/rest-api/objects/job_scheduler/node_checks_job_settings" >}})</span> object | Node checks job settings |
| <span class="break-all">redis_cleanup_job_settings</span> | <span class="break-all">[redis_cleanup_job_settings]({{< relref "/operate/rs/references/rest-api/objects/job_scheduler/redis_cleanup_job_settings" >}})</span> object | Redis cleanup job settings (deprecated as of Redis Software v6.4.2, replaced with persistence_cleanup_scan_interval) |
| rotate_ccs_job_settings | [rotate_ccs_job_settings]({{< relref "/operate/rs/references/rest-api/objects/job_scheduler/rotate_ccs_job_settings" >}}) object | Rotate CCS job settings |
