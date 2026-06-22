---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/mitigate-psa-performance-issues.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================================

# Mitigate Performance Issues in Self-Managed PSA Replica Sets

## Overview

In a three-member replica set with a primary-secondary-arbiter (PSA) architecture or a sharded cluster with three-member PSA shards, a data-bearing node that is down or lagged can lead to performance issues.

If one data-bearing node goes down, the other node becomes the primary. Writes with :writeconcern:`w:1 <\<number\>>` continue to succeed in this state but writes with write concern :writeconcern:`"majority"` cannot succeed and the commit point starts to lag. If your PSA replica set contains a lagged secondary and your replica set requires two nodes to majority commit a change, your commit point also lags.

With a lagged commit point, two things can affect your cluster performance:

- The storage engine keeps **all** changes that happen after the commit
point on disk to retain a `durable` history. The extra I/O from these writes tends to increase over time. This can greatly impact write performance and increase cache pressure.

- MongoDB allows the `oplog <replica-set-oplog>` to grow past its
configured size limit to avoid deleting the `majority commit point <replSetGetStatus.optimes.lastCommittedOpTime>`.

To reduce the cache pressure and increased write traffic, set :rsconf:`votes: 0 <members[n].votes>` and :rsconf:`priority: 0 <members[n].priority>` for the node that is unavailable or lagging. For write operations issued with "majority", only voting members are considered to determine the number of nodes needed to perform a majority commit. Setting the configuration of the node to :rsconf:`votes: 0 <members[n].votes>` reduces the number of nodes required to commit a write with write concern :writeconcern:`"majority"` from two to one and allows these writes to succeed.

Once the secondary is caught up, you can use the :method:`rs.reconfigForPSASet()` method to set :rsconf:`votes <members[n].votes>` back to `1`.

> **Note:** In earlier versions of MongoDB,
:setting:`~replication.enableMajorityReadConcern` and
:option:`--enableMajorityReadConcern` were configurable allowing you
to disable the default read concern :readconcern:`"majority"` which
had a similar effect.

## Procedure

To reduce the cache pressure and increased write traffic for a deployment with a three-member primary-secondary-arbiter (PSA) architecture, set `{ votes: 0, priority: 0 }` for the secondary that is unavailable or lagging:

```javascript
cfg = rs.conf();
cfg["members"][<array_index>]["votes"] = 0;
cfg["members"][<array_index>]["priority"] = 0;
rs.reconfig(cfg);
```

If you want to change the configuration of the secondary later, use the :method:`rs.reconfigForPSASet()` method.
