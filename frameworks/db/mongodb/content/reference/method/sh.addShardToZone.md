---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.addShardToZone.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# sh.addShardToZone() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

You can associate a zone with multiple shards, and a shard can associate with multiple zones.

See the `zone <zone-sharding>` manual page for more information on zones in sharded clusters.

### Ranges

MongoDB effectively ignores zones that do not have at least one range of shard key values associated with it.

To associate a range of shard key values with a zone, use the :method:`sh.updateZoneKeyRange()` method.

.. include:: /includes/extracts/zoned-sharding-updateZoneKeyRange-change.rst

> **Tip:** .. include:: /includes/extracts/zoned-sharding-pre-define-zone.rst

## Security

For sharded clusters that enforce `access control </tutorial/enable-authentication>`, you must authenticate as a user whose privileges include either:

- :authaction:`update` on the `shards` collection in the `config`
database; or, alternatively,

- :authaction:`enableSharding` on the :ref:`cluster
<resource-specific-collection>` resource.

The :authrole:`clusterAdmin` or :authrole:`clusterManager` built-in roles have the appropriate permissions for issuing :method:`sh.addShardToZone()`. See the `Role-Based Access Control <authorization>` manual page for more information.

## Example

The following example adds three zones, `NYC`, `LAX`, and `NRT`, associating each to a shard:

```javascript
sh.addShardToZone("shard0000", "JFK")
sh.addShardToZone("shard0001", "LAX")
sh.addShardToZone("shard0002", "NRT")
```

A shard can associate with multiple zones. The following example associates `LGA` to `shard0000`:

```javascript
sh.addShardToZone("shard0000", "LGA")
```

`shard0000` associates with both the `LGA` zone and the `JFK` zone. In a balanced cluster, MongoDB routes reads and writes covered by either zone to `shard0000`.

> **Seealso:** - :method:`sh.updateZoneKeyRange()`
- :method:`sh.removeShardFromZone()`
