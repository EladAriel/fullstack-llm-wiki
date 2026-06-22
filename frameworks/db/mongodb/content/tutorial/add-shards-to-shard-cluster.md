---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/add-shards-to-shard-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Add Shards to a Cluster

You add shards to a `sharded cluster` after you create the cluster or any time that you need to add capacity to the cluster. If you have not created a sharded cluster, see `sharding-procedure-setup`.

All shards must be `replica sets <replica set>`.

## Considerations

### Balancing

.. include:: /includes/fact-adding-shards-changes-cluster-balance.rst

### Capacity Planning

When adding a shard to a cluster, always ensure that the cluster has enough capacity to support the migration required for balancing the cluster without affecting legitimate production traffic.

### DDL Operations

If you add a shard while your cluster executes a DDL operation (operation that modifies a collection such as :dbcommand:`reshardCollection`), the operation that adds a shard only executes after the concurrent DDL operation finishes.

## Add a Shard to a Cluster

You interact with a sharded cluster by connecting to a :binary:`~bin.mongos` instance.

1. In :binary:`~bin.mongosh`, connect to the :binary:`~bin.mongos`
instance. For example, if a :binary:`~bin.mongos` is accessible at `mongos0.example.net` on port `27017`, issue the following command:

```bash
   mongosh --host mongos0.example.net --port 27017
```

#. Add a shard replica set to the cluster using the :method:`sh.addShard()` method, as shown in the example below. Issue :method:`sh.addShard()` separately for each shard. Specify the name of the replica set and a member of the set.

> **Note:**    You can instead use the :dbcommand:`addShard` database
   command, which lets you specify a name and maximum size for the
   shard. If you do not specify these, MongoDB automatically assigns
   a name and maximum size. To use the database command, see
   :dbcommand:`addShard`.
The following example illustrates adding a shard with
:method:`sh.addShard()`:
To add a shard replica set named `rs1` with a member
running on port `27018` on `mongodb0.example.net`, issue the
following command:
.. code-block:: javascript
   sh.addShard( "rs1/mongodb0.example.net:27018" )
.. note:: It might take some time for `chunks <chunk>` to
   migrate to the new shard.
