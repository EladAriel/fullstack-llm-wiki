---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-compound.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# Compound Indexes

.. include:: /includes/indexes/fact-compound-index-intro.rst

To create a compound index, use the following prototype:

.. include:: /includes/indexes/code-examples/create-compound-index.rst

## Use Cases

If your application repeatedly runs a query that contains multiple fields, you can create a compound index to improve performance for that query. For example, a grocery store manager often needs to look up inventory items by name and quantity to determine which items are low stock. You can create a compound index on both the `item` and `quantity` fields to improve query performance.

## Get Started

To create a compound index, see `index-create-compound`.

## Details

This section describes technical details and limitations for compound indexes.

### Field Limit

A single compound index can contain up to 32 fields.

### Field Order

The order of the indexed fields impacts the effectiveness of a compound index. Compound indexes contain references to documents according to the order of the fields in the index. To create efficient compound indexes, follow the `ESR (Equality, Sort, Range) guideline <esr-indexing-guideline>`.

### Sort Order

Indexes store references to fields in either ascending (`1`) or descending (`-1`) sort order. For compound indexes, sort order can determine whether the index supports a sort operation. For more information, see `index-compound-sort-order`.

### Hashed Index Fields

Compound indexes may contain **a single** `hashed index field <index-type-hashed>`.

### Index Prefixes

Index prefixes are the beginning subsets of indexed fields. Compound indexes support queries on all fields included in the index prefix.

For example, consider this compound index:

```javascript
{ "item": 1, "location": 1, "stock": 1 }
```

The index has these index prefixes:

- `{ item: 1 }`
- `{ item: 1, location: 1 }`
MongoDB can use the compound index to support queries on these field combinations:

- `item`
- `item` and `location`
- `item`, `location`, and `stock`
MongoDB can also use the index to support a query on the `item` and `stock` fields, since the `item` field corresponds to a prefix. However, the index is not as efficient as `{ item: 1, stock: 1 }`.

For example, consider a query for `"item": "saccharomyces cerevisiae"` and `"stock": 60`. If the collection contains 10000 documents matching `"item": "saccharomyces cerevisiae"` and only 100 of those documents match `"stock": 60`, the query examines 10000 keys. In the `IXSCAN` stage, the query filters those keys by the `stock` field and only returns 100 results to the next stage.

MongoDB's indexing strategy eliminates any need to arrange exact match fields in a particular order. However, if the query does not specify an equality condition on an index prefix that precedes or overlaps with the sort specification, the operation will not efficiently use the index. For more information, see `sort-index-nonprefix-subset`.

MongoDB **cannot** use the compound index to support queries on these field combinations:

- `location`
- `stock`
- `location` and `stock`
Without the `item` field, none of the preceding field combinations correspond to a prefix index.

> **Tip:** If you have a collection that has both a compound index and an index on
its prefix (for example, `{ a: 1, b: 1 }` and `{ a: 1 }`), if
neither index has a `sparse <index-type-sparse>` or :ref:`unique
<index-type-unique>` constraint, you can remove the index on the prefix
(`{ a: 1 }`). MongoDB uses the compound index in all of the situations
that it would have used the prefix index.

### Sparse Compound Indexes

.. include:: /includes/indexes/sparse-compound-indexes.rst

## Learn More

To learn how to create efficient compound indexes, see `esr-indexing-guideline`.

## Contents

- Create </core/indexes/index-types/index-compound/create-compound-index>
- Sort Order </core/indexes/index-types/index-compound/sort-order>
