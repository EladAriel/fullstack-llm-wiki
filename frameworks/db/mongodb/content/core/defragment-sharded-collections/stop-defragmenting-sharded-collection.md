---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/defragment-sharded-collections/stop-defragmenting-sharded-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# Stop Defragmenting a Sharded Collection

Typically, you should use a `shard balancing window <sharding-schedule-balancing-window>` to specify when the balancer runs instead of manually starting and stopping defragmentation.

To manually stop defragmenting a sharded collection, use the :dbcommand:`configureCollectionBalancing` command with the `defragmentCollection` option set to `false`.

## About this Task

.. include:: /includes/defragment-sharded-collections-example.rst

If you stop defragmenting a collection before defragmentation is complete, the collection is in a partially defragmented state and operates as usual. To resume defragmentation, restart the process.

## Before you Begin

- Start defragmenting a sharded collection. For details, see
`start-defragmenting-sharded-collection`.

- Connect to :binary:`~bin.mongos`.
## Procedure

## Next Steps

You can start defragmentation again at any time. For details, see `start-defragmenting-sharded-collection`.

## Learn More

- :ref:`Start defragmenting a sharded collection
<start-defragmenting-sharded-collection>`

- :ref:`Monitor defragmentation of a sharded collection
<monitor-defragmentation-sharded-collection>`

.. include:: /includes/defragment-sharded-collections-learn-more.rst
