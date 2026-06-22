---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getAuditConfig.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# getAuditConfig (database command)

> **Important:** .. include:: /includes/deprecated-get-set-auditconfig.rst

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     getAuditConfig: 1 
   } 
)
```

## Behavior

`Auditing <auditing>` must be enabled to use :dbcommand:`getAuditConfig`.

Nodes that are not participating in a runtime audit configuration return their current configuration file settings for `auditLog.filter` and `setParameter.auditAuthorizationSuccess`.

Nodes that are participating in the runtime audit synthesize their current configuration from memory. Configuration updates are distributed via the `oplog` mechanism which means updates on :binary:`~bin.mongod` nodes are distributed to secondary nodes very quickly. However, the distribution mechanism is different on :binary:`~bin.mongos` nodes. :binary:`~bin.mongos` nodes have to :parameter:`poll <auditConfigPollingFrequencySecs>` the primary server at regular intervals for configuration updates. You may see stale data due to polling delay if you run :dbcommand:`setAuditConfig` on the primary server and :dbcommand:`getAuditConfig` on a `shard <sharding-introduction>` before the shard has polled the primary server for updated configuration details.

> **Note:** If you are writing automated audit scripts, note that the quoting
style and the types used to represent the cluster signature differ
between `mongosh` and the legacy `mongo` shell. In `mongosh`
the types are Binary and Long. The corresponding types in the legacy
shell are BinData and NumberLong.
.. code-block:: javascript
   :copyable: false
   // mongosh
   signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: Long("0")
   }
   // mongo
   "signature" : {
"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
"keyId" : Long(0)
}

## Examples

Run :dbcommand:`getAuditConfig` on the `admin` database .

```javascript
db.adminCommand({getAuditConfig: 1})
```

The example server is configured to audit read and write operations. It has a filter which captures the desired operations and the `auditAuthorizationSuccess` value has been set to `true`.

```javascript
{
  generation: ObjectId("60e73e74680a655705f16525"),
  filter: {
    atype: 'authCheck',
    'param.command': {
      '$in': [ 'find', 'insert', 'delete', 'update', 'findandmodify' ]
    }
  },
  auditAuthorizationSuccess: true,
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp(1, 1625767540),
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: Long("0")
    }
  },
  operationTime: Timestamp(1, 1625767540)
}
```

> **Seealso:** :method:`db.adminCommand`, :dbcommand:`setAuditConfig`,
`configure audit filters <audit-filter>`
