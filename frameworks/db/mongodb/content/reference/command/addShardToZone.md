---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/addShardToZone.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# addShardToZone (database command)

## Definition

You can only run :dbcommand:`addShardToZone` on the `admin` database from a :binary:`~bin.mongos` instance.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     addShardToZone: <string>,
     zone: <string>
   }
)
```

### Command Fields

The command takes the following fields:

:binary:`~bin.mongosh` provides the helper method :method:`sh.addShardToZone()`.

## Behavior

You can associate a zone with multiple shards, and a shard can associate with multiple zones.

See the `zone <zone-sharding>` manual page for more information on zones in a sharded cluster.

### Ranges

MongoDB effectively ignores zones that do not have at least one range of shard key values associated with it.

To associate a range of shard key values with a zone, use the :dbcommand:`updateZoneKeyRange` database command, or the :method:`sh.updateZoneKeyRange()` shell helper.

.. include:: /includes/extracts/zoned-sharding-updateZoneKeyRange-change.rst

> **Tip:** .. include:: /includes/extracts/zoned-sharding-pre-define-zone.rst

## Security

For sharded clusters that enforce `access control </tutorial/enable-authentication>`, you must authenticate as a user whose privileges include either:

- :authaction:`update` on the `shards` collection in the `config`
database; or, alternatively,

- :authaction:`enableSharding` on the :ref:`cluster
<resource-specific-collection>` resource.

The :authrole:`clusterAdmin` or :authrole:`clusterManager` built-in roles have the appropriate permissions for issuing :dbcommand:`addShardToZone`. See the documentation page for `Role-Based Access Control <authorization>` for more information.

## Example

The following example associates `shard0000` with zone `JFK`:

```javascript
db.adminCommand( { addShardToZone : "shard0000" , zone : "JFK" } )
```

A shard can associate with multiple zones. The following example associates `LGA` to `shard0000`:

```javascript
db.adminCommand( { addShardToZone : "shard0000" , zone : "LGA" } )
```

`shard0000` associates with both the `LGA` zone and the `JFK` zone. In a balanced cluster, MongoDB routes reads and writes covered by either zone to `shard0000`.
