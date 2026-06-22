---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/cli-utilities/rladmin/cluster/stats_archiver.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin cluster stats_archiver
alwaysopen: false
categories:
- docs
- operate
- rs
description: Enables/deactivates the stats archiver.
headerRange: '[1-2]'
linkTitle: stats_archiver
tags:
- configured
toc: 'true'
weight: $weight
---

Enables or deactivates the stats archiver, which logs statistics in CSV (comma-separated values) format.

```sh
rladmin cluster stats_archiver { enabled | disabled }
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| enabled | Turn on the stats archiver |
| disabled | Turn off the stats archiver |

### Returns

Returns the updated status of the stats archiver. 

### Example

```sh
$ rladmin cluster stats_archiver enabled 
Status: enabled
```