---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dbStats.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# dbStats (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     dbStats: 1, 
     scale: <number>,
     freeStorage: 0
   } 
)
```

## Command Fields

The command takes the following fields:

In :binary:`~bin.mongosh`, the :method:`db.stats()` function provides a wrapper around :dbcommand:`dbStats`.

## Behavior

The time required to run the command depends on the total size of the database. Because the command must touch all data files, the command may take several seconds to run.

### Accuracy after Unexpected Shutdown

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

## Output

## Examples

The following examples demonstrate :dbcommand:`dbStats` usage.

### Limit Data Returned

To limit the data returned to a single field, append the field name to the :dbcommand:`dbStats` command. This example returns the `dbStats.indexSize` value:

```javascript
db.runCommand( { dbStats: 1 } ).indexSize
```

### View Free Space Allocated to Collections

To view free storage usage, set `freeStorage <dbStats-freeStorage>` to 1.

```javascript
db.runCommand( { dbStats: 1, scale: 1024, freeStorage: 1 } )
```

Example output:

```javascript
{
  db: 'test',
  collections: 2,
  views: 0,
  objects: 1689,
  avgObjSize: 52.56542332741267,
  dataSize: 86.7021484375,
  storageSize: 100,
  freeStorageSize: 32,
  indexes: 2,
  indexSize: 116,
  indexFreeStorageSize: 36,
  totalSize: 216,
  totalFreeStorageSize: 68,
  scaleFactor: 1024,
  fsUsedSize: 60155820,
  fsTotalSize: 61255492,
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1646085664, i: 1 }),
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: Long("0")
    }
  },
  operationTime: Timestamp({ t: 1646085664, i: 1 })
}
```

The `freeStorage <dbStats-freeStorage>` field enables the collection and display of the highlighted metrics.

The `scale <dbStats-scale>` field sets the displayed values to kilobytes.
