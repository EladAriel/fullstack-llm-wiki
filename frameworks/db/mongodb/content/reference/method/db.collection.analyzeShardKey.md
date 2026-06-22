---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.analyzeShardKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================

# db.collection.analyzeShardKey() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.analyzeShardKey()` has this syntax:

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

## Fields

.. include:: /includes/analyzeShardKey-method-command-fields.rst

## Behavior

For behavior, see `analyzeShardKey Behavior <ask-behavior>`.

## Access Control

For details, see `analyzeShardKey Access Control <ask-access-control>`.

## Output

For sample output, see `analyzeShardKey Output <ask-output>`.

## Examples

.. include:: /includes/analyzeShardKey-example-intro.rst

> **Note:** Before you run the |analyzeShardKey| method, read the
`supporting-indexes-ref` section. If you require supporting
indexes for the shard key you are analyzing, use the
:method:`db.collection.createIndex()` method to create the indexes.

.. include:: /includes/analyzeShardKey-examples.rst

## Learn More

- :dbcommand:`configureQueryAnalyzer`
- :dbcommand:`refineCollectionShardKey`
- `sharding-reference`
- :method:`sh.shardCollection()`
