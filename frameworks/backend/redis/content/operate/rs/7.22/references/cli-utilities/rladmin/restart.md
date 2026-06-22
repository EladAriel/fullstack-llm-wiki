---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/rladmin/restart.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin restart
alwaysopen: false
categories:
- docs
- operate
- rs
description: Restarts Redis Enterprise Software processes for a specific database.
headerRange: '[1-2]'
linkTitle: restart
toc: 'true'
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/rladmin/restart/'
---

Schedules a restart of the Redis Enterprise Software processes on primary and replica instances of a specific database.

``` sh
rladmin restart db { db:<id> | <name> }
        [preserve_roles]
        [discard_data]
        [force_discard]
```

### Parameters

| Parameter      | Type/Value                     | Description                                                           |
|----------------|--------------------------------|-----------------------------------------------------------------------|
| db             | db:\<id\><br /> name           | Restarts Redis Enterprise Software processes for the specified database                |
| discard_data   |                                | Allows discarding data if there is no persistence or replication      |
| force_discard  |                                | Forcibly discards data even if there is persistence or replication    |
| preserve_roles |                                | Performs an additional failover to maintain shard roles               |

### Returns

Returns `Done` if the restart completed successfully. Otherwise, it returns an error.

### Example

``` sh
$ rladmin restart db db:5 preserve_roles
Monitoring 1db07491-35da-4bb6-9bc1-56949f4c312a
active - SMUpgradeBDB init
active - SMUpgradeBDB stop_forwarding
active - SMUpgradeBDB stop_active_expire
active - SMUpgradeBDB check_slave
oactive - SMUpgradeBDB stop_active_expire
active - SMUpgradeBDB second_failover
completed - SMUpgradeBDB
Done
```
