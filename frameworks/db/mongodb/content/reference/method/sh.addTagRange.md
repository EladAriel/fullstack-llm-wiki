---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.addTagRange.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# sh.addTagRange() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Bounds

.. include:: /includes/fact-shard-ranges-inclusive-exclusive.rst

### Initial Chunk Distribution for Empty or Non-Existing Collections

If you are considering performing `zone sharding <zone-sharding>` on an empty or non-existent collection, use :method:`sh.addTagRange()` to create the zones and zone ranges before sharding the collection. Creating zones and zone ranges on empty or non-existing collections allows MongoDB to optimize the initial chunk creation and distribution process when sharding the collection. This optimized process supports faster setup of zoned sharding with less balancer overhead than creating zones after sharding. The `balancer <sharding-balancing>` performs all chunk management after the optimized initial chunk creation and distribution.

For an example of defining zones and zone ranges for initial chunk distribution, see `pre-define-zone-range-example`.

Initial Chunk Distribution with Compound Hashed Shard Keys ``````````````````````````````````````````````````````````

MongoDB supports sharding collections on `compound hashed indexes <index-type-compound-hashed>`. MongoDB can perform optimized initial chunk creation and distribution when sharding the empty or non-existing collection on a compound hashed shard key.

For a more complete example of defining zones and zone ranges for initial chunk distribution on a compound hashed shard key, see `pre-define-zone-range-hashed-example`.

### Dropped Collections

.. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

In earlier versions, MongoDB does not remove the tag associations for a dropped collection, and if you later create a new collection with the same name, the old tag associations will apply to the new collection.

## Example

Given a shard key of `{state: 1, zip: 1}`, the following operation creates a tag range covering zip codes in New York State:

```javascript
sh.addTagRange( "exampledb.collection",
                { state: "NY", zip: MinKey },
                { state: "NY", zip: MaxKey },
                "NY"
              )
```
