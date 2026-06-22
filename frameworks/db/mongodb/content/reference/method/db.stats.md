---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.stats.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# db.stats() (mongosh method)

## Description

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Parameters

The :method:`db.stats()` method has the following optional parameters:

## Output

The :method:`db.stats()` method returns a `document` with statistics about the database system's state. A complete listing, including `freeStorage <db.stats-freeStorage>` details, resembles the following:

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

For an explanation of the output, see `dbstats-output`.

## Behavior

### Accuracy after Unexpected Shutdown

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

## Examples

### Scale Output Values

To return values in kilobytes, set the `scale <db.stats-scale>` to `1024`:

```javascript
db.stats(1024)
```

> **Note:** The scale factor rounds values to whole numbers.

### Return a Single Value

To return a single value, such as `dbStats.indexSize`, append the field name to `db.stats()`.

```javascript
db.stats().indexSize
db.stats(1024).indexSize
```

The output shows the difference between the original and scaled values.

```javascript
118784
116
```

### Return Information on Free Space Allocated to Collections

To return information on free space allocated to collections, pass the `freeStorage <dbStats-freeStorage>` parameter to `db.stats()`.

The following example returns the `dbStats.indexFreeStorageSize` in kilobytes:

```
db.stats( { freeStorage: 1, scale: 1024 } ).indexFreeStorageSize
```
