---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-find-shard-key.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.531429Z"
---
.. _sharding-find-shard-key:
.. _sharding-display-shard-key:

# Display a Shard Key

**meta:** :description: Discover how to find the shard key for a sharded collection by using the `db.printShardingStatus()` method on a `mongos` instance.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

Every sharded collection has a :ref:`shard key <sharding-shard-key>`. To
display the shard key, connect to a :binary:`mongos` instance and run
the :method:`db.printShardingStatus()` method:

.. code-block:: javascript

   db.printShardingStatus()

The output resembles:

**include:** /includes/reference/sharded-status-output.rst

For more details on the ``db.printShardingStatus()`` output, see the
:ref:`sharded collection section <sharded-collection-output-reference>`
on the :method:`sh.status()` page.