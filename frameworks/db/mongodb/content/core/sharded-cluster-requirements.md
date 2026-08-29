---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharded-cluster-requirements.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.560156Z"
---
.. _sharding-fundamentals:
.. _sharding-capacity-planning:

# Operational Restrictions in Sharded Clusters

**meta:** :description: Understand operational restrictions in sharded clusters, including limitations on certain operations and index consistency requirements.

.. TODO add something about which nodes need to be able to communicate
   with other nodes.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. _sharding-requirements-data:

.. _sharding-operational-restrictions:

## Sharding Operational Restrictions

### Operations Unavailable in Sharded Environments

**include:** /includes/limits-sharding-unavailable-operations.rst

### Single Document Modification Operations in Sharded Collections

.. |single-modification-operation-names| replace:: :method:`~db.collection.updateOne()`
   and :method:`~db.collection.deleteOne()`

.. |single-modification-operation-option| replace:: ``multi: false`` or ``justOne`` 

**include:** /includes/fact-single-modification-in-sharded-collections.rst

To use :method:`~db.collection.findOneAndUpdate()` with a sharded
collection, your query filter must include an equality condition on the
:term:`shard key` to compare the key and value in either of these
formats:

.. code-block:: javascript

   { key: value }
   { key: { $eq: value } }

.. _sharding-requirements-unique-indexes:

### Unique Indexes in Sharded Collections

**include:** /includes/limits-sharding-unique-indexes.rst

### Consistent Indexes

MongoDB does not guarantee consistent indexes across shards.  Index creation
during :dbcommand:`addShard` operations or chunk migrations may not propagate
to new shards.

To check a sharded cluster for consistent indexes, use the
:dbcommand:`checkMetadataConsistency` command:


.. code-block:: javascript

   db.runCommand( {
      checkMetadataConsistency: 1,
      checkIndexes: true
   } )

.. _write-concern-maj-ddl-ops:

### Write Concern for DDL Operations

**include:** /includes/ddl-ops-write-concern-sharded-clusters.rst