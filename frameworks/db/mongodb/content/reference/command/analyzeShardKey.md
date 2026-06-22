---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/analyzeShardKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# analyzeShardKey (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`analyzeShardKey` has this syntax:

```javascript
db.collection.analyzeShardKey(
   <shardKey>,
   {
     keyCharacteristics: <bool>,
     readWriteDistribution: <bool>,
     sampleRate: <double>,
     sampleSize: <int>
   }
 )
```

## Command Fields

.. include:: /includes/analyzeShardKey-command-fields.rst

## Behavior

.. include:: /includes/analyzeShardKey-behavior-intro.rst

### Metrics About Shard Key Characteristics

.. include:: /includes/shard-key-characteristics-metrics.rst

### Metrics About the Read and Write Distribution

.. include:: /includes/shard-key-read-write-distribution.rst

### Non-Blocking Behavior

.. include:: /includes/analyzeShardKey-non-blocking.rst

### Query Sampling

.. include:: /includes/analyzeShardKey-query-sampling.rst

### Supporting Indexes

.. include:: /includes/analyzeShardKey-supporting-indexes.rst

### Read Preference

.. include:: /includes/analyzeShardKey-read-pref.rst

### Limitations

.. include:: /includes/analyzeShardKey-limitations.rst

## Access Control

|analyzeShardKey| requires one of these roles:

- :authaction:`enableSharding` privilege action against the collection
being analyzed.

- :authrole:`clusterManager` role against the cluster.
## Output

.. include:: /includes/analyzeShardKey-output.rst

### keyCharacteristics

.. include:: /includes/analyzeShardKey-keyCharacteristics.rst

### readWriteDistribution

.. include:: /includes/analyzeShardKey-readWriteDistribution-structure.rst

readDistribution Fields ```````````````````````

.. include:: /includes/analyzeShardKey-readWriteDistribution-read.rst

writeDistribution Fields ````````````````````````

.. include:: /includes/analyzeShardKey-readWriteDistribution-write.rst

## Examples

.. include:: /includes/analyzeShardKey-example-intro.rst

> **Note:** Before you run `analyzeShardKey` commands, read the
`supporting-indexes-ref` section earlier on this page. If you
require supporting indexes for the shard key you are analyzing, use
the :method:`db.collection.createIndex()` method to create the
indexes.

.. include:: /includes/analyzeShardKey-examples.rst

## Learn More

- `sharding-reference`
- :method:`sh.shardCollection()`
- :dbcommand:`refineCollectionShardKey`
