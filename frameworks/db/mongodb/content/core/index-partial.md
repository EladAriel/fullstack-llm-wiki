---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/index-partial.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Partial Indexes

Partial indexes only index the documents in a collection that meet a specified filter expression. Partial indexes have lower storage requirements and reduced performance costs for index creation and maintenance.

## Create a Partial Index

To create a `partial` index, use the :method:`db.collection.createIndex()` method with the `partialFilterExpression` option. The `partialFilterExpression` option accepts a document that specifies the filter condition using:

.. include:: /includes/fact-partial-filter-expression-operators.rst

For example, the following operation creates a compound index that indexes only the documents where the `genre` field is `Drama`:

You can specify a `partialFilterExpression` option for all MongoDB `index types <index-types>`. When specifying a `partialFilterExpression` for a TTL index on a time series collection, you can only filter on the collection `metaField`.

> **Seealso:** To learn how to manage indexes in |compass|, see
`manage-indexes`.

## Behavior

### Query Coverage

MongoDB does not use the partial index for a query or sort operation if using the index results in an incomplete result set.

To use the partial index, a query must contain the filter expression (or a modified filter expression that specifies a subset of the filter expression) as part of its query condition.

For example, given the following index:

The following query can use the index since the query predicate includes the condition `password: { $exists: true }` that matches documents matched by the index filter expression `password: { $exists: true }`:

However, the following query cannot use the partial index on the `name` field because using the index results in an incomplete result set. Specifically, the query predicate includes the condition `password: { $exists: false }` while the index has the filter `password: { $exists: true }`. That is, the query `{ name: "Ned Stark", password: { $exists: false } }` matches more documents (users without passwords) than the index covers.

Similarly, the following query cannot use the partial index because the query predicate does not include the filter expression and using the index would return an incomplete result set.

### Comparison with Sparse Indexes

Use partial indexes instead of `sparse indexes <index-type-sparse>` for more precise control over which documents to index:

- Sparse indexes include or exclude documents solely based on the presence of
the indexed field (or multiple fields, for sparse compound indexes).

- Partial indexes include or exclude documents based on the filter expression.
The expression can include fields other than index keys, and can specify conditions other than a field existing.

For example, a partial index can implement the same behavior as a sparse index. This partial index supports the same queries as a sparse index on the `name` field:

However, a partial index can also filter on fields other than the index key. For example, a partial index on the `name` field can check for the existence of the `email` field:

For the query optimizer to choose this partial index, the query predicate must include a condition on the `name` field as well as a non-null match on the `email` field.

For example, the following query can use the index because it includes both a condition on the `name` field and a non-null match on the `email` field:

However, the following query cannot use the index because it includes a null match on the `email` field, which is not permitted by the filter expression `{ email: { $exists: true } }`:

### Partial TTL Indexes

Partial indexes can also be TTL indexes. Partial TTL indexes match the specified filter expression and expire only those documents. For details, see `partial-ttl-index-example`.

## Restrictions

- You cannot specify both the `partialFilterExpression` option and
the `sparse` option.

- `_id` indexes cannot be partial indexes.
- Shard key indexes cannot be partial indexes.
- .. include:: /includes/queryable-encryption/qe-csfle-partial-filter-disclaimer.rst
### Equivalent Indexes

.. include:: /includes/indexes/equivalent-indexes.rst

For example, you can't create two indexes that only differ in the text case in the partial filter expression.

## Examples

.. include:: /includes/sample-data-usage.rst

### Create a Partial Index On A Collection

The following example adds a partial index on the `title` and `genres` fields. The operation only indexes documents where the `rating` field is `PG`:

The following query on the `movies` collection uses the partial index to return the writers of the all movies titled "The Three Musketeers":

However, the following query cannot use the partial index because the query predicate does not include the `rating` filter:

### Partial Index with Unique Constraint

Partial indexes only index the documents in a collection that meet a specified filter expression. If you specify both the `partialFilterExpression` and a `unique constraint <index-type-unique>`, the unique constraint only applies to the documents that meet the filter expression. A partial index with a unique constraint does not prevent the insertion of documents that do not meet the unique constraint if the documents do not meet the filter criteria.

The following operation on the `users` collection creates an index that specifies a `unique constraint <index-type-unique>` on the `email` field and a partial filter expression `password: { $exists: true }`.

The index prevents the insertion of documents that have both an email address that already exists in the collection and an existing `password` field.

However, the following documents with duplicate email addresses are allowed since the unique constraint only applies to documents with a `password` The index prevents inserting a document if it has a password and its email address already exists in the collection. However, since the unique `email` constraint only applies to documents with a `password` field, you can still insert documents with duplicate email addresses if they have no password:
