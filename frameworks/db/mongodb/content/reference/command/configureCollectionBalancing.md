---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/configureCollectionBalancing.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# configureCollectionBalancing (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   {
     configureCollectionBalancing: "<db>.<collection>",
     chunkSize: <num>,
     defragmentCollection: <bool>,
     enableAutoMerger: <bool>,
     enableBalancing: <bool>
   } 
)
```

### Command Fields

:dbcommand:`configureCollectionBalancing` has the following fields:

For more information, see `Data Partitioning with Chunks <sharding-data-partitioning>`.

To configure the chunk defragmentation throttling time parameter, see :parameter:`chunkDefragmentationThrottlingMS`.

To learn about defragmenting sharded collections, see `defragment-sharded-collections`.

## Behavior

### Default Behavior When chunkSize Is Not Specified

If you do not specify `chunkSize` for a collection and no custom size has been set previously, the global default `chunkSize` is used for balancing.

### Specifying chunkSize: 0

If you use :dbcommand:`configureCollectionBalancing` with `chunkSize: 0`, the per-collection `chunkSize` is reset and the global default `chunkSize` is used for balancing.

For more information on configuring default `chunkSize`, see `tutorial-modifying-range-size`.

### Default Behavior When enableAutoMerger Is Not Specified

If you do not specify `enableAutoMerger` for a collection and no custom {+auto-merge-action+} behavior has been previously set, it defaults to `true` and will be taken into account by the {+auto-merge-upper+}.

### Parameter Validation

Starting in 8.2, MongoDB validates the spelling of parameters that you pass to `configureCollectionBalancing`. If you misspell a parameter, `configureCollectionBalancing` fails to execute and returns an error.

## Examples

### Configure Chunk Size

To change the chunk size for a sharded collection, use the `chunkSize` option:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   chunkSize: 256
} )
```

Use this command to change the chunk size for the given collection.

> **Warning:** By default, MongoDB cannot move a chunk if the number of documents in
the chunk is greater than 2 times the result of dividing the
configured chunk size by the average document size.
To find the average document size, see the `avgObjSize` field in the
output of the :method:`db.collection.stats()` method.

For more information, see `Range Size <sharding-range-size>`.

### Defragment Collections

> **Warning:** We do not recommend using `defragmentCollection` to defragment sharded
collections for MongoDB 6.0.0 to 6.0.3 and MongoDB 6.1.0 to 6.1.1, as the
defragmentation process on these releases can make databases and collections
unavailable for extended periods of time.

To tell the balancer to defragment a sharded collection, use the `defragmentCollection` option:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   defragmentCollection: true
} )
```

Use this command to have the balancer defragment a sharded collection. To monitor the chunk defragmentation process, use the :dbcommand:`balancerCollectionStatus` command.

To learn more about defragmenting sharded collections, see `defragment-sharded-collections`.

### Reconfigure and Defragment Collections

To defragment a sharded collection while updating the chunk size, use the `defragmentCollection` option and the `chunkSize` option together:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   chunkSize: 512,
   defragmentCollection: true
} )
```

### Disable the {+auto-merge-upper+} on a Collection

To explicitly disable the {+auto-merge-upper+} on a collection, set the `enableAutoMerger` option to `false`:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   enableAutoMerger: false
} )
```

### Disable Balancing on a Collection

To explicitly disable the balancer on a collection, set the `enableBalancing` option to `false`:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   enableBalancing: false
} )
```
