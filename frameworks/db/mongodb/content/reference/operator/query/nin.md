---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/nin.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $nin (query predicate operator)

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :query:`$nin` operator has the following form:

```javascript
{ field: { $nin: [ <value1>, <value2> ... <valueN> ] } }
```

If `field` has an array, the :query:`$nin` operator selects the documents whose `field` has an array with **no** element equal to a value in the specified array. For example, `<value1>`, `<value2>`, and so on.

.. include:: /includes/fact-comparison-order.rst

## Examples

.. include:: /includes/sample-data-usage.rst

### Select on Unmatching Documents

The following example returns movies where `runtime` is greater than `1000` minutes and `rated` is not in `[ "G", "PG" ]`. Because `$nin` also matches documents that don't contain the `rated` field, the query returns movies even when the rating data is unavailable:

### Select on Elements Not in an Array

The following example sets the `exclude` field to `true` for movies that don't have `"Drama"` in their `genres` array:

:method:`~db.collection.updateMany()` also selects a document when the document does not contain the field :query:`$nin` is matching on.

.. include:: /includes/extracts/nin_operators_selectivity.rst

## Learn More

- :method:`~db.collection.find()`
- :method:`~db.collection.updateMany()`
- :update:`$set`
