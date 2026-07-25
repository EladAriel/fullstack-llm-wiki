---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.balancerCollectionStatus.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================================

# sh.balancerCollectionStatus() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`sh.balancerCollectionStatus` has the following form:

```javascript
sh.balancerCollectionStatus( <namespace> )
```

### Parameter

The :method:`sh.balancerCollectionStatus()` method takes the following parameter:

## Access Control

When running with access control, the user must have the :authaction:`enableSharding` privilege actions on `database and/or collection <resource-specific-db-and-or-collection>` to run the method. That is, a user must have a `role <roles>` that grants the following `privilege <privileges>`:

```javascript
{ resource: { db: <database>, collection: <collection> }, actions: [ "enableSharding" ] }
```

The built-in :authrole:`clusterManager` role provides the appropriate privileges.

## Examples

To check whether the chunks of a sharded collection `test.contacts` is currently in balance, connect to a :binary:`~bin.mongos` instance and issue the following:

```javascript
sh.balancerCollectionStatus("test.contacts")
```

If the chunks for the collection do not need to be moved, the method returns an output similar to the following:

```javascript
{
   "balancerCompliant" : true,
   "ok" : 1,
   "operationTime" : Timestamp(1583193238, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1583193238, 1),
      "signature" : {
         "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
         "keyId" : Long(0)
      }
   }
}
```

### Ongoing Defragmentation Process

.. include:: /includes/sharding/balancer-status-defrag-example.rst

For the description of the output, see `balancerCollectionStatus Output <cmd-balancer-CollectionStatus-output>`.
