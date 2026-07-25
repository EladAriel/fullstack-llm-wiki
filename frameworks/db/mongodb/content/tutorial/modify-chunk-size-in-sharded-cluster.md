---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/modify-chunk-size-in-sharded-cluster.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# Modify Range Size in a Sharded Cluster

The default range size for a sharded cluster is 128 megabytes. This default range size works well for most deployments; however, if you notice that automatic migrations use more I/O than your hardware can handle, you may want to reduce the range size. A small range size leads to more rapid and frequent migrations. The allowed size is between 1 and 1024 megabytes, inclusive.

To modify the range size, use the following procedure:

#. Connect to any :binary:`~bin.mongos` in the cluster using :binary:`~bin.mongosh`.

#. Issue the following command to switch to the `config-database`:

```javascript
   use config
```

#. Issue the following command to store the global range size configuration value:

```javascript
   db.settings.updateOne(
      { _id: "chunksize" },
      { $set: { _id: "chunksize", value: <sizeInMB> } },  
      { upsert: true }
   )
```

The allowed range size is between 1 and 1024 megabytes, inclusive.

To set the chunk size for a specific collection, see :dbcommand:`configureCollectionBalancing`.
