---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/movePrimary.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# movePrimary (database command)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

.. include:: /includes/extracts/mongos-operations-wc-move-primary.rst

### Unsharded Collections

Only run :dbcommand:`movePrimary` after you move unsharded collections using :method:`sh.moveCollection`. Starting in MongoDB 8.0, unmoved, unsharded collections are not available during the `movePrimary` process.

### {+fts+} Indexes

If the database being moved contains unsharded collections that use {+fts+}, their search indexes become unavailable after `movePrimary` completes. Because `movePrimary` updates the :abbr:`UUID (Universally unique identifier)` for unsharded collections that you move, you must manually rebuild the {+fts+} indexes on those collections.

### Maintenance Windows

:dbcommand:`movePrimary` may require a significant time to complete depending on the size of the database and factors such as network health or machine resources. During migration, attempts to write or perform any DDL operations to the unsharded collections on the database being moved fail with the error: `"movePrimary is in progress"`.

Consider scheduling a maintenance window during which applications stop all reads and writes to the cluster. Issuing :dbcommand:`movePrimary` during planned downtime mitigates the risk of encountering undefined behavior due to interleaving reads or writes to the unsharded collections in the database.

### Namespace Conflicts

:dbcommand:`movePrimary` fails if the destination shard contains a conflicting collection namespace. For example:

1. An administrator issues `movePrimary` to change the
primary shard for the `hr` database.

#. A user or application issues a write operation against an unsharded collection in `hr` while `movePrimary` is moving that collection. The write operation creates the collection in the original primary shard.

#. An administrator later issues `movePrimary` to restore the original primary shard for the `hr` database.

#. `movePrimary` fails due to the conflicting namespace left behind from the interleaving write operation.

### Rebuilding Indexes

As part of the `movePrimary` operation, the destination shard must rebuild indexes on the migrated collections after becoming the primary shard. This may require a significant amount of time depending on the number of indexes per collection and the amount of data to index.

See `/core/index-creation` for more information on the index build process.

### Change Streams

.. include:: /includes/movePrimary-change-streams.rst

In earlier MongoDB versions, `movePrimary` invalidates collection change streams and the change streams cannot read events from the collections.

In all MongoDB versions, `movePrimary` updates the :abbr:`UUID (Universally unique identifier)` for moved unsharded collections.

## Additional Information

See `/tutorial/remove-shards-from-cluster` for a complete procedure.
