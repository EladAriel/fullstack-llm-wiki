---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

################### Inconsistency Types ###################

.. versionadded:: 7.0

The :dbcommand:`checkMetadataConsistency` command performs a series of consistency checks on sharding metadata and indexes and returns an array of inconsistency documents.

## Contents

- /reference/inconsistency-type/CollectionAuxiliaryMetadataMismatch
- /reference/inconsistency-type/CollectionOptionsMismatch
- /reference/inconsistency-type/CollectionUUIDMismatch
- /reference/inconsistency-type/CorruptedChunkShardKey
- /reference/inconsistency-type/CorruptedZoneShardKey
- /reference/inconsistency-type/HiddenShardedCollection
- /reference/inconsistency-type/InconsistentIndex
- /reference/inconsistency-type/MisplacedCollection
- /reference/inconsistency-type/MissingLocalCollection
- /reference/inconsistency-type/MissingRoutingTable
- /reference/inconsistency-type/MissingShardKeyIndex
- /reference/inconsistency-type/RangeDeletionMissingShardKeyIndex
- /reference/inconsistency-type/RoutingTableMissingMaxKey
- /reference/inconsistency-type/RoutingTableMissingMinKey
- /reference/inconsistency-type/RoutingTableRangeGap
- /reference/inconsistency-type/RoutingTableRangeOverlap
- /reference/inconsistency-type/ShardCatalogCacheCollectionMetadataMismatch
- /reference/inconsistency-type/TrackedUnshardedCollectionHasInvalidKey
- /reference/inconsistency-type/TrackedUnshardedCollectionHasMultipleChunks
- /reference/inconsistency-type/ZonesRangeOverlap
