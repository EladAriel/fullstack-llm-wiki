---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/moveChunk.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# moveChunk (database command)

## Definition

> **Seealso:** - :dbcommand:`split`
- :method:`sh.moveChunk()`
- :method:`sh.splitAt()`
- :method:`sh.splitFind()`

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

Only use the :dbcommand:`moveChunk` in special circumstances such as preparing your `sharded cluster` for an initial ingestion of data, or a large bulk import operation.  In most cases allow the balancer to create and balance chunks in sharded clusters. See `/tutorial/create-chunks-in-sharded-cluster` for more information.

## Behavior

### Indexes

:dbcommand:`moveChunk` requires that all indexes exist on the target (i.e. `to` ) shard before migration and returns an error if a required index does not exist.

### Meta Data Error

:dbcommand:`moveChunk` returns the following error message if another metadata operation is in progress on the `config.chunks` collection:

```none
errmsg: "The collection's metadata lock is already taken."
```

If another process, such as a balancer process, changes meta data while :dbcommand:`moveChunk` is running, you may see this error. You may retry the :dbcommand:`moveChunk` operation without side effects.

### `maxCatchUpPercentageBeforeBlockingWrites` Server Parameter

Starting in MongoDB 5.0, you can set the :parameter:`maxCatchUpPercentageBeforeBlockingWrites` to specify the maximum allowed percentage of data not yet migrated during a :dbcommand:`moveChunk` operation when compared to the total size (in MBs) of the chunk being transferred.
