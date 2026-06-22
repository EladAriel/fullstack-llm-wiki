---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/manage-indexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# Manage Indexes

This page shows how to manage existing indexes. For instructions on creating indexes, refer to the specific index type pages.

## View Existing Indexes

.. include:: /includes/driver-view-existing-indexes-tabs.rst

## Remove Indexes

> **Tip:** If you drop an index that is actively used in production, your
application may incur a performance degradation. Before you drop an
index, you can evaluate the potential impact of the drop by
`hiding the index <hide-existing-index>`.
Hidden indexes are not used to support queries. If you hide an index
and observe substantial negative performance impact, consider keeping
and unhiding the index so queries can resume using it.

To learn how to remove an existing index, see `drop-an-index`.

To learn how to remove an index in |compass|, see :compass:`Manage Indexes in Compass </indexes>`.

## Modify an Index

.. include:: /includes/driver-examples/driver-example-modify-index-tabs.rst

### Minimize Performance Impact With a Temporary Index

If you drop an index that is actively used in production, your application may incur a performance degradation. To ensure queries can still use an index during modification, you can create a temporary, redundant index that contains the same fields as the modified index.

Example ```````

This example creates a new index and modifies that index to make it `unique <index-type-unique>`.

## Find Inconsistent Indexes Across Shards

A sharded collection has an inconsistent index if the collection does not have the exact same indexes (including the index options) on each shard that contains chunks for the collection. Although inconsistent indexes should not occur during normal operations, inconsistent indexes can occur, such as:

- When a user is creating an index with a `unique` key constraint and
one shard contains a chunk with duplicate documents. In such cases, the create index operation may succeed on the shards without duplicates but not on the shard with duplicates.

- When a user is creating an index across the shards in a :doc:`rolling
manner (i.e. manually building the index one by one across the shards) </tutorial/build-indexes-on-sharded-clusters>` but either fails to build the index for an associated shard or incorrectly builds an index with different specification.

The `config server <sharding-config-server>` primary, by default, checks for index inconsistencies across the shards for sharded collections, and the command :dbcommand:`serverStatus`, when run on the config server primary, returns the field :serverstatus:`shardedIndexConsistency` field to report on the number of sharded collections with index inconsistencies.

If :serverstatus:`shardedIndexConsistency` reports any index inconsistencies, you can run the :dbcommand:`checkMetadataConsistency` command with `checkIndexes: true` for your sharded collections to find the inconsistencies.

#. Run the `checkMetadataConsistency` command:

```javascript
   db.runCommand( {
      checkMetadataConsistency: 1,
      checkIndexes: true
   } )
```

#. If the collection has inconsistent indexes, the `checkMetadataConsistency` command returns details regarding the inconsistent indexes similar to the following:

.. include:: /includes/checkMetadataConsistency-check-indexes-output.rst

To resolve the inconsistency where an index is missing  from the collection on a particular shard(s), You can either:

- Issue an index build :method:`db.collection.createIndex()` from a
:binary:`~bin.mongos` instance. The operation only builds the collection's index on the shard(s) missing the index.

\-OR-

- Perform a :doc:`rolling index build
</tutorial/build-indexes-on-sharded-clusters>` for the collection on the affected shard(s).

> **Note:**      Rolling indexes may negatively impact your deployment. For
     information on when to use this index build, see
     `rolling-index-build`.

.. include:: /includes/warning-simultaneous-index-builds.rst

To resolve where the index properties differ across the shards, Drop the incorrect index from the collection on the affected shard(s) and rebuild the index. To rebuild the index, you can either:

- Issue an index build :method:`db.collection.createIndex()` from a
:binary:`~bin.mongos` instance. The operation only builds the collection's index on the shard(s) missing the index.

\-OR-

- Perform a :doc:`rolling index build
</tutorial/build-indexes-on-sharded-clusters>` for the collection on the affected shard.

> **Note:**      Rolling indexes may negatively impact your deployment. For
     information on when to use this index build, see
     `rolling-index-build`.
Alternatively, if the inconsistency is the `expireAfterSeconds` property,
you can run the :dbcommand:`collMod` command to update the number of
seconds instead of dropping and rebuilding the index.
