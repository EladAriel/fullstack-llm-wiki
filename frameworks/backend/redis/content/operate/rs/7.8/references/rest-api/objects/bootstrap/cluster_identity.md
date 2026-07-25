---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/bootstrap/cluster_identity.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
