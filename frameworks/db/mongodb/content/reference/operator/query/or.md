---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/or.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $or (query predicate operator)

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :query:`$or` operator has the following syntax:

```javascript
{ $or: [ { <expression1> }, { <expression2> }, ... , { <expressionN> } ] }
```

.. include:: /includes/sample-data-usage.rst

Consider the following example:

This query selects all documents in the `movies` collection that meet either of the following conditions:

- The `runtime` field value is greater than `1000`.
- The `year` field value is earlier than `1910`.
## Behaviors

### `$or` Clauses and Indexes

When evaluating the clauses in the :query:`$or` expression, MongoDB performs a collection scan or an index scan. If all clauses are supported by indexes, MongoDB performs index scans. To use indexes to evaluate an :query:`$or` expression, all the clauses in the :query:`$or` expression must be supported by indexes. Otherwise, MongoDB performs a collection scan.

When using indexes with :query:`$or` queries, each clause of an :query:`$or` can use its own index. Consider this query:

To support this query, create one index on `runtime` and another index on `year`, rather than a compound index:

### `$or` and `text` Queries

If :query:`$or` includes a :query:`$text` query, all clauses in the :query:`$or` array must be supported by an index. This is because a `$text` query must use an index, and :query:`$or` can only use indexes if all its clauses are supported by indexes. If the `$text` query cannot use an index, the query returns an error.

.. include:: /includes/text-search-legacy-atlas-section.rst

### `$or` and Geospatial Queries

`$or` supports `geospatial clauses <geospatial-query-operators>`. However, if you use a near clause (:query:`$near` or :query:`$nearSphere`), `$or` cannot contain any other clauses. Using `$or` with a single clause has the same effect as omitting the `$or` operator.

The following query is valid because `$or` uses a non-near geospatial clause (`$geoIntersects`):

### `$or` and Sort Operations

When executing :query:`$or` queries with a :method:`~cursor.sort()`, MongoDB can use indexes that support the :query:`$or` clauses.

### `$or` and Partial Indexes

You can create `partial indexes <index-type-partial>` with :query:`$or`. Use the `partialFilterExpression` of the `db.collection.createIndex() <method-createIndex>` method to create a partial index.

### `$or` Compared to `$in`

If you use :query:`$or` with `<expressions>` that are equality checks for the value of the same field, use :query:`$in` instead of :query:`$or`.

This query selects documents in the `movies` collection where `year` is `1903` or `1909`:

### Nested `$or` Clauses

You can nest :query:`$or` operations.

> **Seealso:** - :query:`$and`
- :method:`~db.collection.find()`
- :method:`~cursor.sort()`
- :query:`$in`

### Error Handling

.. include:: /includes/and-or-behavior.rst
