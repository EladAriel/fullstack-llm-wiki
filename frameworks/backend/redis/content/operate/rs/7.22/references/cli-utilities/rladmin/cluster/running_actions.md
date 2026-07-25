---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/rladmin/cluster/running_actions.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
url: '/operate/rs/7.22/references/cli-utilities/rladmin/cluster/running_actions/'
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