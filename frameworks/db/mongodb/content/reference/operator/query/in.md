---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/in.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $in (query predicate operator)

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The `$in` operator has the following form:

```javascript
{ field: { $in: [ <value1>, <value2>, ... <valueN> ] } }
```

.. include:: /includes/fact-comparison-order.rst

If `field` has an array, the `$in` operator selects the documents whose `field` has an array that contains at least one element that matches a value in the specified array. For example, `<value1>`, `<value2>`, and so on.

`$in` compares each parameter to each document in the collection, which can cause performance issues. To improve performance, create an index on the `field` you want to query. An index allows MongoDB to create bounds for each `$in` element and search more efficiently.

> **Note:** This document describes the `$in` query operator.
For the `$in` aggregation operator, see
`/reference/operator/aggregation/in`.

## Query Data on Atlas by Using {+fts+}

.. include:: /includes/fact-atlas-search-operator.rst

## Examples

.. include:: /includes/sample-data-usage.rst

### Match Values

This query selects documents in the `movies` collection where the value of the `rated` field is `"G"` or `"TV-G"`:

Although you can write the query using the :query:`$or` operator, use the `$in` operator rather than the :query:`$or` operator when performing equality checks on the same field.

### Match Values in an Array

The following :method:`~db.collection.updateMany()` operation sets the `familyFriendly` field to `true` when the `rated` array has at least one element that matches either `"G"` or `"TV-G"`:

.. include:: /includes/arrays-additional-examples.rst

### Use `$in` with a Regular Expression

The `$in` operator can select documents using regular expressions of the form `/pattern/`.

This query selects documents in the `movies` collection where the `plot` field either starts with `Alien` or contains `sci-fi`:

## Learn More

- :method:`~db.collection.find()`
- :method:`~db.collection.updateMany()`
- :query:`$or`
- :update:`$set`
- :query:`$elemMatch`
