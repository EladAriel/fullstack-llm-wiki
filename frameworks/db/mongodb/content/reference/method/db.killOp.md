---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.killOp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# db.killOp() (mongosh method)

## Description

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

> **Important:** {+atlas+} limits the use of this method to the MongoDB user who ran the
operation. For information on Atlas support for all commands,
see :atlas:`Unsupported Commands </unsupported-commands>`.

.. include:: /includes/fact-environments-onprem-only.rst

## Sharded Cluster

### Kill Read Operations

The :method:`db.killOp()` method can be run on a :binary:`~bin.mongos` and can kill queries (read operations) that are running on more than one shard in a cluster.

For example, to kill a query operation on a sharded cluster:

### Kill Write Operations

Within a Session MongoDB drivers associate all operations with a `server session <server-sessions>`, with the exception of unacknowledged writes.

If the write operation is associated with a session, you can use the :dbcommand:`killSessions` command on the :binary:`~bin.mongos` to kill the write operation across shards.

#. Run the aggregation pipeline :pipeline:`$currentOp` on the :binary:`~bin.mongos` to find the `lsid` (logical session id).

```javascript
      use admin
      db.aggregate( [
         { $currentOp : { allUsers: true, localOps: true } },
         { $match : <filter condition> } // Optional.  Specify the condition to find the op.
                                         // e.g. { "op" : "update", "ns": "mydb.someCollection" }
      ] )

   #. Using the returned ``lsid`` information, issue the
      :dbcommand:`killSessions` command on the
      :binary:`~bin.mongos` to kill the operation on the shards.

      .. code-block:: javascript

         db.adminCommand( { killSessions: [
            { "id" : UUID("80e48c5a-f7fb-4541-8ac0-9e3a1ed224a4"), "uid" : BinData(0,"47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=") }
         ] } )
```

Without a Session If the write operation is **not** associated with a session, you must find and kill the operation on all the shards associated with the write.

#. From a :binary:`~bin.mongos`, run the aggregation pipeline :pipeline:`$currentOp` to find the opid(s) of the query operation on the shards:

```javascript
      use admin
      db.aggregate( [
         { $currentOp : { allUsers: true } },
         { $match : <filter condition> } // Optional.  Specify the condition to find the op.
      ] )

   When run on a :binary:`~bin.mongos`, :pipeline:`$currentOp`
   returns the opids in the format of ``"<shardName>:<opid on that
   shard>"``; e.g.

   .. code-block:: javascript

      {
         "shard" : "shardB",
         ..
         "opid" : "shardB:79214",
         ...
      },
      {
         "shard" : "shardA",
         ..
         "opid" : "shardA:100913",
         ...
      },

#. Using the opid information, issue :method:`db.killOp()` on the
   :binary:`~bin.mongos` to kill the operation on the shards.

   .. code-block:: javascript

      db.killOp("shardB:79014");
      db.killOp("shardA:100813");
```

## Access Control

On systems running with :setting:`~security.authorization`, to kill operations not owned by the user, the user must have access that includes the :authaction:`killop` privilege action.

On :binary:`~bin.mongod` instances, users can kill their own operations even without the :authaction:`killop` privilege action.

> **Seealso:** :pipeline:`$currentOp`
