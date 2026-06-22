---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/gt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $gt (query predicate operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The `$gt` operator has this form:

```javascript
{ field: { $gt: value } }
```

## Examples

.. include:: /includes/sample-data-usage.rst

### Match Document Fields

This example selects documents in the `movies` collection where `runtime` is greater than `1000` minutes:

### Perform an Update Based on Embedded Document Fields

This :method:`~db.collection.updateMany()` operation matches an embedded document named `imdb`, with a subfield named `rating`. The operation sets `{ highestRated: true }` in documents where `rating` is greater than `9.5`.

## Learn More

- :method:`~db.collection.find()`
- :update:`$set`
- :method:`~db.collection.updateMany()`
