---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/shard-collection-with-unique-index.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.620690Z"
---
.. _manual-shard-collection-with-unique:

# Sharded Collections with Unique Indexes

Unique indexes are not supported on sharded collections unless
the index is the shard key or includes it as a prefix.

## About this Task

The uniqueness constraint on an index ensures that documents in
the collection have a unique value set on the field. With
sharded collections, MongoDB does not enforce the uniqueness
constraint on the field unless the index is the shard key or it
includes the shard key as a prefix. To prevent issues:

- For sharded collections, if you create a unique index that
  doesn't use the shard key, MongoDB returns an error when you run the
  :dbcommand:`createIndexes` command.

- If you shard a collection and the collection contains a unique
  index that doesn't use the shard key, MongoDB returns an error
  when you run the :dbcommand:`shardCollection` command.

## Steps

**procedure:** :style: normal

   .. step:: Create the shard key

      Create the index you plan to use as the shard key:

      .. io-code-block:: 

         .. input::
            :language: javascript

            db.names.createIndex( { region_id: 1 } )

         .. output::
            :language: javascript

            region_id_1
            

   .. step:: Create a unique index

      Create the unique index for the collection. Include the
      shard key as a prefix for the index:

      .. io-code-block::

         .. input::
            :language: javascript

            db.names.createIndex( 
               { region_id: 1, email: 1 }, 
               { unique: true } 
            )

         .. output::
            :language: javascript

            region_id_1_email_1

   .. step:: Shard the collection

      .. io-code-block::

         .. input::
            :language: javascript

            sh.shardCollection( "accounts.names", { region_id: 1 } )

         .. output::
            :language: javascript

            {
               collectionsharded: 'accounts.names',
               ok: 1,
               '$clusterTime': {
                  clusterTime: Timestamp( { t: 1759260515, i: 58 } ),
                  signature: {
                     hash: Binary.createFromBase64( 'AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0 ),
                     keyId: Long( '0' )
                  }
               },
               operationTime: Timestamp( { t: 1759260515, i: 57 } )
            }


## Learn More

- :ref:`index-type-unique`

- :ref:`sharding-introduction`

- :dbcommand:`shardCollection`

- :dbcommand:`createIndexes`

- :method:`sh.shardCollection`

- :method:`db.collection.createIndex`

