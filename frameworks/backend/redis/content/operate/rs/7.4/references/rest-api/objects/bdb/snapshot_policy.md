---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/bdb/snapshot_policy.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Snapshot policy object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the snapshot_policy object used with Redis Enterprise Software
  REST API calls.
linkTitle: snapshot_policy
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/bdb/snapshot_policy/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| secs   | integer | Interval in seconds between snapshots |
| writes | integer | Number of write changes required to trigger a snapshot |
