---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/collStats.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# collStats (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     collStats: <string>,
     scale: <int>
   }
)
```

### Command Fields

The command takes the following fields:

## Behavior

### Redaction

When using `Queryable Encryption <qe-manual-feature-qe>`, `$collStats` output redacts certain information for encrypted collections:

- The output omits `"queryExecStats"`
- The output omits `"latencyStats"`
- The output redacts `"WiredTiger"`, if present, to include only the `url` field.
### Scaled Sizes

Unless otherwise specified by the metric name (such as `"bytes currently in the cache"`), values related to size are displayed in bytes and can be overridden by `scale`.

The scale factor rounds the affected size values to whole numbers.

### Accuracy after Unexpected Shutdown

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

### In-Progress Indexes

`collStats` includes information on indexes currently being built. For details, see:

- `collStats.nindexes`
- `collStats.indexDetails`
- `collStats.indexBuilds`
- `collStats.totalIndexSize`
- `collStats.indexSizes`
### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

### Non-Existent Collections

If you run `collStats` for a non-existent collection, then depending on your database implementation, `collStats` might return `0` values in the output fields instead of returning an error.

For example:

```javascript
db.runCommand( { collStats : "nonExistentCollection" } )
```

Example output with `0` values in the fields:

```javascript
{
   ns: 'test.nonExistentCollection',
   size: 0,
   count: 0,
   ...
}
```

## Example

The following operation runs the `collStats` command on the `restaurants` collection, specifying a scale of `1024` bytes:

```javascript
db.runCommand( { collStats : "restaurants", scale: 1024 } )
```

The following document provides a representation of the `collStats` output. Depending on the configuration of your collection and the storage engine, the output fields may vary.

```javascript
{
  "ns" : <string>,
  "size" : <number>,
  "timeseries" : {
     "bucketsNs" : <bucketName>,
     "bucketCount" : <number>,
     "avgBucketSize" : <number>,
     "numBucketInserts" : <number>,
     "numBucketUpdates" : <number>,
     "numBucketsOpenedDueToMetadata" : <number>,
     "numBucketsClosedDueToCount" : <number>,
     "numBucketsClosedDueToSize" : <number>,
     "numBucketsClosedDueToTimeForward" : <number>,
     "numBucketsClosedDueToTimeBackward" : <number>,
     "numBucketsClosedDueToMemoryThreshold" : <number>,
     "numCommits" : <number>,
     "numWaits" : <number>,
     "numMeasurementsCommitted" : <number>,
     "avgNumMeasurementsPerCommit": <number>
  },
  "count" : <number>,
  "avgObjSize" : <number>,
  "numOrphanDocs" : <number>,      // Available starting in MongoDB 6.0
  "storageSize" : <number>,
  "freeStorageSize" : <number>,
  "capped" : <boolean>,
  "max" : <number>,
  "maxSize" :  <number>,
  "wiredTiger" : {
     "metadata" : {
        "formatVersion" : <num>
     },
     "creationString" : <string>
     "type" :  <string>,
     "uri" :  <string>,
     "LSM" : {
        "bloom filter false positives" : <number>,
        "bloom filter hits" : <number>,
        "bloom filter misses" : <number>,
        "bloom filter pages evicted from cache" : <number>,
        "bloom filter pages read into cache" : <number>,
        "bloom filters in the LSM tree" : <number>,
        "total size of bloom filters" : <number>,
        "chunks in the LSM tree" : <number>,
        "highest merge generation in the LSM tree" : <number>,
        "queries that could have benefited from a Bloom filter that did not exist" : <number>,
        "sleep for LSM checkpoint throttle" : <number>,
        "sleep for LSM merge throttle" : <number>
        "total size of bloom filters" : <number>
     },
     "block-manager" : {
         "allocations requiring file extension" : <number>,
         "blocks allocated" : <number>,
         "blocks freed" : <number>,
         "checkpoint size" : <number>,
         "file allocation unit size" : <number>,
         "file bytes available for reuse" : <number>,
         "file magic number" : <number>,
         "file major version number" : <number>,
         "file size in bytes" : <number>,
         "minor version number" : <number>
     },
     "btree" : {
         "btree checkpoint generation" : <number>,
         "column-store fixed-size leaf pages" : <number>,
         "column-store internal pages" : <number>,
         "column-store variable-size RLE encoded values" : <number>,
         "column-store variable-size deleted values" : <number>,
         "column-store variable-size leaf pages" : <number>,
         "fixed-record size" : <number>,
         "maximum internal page key size" : <number>,
         "maximum internal page size" : <number>,
         "maximum leaf page key size" : <number>,
         "maximum leaf page size" : <number>,
         "maximum leaf page value size" : <number>,
         "maximum tree depth" : <number>,
         "number of key/value pairs" : <number>,
         "overflow pages" : <number>,
         "pages rewritten by compaction" : <number>,
         "row-store empty values" : <number>,
         "row-store internal pages" : <number>,
         "row-store leaf pages" : <number>
     },
     "cache" : {
        "bytes currently in the cache" : <number>,
        "bytes dirty in the cache cumulative" : <number>,
        "bytes read into cache" : <number>,
        "bytes written from cache" : <number>,
        "checkpoint blocked page eviction" : <number>,
        "data source pages selected for eviction unable to be evicted" : <number>,
        "eviction walk passes of a file" : <number>,
        "eviction walk target pages histogram - 0-9" : <number>,
        "eviction walk target pages histogram - 10-31" : <number>,
        "eviction walk target pages histogram - 128 and higher" : <number>,
        "eviction walk target pages histogram - 32-63" : <number>,
        "eviction walk target pages histogram - 64-128" : <number>,
        "eviction walks abandoned" : <number>,
        "eviction walks gave up because they restarted their walk twice" : <number>,
        "eviction walks gave up because they saw too many pages and found no candidates" : <number>,
        "eviction walks gave up because they saw too many pages and found too few candidates" : <number>,
        "eviction walks reached end of tree" : <number>,
        "eviction walks started from root of tree" : <number>,
        "eviction walks started from saved location in tree" : <number>,
        "hazard pointer blocked page eviction" : <number>,
        "in-memory page passed criteria to be split" : <number>,
        "in-memory page splits" : <number>,
        "internal pages evicted" : <number>,
        "internal pages split during eviction" : <number>,
        "leaf pages split during eviction" : <number>,
        "modified pages evicted" : <number>,
        "overflow pages read into cache" : <number>,
        "page split during eviction deepened the tree" : <number>,
        "page written requiring cache overflow records" : <number>,
        "pages read into cache" : <number>,
        "pages read into cache after truncate" : <number>,
        "pages read into cache after truncate in prepare state" : <number>,
        "pages read into cache requiring cache overflow entries" : <number>,
        "pages requested from the cache" : <number>,
        "pages seen by eviction walk" : <number>,
        "pages written from cache" : <number>,
        "pages written requiring in-memory restoration" : <number>,
        "tracked dirty bytes in the cache" : <number>,
        "unmodified pages evicted" : <number>
     },
     "cache_walk" : {
        "Average difference between current eviction generation when the page was last considered" : <number>,
        "Average on-disk page image size seen" : <number>,
        "Average time in cache for pages that have been visited by the eviction server" : <number>,
        "Average time in cache for pages that have not been visited by the eviction server" : <number>,
        "Clean pages currently in cache" : <number>,
        "Current eviction generation" : <number>,
        "Dirty pages currently in cache" : <number>,
        "Entries in the root page" : <number>,
        "Internal pages currently in cache" : <number>,
        "Leaf pages currently in cache" : <number>,
        "Maximum difference between current eviction generation when the page was last considered" : <number>,
        "Maximum page size seen" : <number>,
        "Minimum on-disk page image size seen" : <number>,
        "Number of pages never visited by eviction server" : <number>,
        "On-disk page image sizes smaller than a single allocation unit" : <number>,
        "Pages created in memory and never written" : <number>,
        "Pages currently queued for eviction" : <number>,
        "Pages that could not be queued for eviction" : <number>,
        "Refs skipped during cache traversal" : <number>,
        "Size of the root page" : <number>,
        "Total number of pages currently in cache" : <number>
     },
     "compression" : {
        "compressed page maximum internal page size prior to compression" : <number>,
        "compressed page maximum leaf page size prior to compression " : <number>,
        "compressed pages read" : <number>,
        "compressed pages written" : <number>,
        "page written failed to compress" : <number>,
        "page written was too small to compress" : 1
     },
     "cursor" : {
        "bulk loaded cursor insert calls" : <number>,
        "cache cursors reuse count" : <number>,
        "close calls that result in cache" : <number>,
        "create calls" : <number>,
        "insert calls" : <number>,
        "insert key and value bytes" : <number>,
        "modify" : <number>,
        "modify key and value bytes affected" : <number>,
        "modify value bytes modified" : <number>,
        "next calls" : <number>,
        "open cursor count" : <number>,
        "operation restarted" : <number>,
        "prev calls" : <number>,
        "remove calls" : <number>,
        "remove key bytes removed" : <number>,
        "reserve calls" : <number>,
        "reset calls" : <number>,
        "search calls" : <number>,
        "search near calls" : <number>,
        "truncate calls" : <number>,
        "update calls" : <number>,
        "update key and value bytes" : <number>,
        "update value size change" : <num>
     },
     "reconciliation" : {
        "dictionary matches" : <number>,
        "fast-path pages deleted" : <number>,
        "internal page key bytes discarded using suffix compression" : <number>,
        "internal page multi-block writes" : <number>,
        "internal-page overflow keys" : <number>,
        "leaf page key bytes discarded using prefix compression" : <number>,
        "leaf page multi-block writes" : <number>,
        "leaf-page overflow keys" : <number>,
        "maximum blocks required for a page" : <number>,
        "overflow values written" : <number>,
        "page checksum matches" : <number>,
        "page reconciliation calls" : <number>,
        "page reconciliation calls for eviction" : <number>,
        "pages deleted" : <number>
     },
     "session" : {
        "object compaction" : <number>,
     },
     "transaction" : {
        "update conflicts" : <number>
     }
  },
  "nindexes" : <number>,
  "indexDetails" : {
     "_id_" : {
        "metadata" : {
           "formatVersion" : <number>
        },
        ...
     },
     ...
  },
  "indexBuilds" : [
     <string>,
  ],
  "totalIndexSize" : <number>,
  "totalSize" : <number>, 
  "indexSizes" : {
          "_id_" : <number>,
          "<indexName>" : <number>,
          ...
  },
  "scaleFactor" : <number>
  "ok" : <number>
}
```

## Output
