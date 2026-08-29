---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/job_scheduler/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.780713Z"
---
# _Index

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
url: '/operate/rs/7.4/references/rest-api/objects/job_scheduler/'
---

An API object that represents the job scheduler settings in the cluster.

| Name | Type/Value | Description |
|------|------------|-------------|
| backup_job_settings | [backup_job_settings]({{< relref "/operate/rs/7.4/references/rest-api/objects/job_scheduler/backup_job_settings" >}}) object | Backup job settings |
| cert_rotation_job_settings | [cert_rotation_job_settings]({{< relref "/operate/rs/7.4/references/rest-api/objects/job_scheduler/cert_rotation_job_settings" >}}) object | Job settings for internal certificate rotation |
| log_rotation_job_settings | [log_rotation_job_settings]({{< relref "/operate/rs/7.4/references/rest-api/objects/job_scheduler/log_rotation_job_settings" >}}) object | Log rotation job settings |
| node_checks_job_settings | [node_checks_job_settings]({{< relref "/operate/rs/7.4/references/rest-api/objects/job_scheduler/node_checks_job_settings" >}}) object | Node checks job settings |
| redis_cleanup_job_settings | [redis_cleanup_job_settings]({{< relref "/operate/rs/7.4/references/rest-api/objects/job_scheduler/redis_cleanup_job_settings" >}}) object | Redis cleanup job settings (deprecated as of Redis Enterprise v6.4.2, replaced with persistence_cleanup_scan_interval) |
| rotate_ccs_job_settings | [rotate_ccs_job_settings]({{< relref "/operate/rs/7.4/references/rest-api/objects/job_scheduler/rotate_ccs_job_settings" >}}) object | Rotate CCS job settings |
