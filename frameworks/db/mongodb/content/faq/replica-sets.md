---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/faq/replica-sets.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:orphan:

=================================

# FAQ: Replication and Replica Sets

This document answers common questions about replication in MongoDB. See also the `replication` section in the manual, which provides an overview of replication including details on:

- `replica-set-members`
- `replica-set-architecture`
- `replica-set-elections`
## What kind of replication does MongoDB support?

MongoDB supports `Replica sets <replication>`, which can have up to 50 nodes.

## Does replication work over the Internet and WAN connections?

Yes.

For example, a deployment may maintain a `primary` and `secondary` in an East-coast data center along with a `secondary` member for disaster recovery in a West-coast data center.

> **Seealso:** `server-replica-set-deploy-geo`

## Can MongoDB replicate over a "noisy" connection?

Yes, but not without connection failures and the obvious latency.

Members of the set will attempt to reconnect to the other members of the set in response to networking flaps. This does not require administrator intervention. However, if the network connections among the nodes in the replica set are very slow, it might not be possible for the members of the node to keep up with the replication.

> **Seealso:** `replica-set-elections`

## Why use journaling if replication already provides data redundancy?

`Journaling <journal>` facilitates faster crash recovery.

Journaling is particularly useful for protection against power failures, especially if your replica set resides in a single data center or power circuit.

When a `replica set` runs with journaling, you can safely restart :binary:`~bin.mongod` instances without additional intervention.

> **Note:** Journaling requires some resource overhead for write
operations. Journaling has no effect on read performance, however.
Journaling is enabled by default on all 64-bit
builds of MongoDB v2.0 and greater.

## What information do arbiters exchange with the rest of the replica set?

Arbiters never receive the contents of a collection but do exchange the following data with the rest of the replica set:

- Credentials used to authenticate the arbiter with the replica set.
These exchanges are encrypted.

- Replica set configuration data and voting data. This information is
not encrypted. Only credential exchanges are encrypted.

If your MongoDB deployment uses TLS/SSL, then all communications between arbiters and the other members of the replica set are secure.

See the documentation for `configure-mongod-mongos-for-tls-ssl` for more information. As with all MongoDB components, run arbiters on secure networks.

## Is it normal for replica set members to use different amounts of disk space?

Yes.

Factors including: different oplog sizes, different levels of storage fragmentation, and MongoDB's data file pre-allocation can lead to some variation in storage utilization between nodes. Storage use disparities will be most pronounced when you add members at different times.

## Can I rename a replica set?

Yes, unsharded replica sets can be renamed. This procedure requires downtime.

To learn how to rename your replica set, see `rename-a-replica-set`.

Before renaming a replica set, perform a full `backup of your MongoDB deployment <backup-methods>`.
