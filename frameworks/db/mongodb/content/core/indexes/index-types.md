---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========

# Index Types

This page describes the types of indexes you can create in MongoDB. Different index types support different types of data and queries.

## Single Field Index

Single field indexes collect and sort data from a single field in each document in a collection.

This image shows an index on a single field, `score`:

.. include:: /images/index-ascending.rst

To learn more, see `indexes-single-field`.

## Compound Index

.. include:: /includes/indexes/fact-compound-index-intro.rst

To learn more, see `index-type-compound`.

## Multikey Index

Multikey indexes collect and sort data stored in arrays.

This image shows a multikey index on the `addr.zip` field:

.. include:: /images/index-multikey.rst

To learn more, see `index-type-multikey`.

## Wildcard Index

Wildcard indexes apply to collections with flexible schemas, where document field names may differ. Use wildcard indexes to support queries against arbitrary or unknown field names.

To learn more, see `wildcard-index-core`.

## Geospatial Index

Geospatial indexes improve performance for queries on geospatial coordinate data. To learn more, see `geospatial-index`.

## Hashed Index

Hashed indexes support `hashed sharding <sharding-hashed-sharding>`. Hashed indexes index the hash of a field's value.

To learn more, see `index-type-hashed`.

## Text Index

Text indexes support `$text` queries on fields containing string content.

To learn more, see `index-type-text`.

> **Note:** MongoDB also offers the following text search solutions:
- :atlas:`{+fts+} </atlas-search/>` provides improved performance
  and functionality compared to on-premises text search.
- :atlas:`{+avs+} </atlas-vector-search/vector-search-overview/>`
  provides vector search capabilities to perform semantic, hybrid, and generative
  search.

## Clustered Index

Clustered indexes specify the order in which `clustered collections <clustered-collections>` store data. Collections created with a clustered index are called clustered collections.

To learn how to create a collection with a clustered index, see `clustered-collections-index-example`.

## Contents

- Single Field </core/indexes/index-types/index-single>
- Compound </core/indexes/index-types/index-compound>
- Multikey </core/indexes/index-types/index-multikey>
- Wildcard </core/indexes/index-types/index-wildcard>
- Geospatial </core/indexes/index-types/index-geospatial>
- Hashed </core/indexes/index-types/index-hashed>
- Text </core/indexes/index-types/index-text>
- Clustered </core/clustered-collections>
