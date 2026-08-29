---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.analyzeShardKey.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.943252Z"
---
.. _analyzeShardKey-method:

# db.collection.analyzeShardKey() (mongosh method)

**meta:** :description: Evaluate shard keys for collections using `db.collection.analyzeShardKey()` to calculate metrics based on sampled queries.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** db.collection.analyzeShardKey(key, opts)

   Calculates metrics for evaluating a shard key for an unsharded or 
   sharded collection. Metrics are based on sampled queries. You
   can use :dbcommand:`configureQueryAnalyzer` to configure query
   sampling on a collection.


## Compatibility

.. |command| replace:: method

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

``db.collection.analyzeShardKey()`` has this syntax:

.. code-block:: javascript
   
   db.collection.analyzeShardKey(
      <shardKey>,
      {
        keyCharacteristics: <bool>,
        readWriteDistribution: <bool>,
        sampleRate: <double>,
        sampleSize: <int>
      }
    )

## Fields

**include:** /includes/analyzeShardKey-method-command-fields.rst

## Behavior

For behavior, see :ref:`analyzeShardKey Behavior <ask-behavior>`.

## Access Control

For details, see :ref:`analyzeShardKey Access Control 
<ask-access-control>`.

## Output

For sample output, see :ref:`analyzeShardKey Output <ask-output>`.

## Examples

.. |analyzeShardKey| replace:: ``db.collection.analyzeShardKey`` method

**include:** /includes/analyzeShardKey-example-intro.rst

**note:** Before you run the |analyzeShardKey| method, read the
   :ref:`supporting-indexes-ref` section. If you require supporting 
   indexes for the shard key you are analyzing, use the 
   :method:`db.collection.createIndex()` method to create the indexes.

**include:** /includes/analyzeShardKey-examples.rst

## Learn More

- :dbcommand:`configureQueryAnalyzer`
- :dbcommand:`refineCollectionShardKey`
- :ref:`sharding-reference`
- :method:`sh.shardCollection()`