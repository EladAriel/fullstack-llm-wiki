---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/databases/active-active/syncer.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Syncer process
alwaysopen: false
categories:
- docs
- operate
- rs
description: Detailed information about the syncer process and its role in distributed
  databases.
linktitle: Syncer process
weight: 90
url: '/operate/rs/7.8/databases/active-active/syncer/'
---

## Syncer process

Each node in a cluster containing an instance of an Active-Active database hosts a process called the syncer.
The syncer process:

1. Connects to the proxy on another participating cluster
1. Reads data from that database instance
1. Writes the data to the local cluster's primary(master) shard

Some replication capabilities are also included in [Redis Open Source]({{< relref "/operate/oss_and_stack/management/replication" >}}).

The primary (also known as master) shard at the top of the primary-replica tree creates a replication ID.
This replication ID is identical for all replicas in that tree.
When a new primary is appointed, the replication ID changes, but a partial sync from the previous ID is still possible.


In a partial sync, the backlog of operations since the offset are transferred as raw operations.
In a full sync, the data from the primary is transferred to the replica as an RDB file which is followed by a partial sync. 

Partial synchronization requires a backlog large enough to store the data operations until connection is restored. See [replication backlog]({{< relref "/operate/rs/7.8/databases/active-active/manage#replication-backlog" >}}) for more info on changing the replication backlog size.

### Syncer in Active-Active replication

In the case of an Active-Active database:

- Multiple past replication IDs and offsets are stored to allow for multiple syncs 
- The [Active-Active replication backlog]({{< relref "/operate/rs/7.8/databases/active-active/manage#replication-backlog" >}}) is also sent to the replica during a full sync. 

{{< warning >}}
Full sync triggers heavy data transfers between geo-replicated instances of an Active-Active database. 
{{< /warning >}}

An Active-Active database uses partial synchronization in the following situations:

- Failover of primary shard to replica shard
- Restart or crash of replica shard that requires sync from primary
- Migrate replica shard to another node
- Migrate primary shard to another node as a replica using failover and replica migration
- Migrate primary shard and preserve roles using failover, replica migration, and second failover to return shard to primary

{{< note >}}
Synchronization of data from the primary shard to the replica shard is always a full synchronization.
{{< /note >}}
