---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/steps-deploy-sharded-cluster-config-server-noauth.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. Start each member of the config server replica set.

When starting each :binary:`~bin.mongod`, specify the `mongod` settings using either a configuration file or the command line.

#. Connect mongosh to one of the config server members.

```javascript
   mongosh --host <hostname> --port <port>
```

#. Initiate the replica set.

From `mongosh`, run the :method:`rs.initiate()` method.

`rs.initiate()` can take an optional `replica set configuration document <self-managed-replset-configuration>`. In the replica set configuration document, include:

- The :rsconf:`_id` set to the replica set name specified in either
the :setting:`replication.replSetName` or the `--replSet` option.

- The :rsconf:`configsvr` field  set to `true` for the config server replica set.
- The :rsconf:`members` array with a document per each member of the replica set.
> **Important:**    .. include:: /includes/fact-rs-initiate-once-only.rst
.. code-block:: javascript
   rs.initiate(
     {
       _id: "myReplSet",
       configsvr: true,
       members: [
         { _id : 0, host : "cfg1.example.net:27019" },
         { _id : 1, host : "cfg2.example.net:27019" },
         { _id : 2, host : "cfg3.example.net:27019" }
       ]
     }
   )
See `<self-managed-replset-configuration>` for more
information on replica set configuration documents.
