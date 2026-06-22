---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/balancerCollectionStatus.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# balancerCollectionStatus (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     balancerCollectionStatus: "<db>.<collection>" 
   } 
)
```

Specify the full namespace (`"<db>.<collection>"`) of the sharded collection.

:binary:`~bin.mongosh` provides a wrapper method :method:`sh.balancerCollectionStatus()`.

## Access Control

When running with access control, the user must have the :authaction:`enableSharding` privilege actions on `database and/or collection <resource-specific-db-and-or-collection>` to run the command. That is, a user must have a `role <roles>` that grants the following `privilege <privileges>`:

```javascript
{ resource: { db: <database>, collection: <collection> }, actions: [ "enableSharding" ] }
```

The built-in :authrole:`clusterManager` role provides the appropriate privileges.

## Output Document

The following is an example of a document returned by the command:

```json
{
   "chunkSize": Long("128"),
   "balancerCompliant" : false,
   "firstComplianceViolation" : "chunksImbalance",
   "ok" : 1,
   "operationTime" : Timestamp(1583192967, 16),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1583192967, 16),
      "signature" : {
         "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
         "keyId" : Long(0)
      }
   }
}
```

In addition to the command-specific return fields, the command also returns the `ok` status field, the `operationTime` field, and the `$clusterTime` field for the operation. For details on these fields, see `command-response`.

## Examples

To check whether the chunks of a sharded collection `test.contacts` is currently in balance, connect to a :binary:`~bin.mongos` instance and issue the following command:

```javascript
db.adminCommand( { balancerCollectionStatus: "test.contacts" } )
```

If the chunks for the collection do not need to be moved, the command returns an output similar to the following:

```javascript
{
   "chunkSize": Long("128"),
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

To learn more about:

- Monitoring defragmentation, see
`monitor-defragmentation-sharded-collection`.

- Defragmenting sharded collections, see
`defragment-sharded-collections`.
