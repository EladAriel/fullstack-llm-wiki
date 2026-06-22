---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/schema-design-process/create-indexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Create Indexes to Support Your Queries

An index covers a query when the index contains all of the fields scanned by the query. A covered query scans the index and not the collection, which improves query performance.

Indexes can also partially support queries if a subset of the fields queried are indexed.

## About this Task

A single collection can have a maximum of 64 indexes. However, too many indexes can degrade performance before that limit is reached. For collections with a high write-to-read ratio, indexes can degrade performance because each insert must also update any indexes.

## Steps

Repeat this procedure periodically to ensure that your indexes support your current workload.

## Examples

.. include:: /includes/sample-data-usage.rst

.. include:: /includes/sample-data-additional-fields-note.rst

### Create a Single-Key Index

If your application only queries on a single key in a given collection, then you need to create a single-key index for that collection. For example, you can create an index on `title` in the `movies` collection:

This index supports this query:

### Create a Compound Index

If your application performs queries on both a single key and multiple keys, a `compound index <index-type-compound>` is more efficient than a single-key index. For example, you can create an index on the `year`, `runtime`, and `title` fields:

Index Prefixes ``````````````

A compound index supports queries on index prefixes, which are the beginning subsets of indexed fields. For example, the preceding index supports this query:

For more information and performance considerations on index prefixes, see `compound-index-prefix`.

### Create Indexes to Support `$text` Queries

.. include:: /includes/indexes/text-search-indexes-overview.rst

### Create Vector Search Indexes

Vector Search Indexes support queries on vector embeddings. To create Vector Search Indexes, see :atlas:`Index Fields for Vector Search </atlas-vector-search/vector-search-type/>`.

### Index Use and Collation

.. include:: /includes/extracts/collation-index-use.rst

## Learn More

- `esr-indexing-guideline`
- `collation`
- `read-operations-indexing`
