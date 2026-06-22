---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/manage-shard-zone.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Manage Shard Zones

In sharded clusters, you can create zones that represent a group of shards and associate one or more ranges of `shard key` values to that zone. MongoDB routes reads and writes that fall into a zone range only to those shards inside of the zone.

> **Tip:** .. include:: /includes/extracts/zoned-sharding-pre-define-zone.rst

## Add Shards to a Zone

Associate a Zone with a particular shard using the :method:`sh.addShardToZone()` method when connected to a :binary:`~bin.mongos` instance. A single shard may have multiple zones, and multiple shards may also have the same zone.

You may remove zone from a particular shard using the :method:`sh.removeShardFromZone()` method when connected to a :binary:`~bin.mongos` instance, as in the following example, which removes the `NRT` zone from a shard:

```javascript
sh.removeShardFromZone("shard0002", "NRT")
```

## Create a Zone Range

To define the zone's range of shard keys, use the :method:`sh.updateZoneKeyRange()` method when connected to a :binary:`~bin.mongos` instance. Any given shard key range may only have one assigned zone. You cannot overlap defined ranges.

> **Note:** - .. include:: /includes/fact-shard-ranges-inclusive-exclusive.rst
- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

## Remove a Zone Range

Use the shell helper method :method:`sh.removeRangeFromZone()` to remove a range from a zone.

> **Note:** .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

## View Existing Zones

Use :method:`sh.status()` to list the zones associated to each shard in the cluster. You can also view a shards zones by querying the `config.shards` collection in the `config` database.

The following example uses the :method:`~db.collection.find()` method to return all shards with the `NYC` zone.

```javascript
use config
db.shards.find({ tags: "NYC" })
```

You can find zone ranges for all `namespaces <namespace>` in the `config.tags` collection of the `config` database. The output of :method:`sh.status()` also displays all zone ranges.

The following example uses the :method:`~db.collection.find()` method to return any range associated to the `NYC` zone.

```javascript
use config
db.tags.find({ tag: "NYC" })
```

## Contents

- Update Shard Zone </tutorial/manage-shard-zone/update-existing-shard-zone>
