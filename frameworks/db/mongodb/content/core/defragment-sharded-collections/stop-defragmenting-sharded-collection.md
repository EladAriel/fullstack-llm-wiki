---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/defragment-sharded-collections/stop-defragmenting-sharded-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
