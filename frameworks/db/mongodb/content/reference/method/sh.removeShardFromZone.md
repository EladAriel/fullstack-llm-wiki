---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.removeShardFromZone.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# sh.removeShardFromZone() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

:method:`sh.removeShardFromZone()` does not remove ranges associated with the zone.

To completely remove a zone from the cluster, you must run :method:`sh.removeShardFromZone()` on each shard associated with the zone.

If the shard specified is the last shard associated with the zone, you must ensure there are no remaining ranges associated with the zone. Use :dbcommand:`updateZoneKeyRange` to remove any existing ranges associated to the zone before running :method:`sh.removeShardFromZone()`.

See the `zone <zone-sharding>` manual page for more information on zones in sharded clusters.

### Balancer

Removing the association between a zone and a shard removes the constraints keeping chunks covered by the zone on the shard. During the next balancer round, the balancer may migrate chunks that previously covered by the zone.

See the `sharded cluster balancer <sharding-balancing>` manual page for more information on how migrations work in a sharded cluster.

### Security

For sharded clusters that enforce `access control </tutorial/enable-authentication>`, you must authenticate either as:

- a user whose privileges include:
- :authaction:`update` on the `shards` collection in the `config`
database, and

- :authaction:`find` on the `tags` collection in the `config`
database;

or, alternatively,

- a user whose privileges include :authaction:`enableSharding` on the
`cluster <resource-specific-collection>` resource.

The :authrole:`clusterAdmin` or :authrole:`clusterManager` built-in roles have the appropriate permissions for issuing :method:`sh.removeShardFromZone()`. See the `Role-Based Access Control <authorization>` manual page for more information.

## Example

The following example removes the association between `shard0000` and the `NYC` zone:

```javascript
sh.removeShardFromZone("shard0000", "NYC")
```

> **Seealso:** :method:`sh.addShardToZone()`
:method:`sh.updateZoneKeyRange()`
:method:`sh.removeRangeFromZone()`
