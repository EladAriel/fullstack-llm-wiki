---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/stop-unsharding-collection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.647696Z"
---
.. _stop-unshard-collection-task:

# Stop Unsharding a Collection

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**facet:** :name: genre
   :values: tutorial

You can stop unsharding a sharded collection with the
:dbcommand:`abortUnshardCollection` command. 

## About this Task

To stop an in-progress ``unshardCollection`` operation, run the 
``abortUnshardCollection`` command.

.. |operation| replace:: unsharding
**include:** /includes/resharding-oplog-note.rst

### Compatibility

You can perform this task on deployments hosted in the following
environments: 

**include:** /includes/fact-environments-atlas-only.rst

**note:** This task is not available on the {+atlas+} Free or Flex Tiers.

**include:** /includes/fact-environments-onprem-only.rst

### Restrictions

.. |uc| replace:: ``abortUnshardCollection``

**include:** /includes/auc-considerations.rst

## Access Control

If your deployment has :ref:`access control <authorization>` enabled, 
the :authrole:`enableSharding` role grants you access to run the 
``abortUnshardCollection`` command.

## Steps

**procedure:** :style: normal

   .. step:: Stop unsharding the collection

      To stop unshard a collection, run the :dbcommand:`abortUnshardCollection` command.
      The following example stops ``unshardCollection`` operations on the ``us_accounts`` 
      in the ``sales`` database:

      .. code-block:: javascript

         db.adminCommand( {
            abortUnshardCollection: "sales.us_accounts",
         } )

   .. step:: Confirm the unsharding operation has been stopped

      To confirm the ``unshardCollection`` operation has been stopped,
      use the :method:`sh.status()` method:
  
      .. code-block:: javascript

         sh.status()

      This sample output shows the collection as sharded with its 
      :ref:`original shard key <sharding-status-collection-fields>`:

      .. code-block:: javascript
         :copyable: false
         :emphasize-lines: 3

         collections: {
            'sales.us_accounts': {
               shardKey: { account_number: 1 },
               unique: false,
               balancing: true,
               chunkMetadata: [
                 { shard: 'shard-0', nChunks: 1 },
                 { shard: 'shard-1', nChunks: 1 }
               ],
               chunks: [
                 { min: { _id: MinKey() }, max: { _id: Long('0') }, 'on shard': 'shard-0', 'last modified': Timestamp({ t: 1, i: 0 }) },
                 { min: { _id: Long('0') }, max: { _id: MaxKey() }, 'on shard': 'shard-1', 'last modified': Timestamp({ t: 1, i: 1 }) }
               ], 
               ... }
             ... }
 
## Learn More

- :dbcommand:`abortUnshardCollection`
- :method:`sh.abortUnshardCollection()`
- :ref:`unshard-collection-task`