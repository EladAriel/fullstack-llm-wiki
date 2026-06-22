---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/not.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $not (query predicate operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :query:`$not` operator has the following form:

```javascript
{ field: { $not: { <operator-expression> } } }
```

Consider the following example:

```javascript
db.movies.find( { runtime: { $not: { $gt: 180 } } } )
```

The example selects all documents in the `movies` collection where:

- the `runtime` field value is less than or equal to `180` **or**
- the `runtime` field does not exist
`{ $not: { $gt: 180 } }` differs from the :query:`$lte` operator. `{ $lte: 180 }` returns only the documents where the `runtime` field exists and its value is less than or equal to `180`.

Use the `$not` operator with another operator expression. To use `$not` for an inequality check, use:

```javascript
{ runtime: { $not: { $eq: 120 } } }
```

The preceding query is equivalent to:

```javascript
{ runtime: { $ne: 120 } }
```

The following query is invalid because it compares a field without an operator:

```javascript
{ runtime: { $not: 120 } }
```

## Behavior

### Arrays

The `$not` operator can yield unexpected results when used with an array. To match documents based on multiple false conditions, use :query:`$nor`.

### Regular Expressions

.. include:: /includes/sample-data-usage.rst

:query:`$not` supports logical `NOT` operations on:

- Regular expression objects, such as `/pattern/`.
The following example returns movies where `runtime` is greater than `1000` minutes and `title` does not start with the letter `T`. Because `$not` also matches documents that don't contain the `title` field, the query returns movies even when title data is unavailable:

- :query:`$regex` operator expressions.
The following two queries return movies where `runtime` is greater than `1000` minutes and `title` does not start with the letter `T`. The first query passes a string to `$regex`:

- Driver language regular expression objects.
For example, the following [PyMongo](https://pymongo.readthedocs.io/en/stable/index.html)_ query uses Python's `re.compile()` method to compile a regular expression:

```python
  import re
  for noMatch in db.inventory.find( { "item": { "$not": re.compile("^p.*") } } ):
      print noMatch
```

## Learn More

- :method:`~db.collection.find()`
- :update:`$set`
- :query:`$gt`
- :query:`$regex`
- :query:`$eq`
