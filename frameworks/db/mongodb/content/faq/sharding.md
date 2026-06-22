---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/faq/sharding.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:orphan:

==========================

# FAQ: Sharding with MongoDB

This document answers common questions about `/sharding`. See also the `/sharding` section in the manual, which provides an `overview of sharding <sharding-background>`, including details on:

- :ref:`Shard Keys and Considerations for Shard Key Selection
<sharding-shard-key>`

- `Query Routing <sharding-read-operations>`
- `sharding-availability`
- `/core/sharding-data-partitioning` and
`Chunk Migration Process <sharding-balancing>`

- `/tutorial/troubleshoot-sharded-clusters`
## Is sharding appropriate for a new deployment?

Sometimes. However, if your data set fits on a single server, you should begin with an unsharded deployment as sharding while your data set is small provides little advantage .

## Can I select a different shard key after sharding a collection?

Your options for changing a shard key depend on the version of MongoDB that you are running:

- Starting in MongoDB 5.0, you can :ref:`reshard a collection
<sharding-resharding>` by changing a document's shard key.

- You can `refine a shard key <shard-key-refine>` by adding a suffix field
or fields to the existing shard key.

> **Seealso:** `/core/sharding-shard-key`

## Why are my documents not distributed across the shards?

The balancer starts distributing data across the shards once the distribution of chunks has reached certain thresholds. See `sharding-migration-thresholds`.

In addition, MongoDB cannot move a chunk if the number of documents in the chunk exceeds a certain number. See `migration-chunk-size-limit` and `jumbo-chunk`.

## How does `mongos` detect changes in the sharded cluster configuration?

:binary:`~bin.mongos` instances maintain a cache of the `config database` that holds the metadata for the `sharded cluster`.

:binary:`~bin.mongos` updates its cache lazily by issuing a request to a shard and discovering that its metadata is out of date. To force the :binary:`~bin.mongos` to reload its cache, you can run the :dbcommand:`flushRouterConfig` command against each :binary:`~bin.mongos` directly.

## How does `mongos` use connections?

Each :binary:`~bin.mongos` instance maintains a pool of connections to the members of the sharded cluster. Client requests use these connections one at a time; i.e. requests are not multiplexed or pipelined.

When client requests complete, the :binary:`~bin.mongos` returns the connection to the pool. These pools do not shrink when the number of clients decreases. This can lead to an unused :binary:`~bin.mongos` with a large number of open connections. If the :binary:`~bin.mongos` is no longer in use, it is safe to restart the process to close existing connections.

To return aggregated statistics related to all of the outgoing connection pools used by the :binary:`~bin.mongos`, connect :binary:`~bin.mongosh` to the :binary:`~bin.mongos`, and run the :dbcommand:`connPoolStats` command:

```bash
db.adminCommand("connPoolStats");
```

See the `System Resource Utilization <system-resource-utilization>` section of the `/reference/ulimit` document.
