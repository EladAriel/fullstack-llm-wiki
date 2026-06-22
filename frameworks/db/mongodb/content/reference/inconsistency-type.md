---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
