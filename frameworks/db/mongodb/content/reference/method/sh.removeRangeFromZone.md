---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.removeRangeFromZone.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# sh.removeRangeFromZone() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

`sh.removeRangeFromZone()` doesn't remove the association between a zone and a shard. It also doesn't remove the zone itself.

See the `zone <zone-sharding>` manual page for more information on zones in sharded clusters.

### Balancer

Removing the association between a range and a zone removes the constraints keeping chunks covered by the range on the shards inside that zone. During the next balancer round, the balancer may migrate chunks that were previously covered by the zone.

See the documentation for the `sharded cluster balancer <sharding-balancing>` for more information on how migrations work in a sharded cluster.

### Security

For sharded clusters running with `authentication <authentication>`, you must authenticate as either:

- a user whose privileges include the specified actions on various
collections in the `config` database:

- :authaction:`find` on the `config.shards` collection
- :authaction:`find`, :authaction:`update`, and :authaction:`remove`
on the `config.tags` collection;

or, alternatively

- a user whose privileges include :authaction:`enableSharding` on the
`cluster <resource-specific-collection>` resource.

The :authrole:`clusterAdmin` or :authrole:`clusterManager` built-in roles have the appropriate permissions for running `sh.removeRangeFromZone()`. See the documentation page for `Role-Based Access Control <authorization>` for more information.

## Example

Given a sharded collection `exampledb.collection` with a shard key of `{ a : 1 }`, the following operation removes the range with a lower bound of `1` and an upper bound of `10`:

```javascript
sh.removeRangeFromZone( "exampledb.collection",
                { a : 1 },
                { a : 10 }
              )
```

The `min` and `max` must match exactly the bounds of the target range. The following operation attempts to remove the previously created range, but specifies `{ a : 0 }` as the `min` bound:

```javascript
admin = db.getSiblingDB("admin")
admin.runCommand(
   {
      updateZoneKeyRange : "exampledb.collection",
      min : { a : 0 },
      max : { a : 10 },
      zone : null
   }
)
```

While the range of `{ a : 0 }` and `{ a : 10 }` encompasses the existing range, it is not an exact match and therefore `sh.removeRangeFromZone()` does not remove anything.

### Compound Shard Key

Given a sharded collection `exampledb.collection` with a shard key of `{ a : 1, b : 1 }`, the following operation removes the range with a lower bound of `{ a : 1, b : 1}` and an upper bound of `{ a : 10, b : 10 }`:

```javascript
sh.removeRangeFromZone( "exampledb.collection",
                { a : 1, b : 1 },
                { a : 10, b : 10 }
              )
```

Given the previous example, if there was an existing range with a lower bound of `{ a : 1, b : 5 }` and an upper bound of `{ a : 10, b : 1 }`, the operation would not remove that range, as it is not an exact match of the minimum and maximum passed to `sh.removeRangeFromZone()`.
