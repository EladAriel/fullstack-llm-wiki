---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/exists.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $exists (query predicate operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

.. include:: /includes/reference/exist-op-support-expressions.rst

## Syntax

To specify an :query:`$exists` expression, use the following prototype:

```javascript
{ field: { $exists: <boolean> } }
```

When `<boolean>` is true, :query:`$exists` matches the documents that contain the field, including documents where the field value is `null`. If `<boolean>` is false, the query returns only the documents that do not contain the field.

## Query Data on Atlas by Using {+fts+}

.. include:: /includes/fact-atlas-search-operator.rst

## Examples

.. include:: /includes/sample-data-usage.rst

### Exists and Not Equal To

Consider the following example:

This query selects 5 documents in the `movies` collection where the `rated` field exists and its value does not equal `"R"` or `"PG-13"`.

### Null Values

The `movies` collection in the `sample_mflix` database contains documents where some fields are present and others are missing. For example, the `rated` field exists in 11,455 documents and is absent from the remaining 9,894 documents.

#### `$exists: true`

The following query specifies the query predicate `rated: { $exists: true }`:

The results consist of three documents that contain the field `rated`:

#### `$exists: false`

The following query specifies the query predicate `rated: { $exists: false }`:

The results consist of three documents that do not contain the field `rated`:

### Use a Sparse Index to Improve `$exists` Performance

The following table compares `$exists` query performance using sparse and non-sparse indexes:

Queries that use `{ $exists: true }` on fields that use a non-sparse index or that use `{ $exists: true }` on fields that are not indexed examine all documents in a collection. To improve performance, create a `sparse index <index-type-sparse>` on the `field` as shown in the following scenario:

#. The `movies` collection contains documents where the `metacritic` field is present in some documents and absent from others. Of the 21,349 documents, 6,964 have the `metacritic` field and 14,385 do not.

#. Create a `sparse index <index-type-sparse>` on the `metacritic` field:

#. The following example counts the documents where the `metacritic` field has a value (including null) and uses the `sparse index <index-type-sparse>`:

> **Tip:** If you only need documents where the `field` has a non-null value,
you:
- Can use `$ne: null` instead of `$exists: true`.
- Do not need a `sparse index <index-type-sparse>` on the
  `field`.
For example, using the `movies` collection:
.. literalinclude:: /code-examples/tested/command-line/mongosh/aggregation/expressions/exists/metracritic-2.snippet.ne-null.js
   :language: javascript
   :category: usage example
The example returns 6964. Documents that are missing the
`metacritic` value or have a null `metacritic` value are not
counted.

## Learn More

- `faq-developers-query-for-nulls`
- :query:`$nin`
- :query:`$in`
