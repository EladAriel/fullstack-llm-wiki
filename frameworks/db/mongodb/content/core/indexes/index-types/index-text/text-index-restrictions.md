---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/text-index-restrictions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================================

# Text Index Restrictions on Self-Managed Deployments

.. include:: /includes/fact-fts-avs-text-index.rst

Text indexes have these restrictions:

## One Text Index per Collection

.. include:: /includes/fact-text-index-limit-one.rst

## $text Queries and Hints

.. include:: /includes/fact-hint-text-query-restriction.rst

## $text Queries and Multi-Word Strings

.. include:: /includes/fact-text-search-multiword-and-term.rst

For examples of `$text` queries with multi-word strings, see `text-operator-exact-string`.

## Text Index and Sort

Text indexes cannot improve performance for sort operations. This restriction applies to both single-field and compound text indexes.

## Compound Text Index

A `compound index <index-type-compound>` can include a text index key in combination with ascending and descending index keys. However, compound text indexes have these restrictions:

.. include:: /includes/fact-compound-index-with-text-restrictions.rst

For examples of compound text indexes, see these pages:

- `compound-text-index-example`
- `limit-entries-scanned`
## Collation Option

Text indexes only support binary comparison, and do not support the `collation <collation>` option. Binary comparison compares the numeric Unicode value of each character in each string, and does not account for letter case or accent marks.

To create a text index on a collection that has a non-simple collation, you must explicitly specify `{ collation: { locale: "simple" } }` when you create the index.

For example, consider a collection named `collationTest` with a collation of `{ locale: "en" }`:

```javascript
db.createCollection(
   "collationTest",
   {
      collation: { locale: "en" }
   }
)
```

To create a text index on the `collationTest` collection, you must specify `{ collation: { locale: "simple" } }`. The following command creates a text index on the `quotes` field:

```javascript
db.collationTest.createIndex(
   {
      quotes: "text"
   },
   {
      collation: { locale: "simple" }
   }
)
```
