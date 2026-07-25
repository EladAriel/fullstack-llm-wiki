---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/cli-utilities/rladmin/cluster/master.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: rladmin cluster master
alwaysopen: false
categories:
- docs
- operate
- rs
description: Identifies or changes the cluster's master node.
headerRange: '[1-2]'
linkTitle: master
tags:
- configured
toc: 'true'
weight: $weight
---

Identifies the cluster's master node. Use `set` to change the cluster's master to a different node.

```sh
cluster master [ set <node_id> ]
```

### Parameters

| Parameter | Type/Value | Description |
|-----------|------------|-------------|
| node_id | integer | Unique node ID |

### Returns

Returns the ID of the cluster's master node. Otherwise, it returns an error message.

### Example

Identify the cluster's master node:

```sh
$ rladmin cluster master
Node 1 is the cluster master node
```

Change the cluster master to node 3:

```sh
$ rladmin cluster master set 3
Node 3 set to be the cluster master node
```
