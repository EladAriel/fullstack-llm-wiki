---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/removeShardFromZone.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# removeShardFromZone (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

You can only run :dbcommand:`removeShardFromZone` on the `admin` database from a :binary:`~bin.mongos` instance.

The command has the following syntax:

```javascript
db.adminCommand(
   {
     removeShardFromZone: <string>,
     zone: <string>
   }
)
```

## Command Fields

The command takes the following fields:

:binary:`~bin.mongosh` provides the helper method :method:`sh.removeShardFromZone()`.

## Behavior

:dbcommand:`removeShardFromZone` does not remove ranges associated with the zone.

To completely remove a zone from the cluster, you must run :dbcommand:`removeShardFromZone` on each shard associated with the zone.

If the shard specified is the last shard associated with the zone, you must ensure there are no remaining shard key ranges associated with the zone. Use :dbcommand:`updateZoneKeyRange` to remove any existing ranges associated with the zone before running :dbcommand:`removeShardFromZone`.

See the `zone <zone-sharding>` manual page for more information on zones in sharded clusters.

### Security

For sharded clusters that enforce `access control </tutorial/enable-authentication>`, you must authenticate either as:

- a user whose privileges include:
- :authaction:`update` on the `shards` collection in the `config`
database, and

- :authaction:`find` on the `tags` collection in the `config`
database;

or, alternatively

- a user whose privileges include :authaction:`enableSharding` on the
`cluster <resource-specific-collection>` resource.

The :authrole:`clusterAdmin` or :authrole:`clusterManager` built-in roles have the appropriate permissions for issuing :dbcommand:`removeShardFromZone`. See the `Role-Based Access Control <authorization>` manual page for more information.

## Example

The following example removes the association between `shard0000` and zone `NYC`:

```javascript
db.adminCommand( { removeShardFromZone : "shard0000" , zone : "NYC" } )
```
