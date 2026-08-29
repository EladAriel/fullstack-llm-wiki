---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/defragment-sharded-collections/start-defragmenting-sharded-collection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.799430Z"
---
.. _start-defragmenting-sharded-collection:

# Start Defragmenting a Sharded Collection

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

To start defragmenting a sharded collection, use the
:dbcommand:`configureCollectionBalancing` command with the
``defragmentCollection`` option set to ``true``.

## About this Task

**include:** /includes/defragment-sharded-collections-conditions.rst

**include:** /includes/defragment-sharded-collections-example.rst

## Before you Begin

Connect to :binary:`~bin.mongos`.

## Procedure

**procedure:** :style: normal

   .. step:: Start defragmenting the collection

      Run:

      .. code-block:: javascript

         db.adminCommand(
            {
               configureCollectionBalancing: "test.ordersShardedCollection",
               defragmentCollection: true
            }
         )

   .. step:: Ensure defragmentation started

      Ensure ``ok`` is ``1`` in the command output, which indicates the
      command execution was successful:

      .. code-block:: javascript
         :copyable: false
         :emphasize-lines: 2

         {
            ok: 1,
            '$clusterTime': {
               clusterTime: Timestamp({ t: 1677616966, i: 8 }),
               signature: {
                  hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
                  keyId: Long("0")
               }
            },
            operationTime: Timestamp({ t: 1677616966, i: 8 })
         }

## Next Steps

You can monitor the collection's defragmentation progress. For details,
see :ref:`monitor-defragmentation-sharded-collection`.

## Learn More

**include:** /includes/defragment-sharded-collections-learn-more.rst