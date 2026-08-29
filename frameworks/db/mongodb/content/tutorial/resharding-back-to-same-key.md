---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/resharding-back-to-same-key.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.644602Z"
---
.. _resharding-a-collection-back-to-same-key:

# Reshard a Collection back to the Same Shard Key

**facet:** :name: genre
   :values: tutorial

**meta:** :description: Reshard a collection on its current shard key to move data or rebalance shards without changing the shard key. Monitor progress using the $currentOp stage.

## About this Task

Resharding to the same shard key lets you use resharding as a data
movement mechanism. This enables you to:       

**include:** /includes/resharding-about.rst

**include:** /includes/resharding-operation-phases.rst

## Before you Begin

Before you reshard, you must calculate your cluster's 
:ref:`<resharding-storage-req>`, :ref:`<resharding-latency-req>`,
and any :ref:`<resharding-addl-reqs>`.

.. _resharding-storage-req:

### Storage Requirements

**include:** /includes/reshard-to-same-key/storage.rst

.. _resharding-latency-req:

### Latency Requirements

**include:** /includes/reshard-to-same-key/latency.rst

### Reshard Limitations

**include:** /includes/fact-reshard-limitations.rst

.. _resharding-addl-reqs:

### Additional Resource Requirements

**include:** /includes/reshard-to-same-key/addl-resource-reqs.rst

## Steps

**procedure:** :style: normal
   
   .. step:: Reshard the collection.

      Use the :dbcommand:`reshardCollection` command with the ``forceRedistribution`` 
      option set to ``true`` to reshard the collection. The ``reshardCollection``
      command has the following syntax:
 
      .. include:: /includes/reshardCollection-syntax.rst

      For example, this command reshards the ``info.productsInformation``
      collection on its current shard key ``{ product_SKU : 1 }``:

      .. code-block:: javascript
     
         db.adminCommand( 
            {
               reshardCollection: "info.productsInformation",
               key: { product_SKU : 1 },
               forceRedistribution: true
            }
         )
      .. note::
   
         .. include:: /includes/fact-resharding-if-key-is-hashed.rst

   .. step:: Monitor the resharding operation. 
   
      To monitor the resharding operation, you can use the
      :pipeline:`$currentOp` pipeline stage:
   
      .. code-block:: javascript
   
         db.getSiblingDB("admin").aggregate( 
            [
              { $currentOp: { allUsers: true, localOps: false } },
              {
                $match: {
                  type: "op",
                  "originatingCommand.reshardCollection": "<database>.<collection>"
                }
              }
            ] 
         )
   
      .. note::
   
         To see updated values, you need to continuously run the 
         pipeline.
   
      The :pipeline:`$currentOp` pipeline outputs:
   
      - ``totalOperationTimeElapsedSecs``: elapsed operation time in
        seconds
      - .. include:: /includes/remainingOperationTimeEstimatedSecs-details.rst
   
      .. code-block:: javascript
   
         [
           {
             shard: '<shard>',
             type: 'op',
             desc: 'ReshardingRecipientService | ReshardingDonorService | ReshardingCoordinatorService <reshardingUUID>',
             op: 'command',
             ns: '<database>.<collection>',
             originatingCommand: {
               reshardCollection: '<database>.<collection>',
               key: <shardkey>,
               unique: <boolean>,
               collation: { locale: 'simple' }
             },
             totalOperationTimeElapsedSecs: <number>,
             remainingOperationTimeEstimatedSecs: <number>,
             ...
           },
           ...
         ]
      

## Learn More

- :ref:`<reshard-to-same-key>`
- :ref:`<sharding-resharding>`
- :method:`sh.reshardCollection()`