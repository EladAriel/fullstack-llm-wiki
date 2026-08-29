---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.disableAutoSplit.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.969746Z"
---
# sh.disableAutoSplit (mongosh method)

**meta:** :description: Disable the autosplit flag in a sharded cluster using `sh.disableAutoSplit()` from a `mongos` instance.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**note:** .. include:: /includes/autosplit-no-operation.rst

## Description

**method:** sh.disableAutoSplit()

   Disables the autosplit flag in the :data:`config.settings`
   collection. When auto-splitting is enabled for a sharded cluster,
   MongoDB automatically splits chunks based on the shard key values
   the chunk represents to keep the chunks from growing too large.
   
   You can only run :method:`sh.disableAutoSplit()` from a
   :binary:`~bin.mongosh` session that is connected to a
   :binary:`~bin.mongos` instance. :method:`sh.disableAutoSplit()`
   errors if run on a :binary:`~bin.mongod` instance.

   .. note::

      .. include:: /includes/extracts/4.2-changes-stop-balancer-autosplit.rst

   .. seealso::

      - :doc:`/tutorial/manage-sharded-cluster-balancer`
      - :ref:`sharding-balancing`