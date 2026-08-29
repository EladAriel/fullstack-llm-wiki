---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/bootstrap/cluster_identity.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.512989Z"
---
# Cluster_Identity

---
Title: Cluster identity object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the cluster_identity object used with Redis Enterprise Software
  REST API calls.
linkTitle: cluster_identity
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/bootstrap/cluster_identity/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| name          | string                | Fully qualified cluster name. Limited to 64 characters and must comply with the IETF's RFC 952 standard and section 2.1 of the RFC 1123 standard. |
| nodes         | array of strings       | Array of IP addresses of existing cluster nodes |
| wait_command  | boolean (default:&nbsp;true) | Supports Redis wait command |
