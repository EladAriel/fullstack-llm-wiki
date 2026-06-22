---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/indexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======

# Indexes

Indexes support efficient execution of queries in MongoDB. Without indexes, MongoDB must scan every document in a collection to return query results. If an appropriate index exists for a query, MongoDB uses the index to limit the number of documents it must scan.

Although indexes improve query performance, adding an index has negative performance impact for write operations. For collections with a high write-to-read ratio, indexes are expensive because each insert must also update any indexes.

## Use Cases

If your application repeatedly runs queries on the same fields, create an index on those fields to improve performance. For example, consider the following scenarios:

## Get Started

You can create and manage indexes in [{+atlas+}](https://www.mongodb.com/docs/atlas)_, with a driver method, or with the MongoDB Shell.

### Create and Manage Indexes in {+atlas+}

For deployments hosted in {+atlas+}, you can create and manage indexes with the {+atlas+} UI or the Atlas CLI. {+atlas+} also includes a Performance Advisor that recommends indexes to improve slow queries, ranks suggested indexes by impact, and recommends which indexes to drop.

To learn how to create and manage indexes using the {+atlas+} UI or the Atlas CLI, see :atlas:`Create, View, Drop, and Hide Indexes </atlas-ui/indexes>`.

To learn more about the {+atlas+} Performance Advisor, see :atlas:`Monitor and Improve Slow Queries </performance-advisor>`.

### Create and Manage Indexes with a Driver Method or the MongoDB Shell

You can create and manage indexes with a driver method or the MongoDB Shell. To learn more, see the following resources:

- `manual-create-an-index`
- `index-create-compound`
- `index-create-multikey-basic`
- :ref:`Create an Index to Support Geospatial Queries
<geospatial-index>`

## Details

Indexes are special data structures that store a small portion of the collection's data set in an easy-to-traverse form. MongoDB indexes use a :wikipedia:`B-tree <B-tree>` data structure.

The index stores the value of a specific field or set of fields, ordered by the value of the field. The ordering of the index entries supports efficient equality matches and range-based query operations. In addition, MongoDB can return sorted results using the ordering in the index.

### Restrictions

For index key length limits and per-collection index limits, see `Index Limitations <index-limitations>`.

### Default Index

MongoDB creates a `unique index <index-type-unique> on the id <document-id-field> field during the creation of a collection. The id index prevents clients from inserting two documents with the same value for the id` field. You cannot drop this index.

> **Note:** In `sharded clusters <sharded cluster>`, if you do not use
the `_id` field as the `shard key`, then your application
**must** ensure the uniqueness of the values in the `_id` field.
You can do this by using a field with an auto-generated `ObjectId`.

### Index Names

The default name for an index is the concatenation of the indexed keys and each key's direction in the index (`1` or `-1`) using underscores as a separator. For example, an index created on `{ item : 1, quantity: -1 }` has the name `item_1_quantity_-1`.

You cannot rename an index once created. Instead, you must `drop <drop-an-index>` and recreate the index with a new name.

To learn how to specify the name for an index, see `specify-index-name`.

### Index Build Performance

Applications may encounter reduced performance during index builds, including limited read/write access to the collection. For more information on the index build process, see `index-operations`, including the `index-operations-replicated-build` section.

## Learn More

- MongoDB provides several index types to support specific data and
queries. To learn more, see `index-types`.

- To learn what properties and behaviors you can specify in your index,
see `index-properties`.

- To review considerations for creating an index, see
`manual-indexing-strategies`.

- To learn about the performance impact of indexes, see
`Operational Factors and Data Models <data-model-indexes>`.

- To learn about query settings and indexes, see
:dbcommand:`setQuerySettings`.

## Contents

- Create </core/indexes/create-index>
- Drop </core/indexes/drop-index>
- Types </core/indexes/index-types>
- Properties </core/indexes/index-properties>
- Builds </core/index-creation>
- Manage </tutorial/manage-indexes>
- Measure Use </tutorial/measure-index-use>
- Strategies </applications/indexes>
- Reference </reference/indexes>
