---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/cli-utilities/rladmin/placement.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin placement
alwaysopen: false
categories:
- docs
- operate
- rs
description: Configures the shard placement policy for a database.
headerRange: '[1-2]'
linkTitle: placement
toc: 'true'
weight: $weight
url: '/operate/rs/7.4/references/cli-utilities/rladmin/placement/'
---

Configures the shard placement policy for a specified database.

``` sh
rladmin placement
        db { db:<id> | <name> }
        { dense | sparse }
```

### Parameters

| Parameter | Type/Value                     | Description                                                                                   |
|-----------|--------------------------------|-----------------------------------------------------------------------------------------------|
| db        | db:\<id\><br /> name           | Configures shard placement for the specified database                                         |
| dense     |                                | Places new shards on the same node as long as it has resources                                |
| sparse    |                                | Places new shards on the maximum number of available nodes within the cluster                 |

### Returns

Returns the new shard placement policy if the policy was changed successfully. Otherwise, it returns an error.

Use [`rladmin status databases`]({{< relref "/operate/rs/7.4/references/cli-utilities/rladmin/status#status-databases" >}}) to verify that the failover completed.

### Example

``` sh
$ rladmin status databases
DATABASES:
DB:ID  NAME       TYPE   STATUS   SHARDS   PLACEMENT    REPLICATION    PERSISTENCE    ENDPOINT                                
db:5   tr01       redis  active   1        dense        enabled        aof            redis-12000.cluster.local:12000         
$ rladmin placement db db:5 sparse
Shards placement policy is now sparse
$ rladmin status databases
DATABASES:
DB:ID  NAME       TYPE   STATUS   SHARDS   PLACEMENT    REPLICATION    PERSISTENCE    ENDPOINT                                
db:5   tr01       redis  active   1        sparse       enabled        aof            redis-12000.cluster.local:12000         
```
