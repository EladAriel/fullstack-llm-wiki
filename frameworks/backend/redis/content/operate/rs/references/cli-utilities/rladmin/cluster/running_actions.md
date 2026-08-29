---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/cli-utilities/rladmin/cluster/running_actions.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.572831Z"
---
# Running_Actions

---
Title: rladmin cluster running_actions
alwaysopen: false
categories:
- docs
- operate
- rs
description: Lists all active tasks.
headerRange: '[1-2]'
linkTitle: running_actions
tags:
- configured
toc: 'true'
weight: $weight
---

Lists all active tasks running on the cluster.

```sh
rladmin cluster running_actions
```

### Parameters

None

### Returns

Returns details about any active tasks running on the cluster. 

### Example

```sh
$ rladmin cluster running_actions
Got 1 tasks:
1) Task: maintenance_on (ce391d81-8d51-4ce2-8f63-729c7ac2589e) Node: 1 Status: running
```