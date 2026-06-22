---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/deploy-replica-set-for-testing.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================================

# Deploy a Self-Managed Replica Set for Testing and Development

This procedure describes deploying a replica set in a development or test environment. For a production deployment, refer to the `/tutorial/deploy-replica-set` tutorial.

.. include:: /includes/introduction-deploy-replica-set.rst

## Requirements

For test and development systems, you can run your :binary:`~bin.mongod` instances on a local system, or within a virtual instance.

Before you can deploy a replica set, you must install MongoDB on each system that will be part of your `replica set`. If you have not already installed MongoDB, see the `installation tutorials <tutorial-installation>`.

Each member must be able to connect to every other member. For instructions on how to check your connection, see `replica-set-troubleshooting-check-connection`.

## Considerations

.. include:: /includes/important-hostnames.rst

### IP Binding

.. include:: /includes/fact-default-bind-ip.rst

In this test deployment, the three members run on the same machine.

### Replica Set Naming

> **Important:** development deployments.

The examples in this procedure create a new replica set named `rs0`.

.. include:: /includes/fact-unique-replica-set-names.rst

## Procedure

.. include:: /includes/important-hostnames.rst

1. Create the necessary data directories for each member by issuing a
command similar to the following:

```bash
   mkdir -p /srv/mongodb/rs0-0  /srv/mongodb/rs0-1 /srv/mongodb/rs0-2

This will create directories called "rs0-0", "rs0-1", and "rs0-2", which
will contain the instances' database files.
```

#. Start your :binary:`~bin.mongod` instances in their own shell windows by issuing the following commands:

.. include:: /includes/warning-bind-ip-security-considerations.rst

#. Connect to one of your :binary:`~bin.mongod` instances through :binary:`~bin.mongosh`. You will need to indicate which instance by specifying its port number. For the sake of simplicity and clarity, you may want to choose the first one, as in the following command;

```bash
   mongosh --port 27017
```

#. In :binary:`~bin.mongosh`, use :method:`rs.initiate()` to initiate the replica set. You can create a replica set configuration object in :binary:`~bin.mongosh` environment, as in the following example:

```javascript
   rsconf = {
     _id: "rs0",
     members: [
       {
        _id: 0,
        host: "<hostname>:27017"
       },
       {
        _id: 1,
        host: "<hostname>:27018"
       },
       {
        _id: 2,
        host: "<hostname>:27019"
       }
      ]
   }

replacing ``<hostname>`` with your system's hostname,
and then pass the ``rsconf`` file to :method:`rs.initiate()` as
follows:

.. code-block:: javascript

   rs.initiate( rsconf )
```

#. Display the current `replica configuration </reference/replica-configuration>` by issuing the following command:

```javascript
   rs.conf()

The replica set configuration object resembles the following:

.. code-block:: json

   {
      "_id" : "rs0",
      "version" : 1,
      "protocolVersion" : Long(1),
      "members" : [
         {
            "_id" : 0,
            "host" : "<hostname>:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : Long(0),
            "votes" : 1
         },
         {
            "_id" : 1,
            "host" : "<hostname>:27018",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : Long(0),
            "votes" : 1
         },
         {
            "_id" : 2,
            "host" : "<hostname>:27019",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : Long(0),
            "votes" : 1
         }
      ],
      "settings" : {
         "chainingAllowed" : true,
         "heartbeatIntervalMillis" : 2000,
         "heartbeatTimeoutSecs" : 10,
         "electionTimeoutMillis" : 10000,
         "catchUpTimeoutMillis" : -1,
         "getLastErrorModes" : {

         },
         "getLastErrorDefaults" : {
            "w" : 1,
            "wtimeout" : 0
         },
         "replicaSetId" : ObjectId("598f630adc9053c6ee6d5f38")
      }
   }
```

Check the status of your replica set at any time with the :method:`rs.status()` operation.

> **Seealso:** The documentation of the following shell functions for
more information:
- :method:`rs.initiate()`
- :method:`rs.conf()`
- :method:`rs.reconfig()`
- :method:`rs.add()`
You may also consider the `simple setup script
<https://github.com/mongodb/mongo-snippets/blob/master/replication/simple-setup.py>`_
as an example of a basic automatically-configured replica set.
Refer to `Replica Set Read and Write Semantics <replica-set-read-write-semantics>`
for a detailed explanation of read and write semantics in MongoDB.

.. include:: /includes/fact-oplog-size.rst
