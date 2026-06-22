---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.initiate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# rs.initiate() (mongosh method)

## Description

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## IP Binding

.. include:: /includes/fact-default-bind-ip.rst

## Replica Set Configuration

See `replica-set-configuration-document` for details of the replica set configuration document.

.. include:: /includes/important-hostnames.rst

## Example

The following example initiates a new replica set with three members.

The three :binary:`~bin.mongod` instances must have started with the :option:`--replSet <mongod --replSet>` command line option (or :setting:`replication.replSetName` if using a configuration file) set to `myReplSet` and the :option:`--bind_ip <mongod --bind_ip>` (or :setting:`net.bindIp` if using a configuration file) set appropriately such that other members of the replica set and clients can connect.

.. include:: /includes/warning-bind-ip-security-considerations.rst

Connect :binary:`~bin.mongosh` to one of the :binary:`~bin.mongod` instances and run :method:`rs.initiate()`.

> **Note:** .. include:: /includes/fact-rs-initiate-once-only.rst

.. include:: /includes/important-hostnames.rst

```javascript
rs.initiate(
   {
      _id: "myReplSet",
      version: 1,
      members: [
         { _id: 0, host : "mongodb0.example.net:27017" },
         { _id: 1, host : "mongodb1.example.net:27017" },
         { _id: 2, host : "mongodb2.example.net:27017" }
      ]
   }
)
```

For details on replica set configuration, see `replSetGetConfig-output`.

For details on deploying a replica set, see `/tutorial/deploy-replica-set`.

> **Seealso:** `/administration/replica-set-member-configuration`
