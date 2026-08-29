---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/bdb/snapshot_policy.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.611797Z"
---
# Snapshot_Policy

---
Title: Snapshot policy object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the snapshot_policy object used with Redis Software
  REST API calls.
linkTitle: snapshot_policy
weight: $weight
---

| Name | Type/Value | Description |
|------|------------|-------------|
| secs   | integer | Interval in seconds between snapshots |
| writes | integer | Number of write changes required to trigger a snapshot |
