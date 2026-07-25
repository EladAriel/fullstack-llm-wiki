---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/size.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# $size (query predicate operator)

## Compatibility

.. include:: /includes/fact-compatibility.rst

Consider the following examples:

```javascript
db.collection.find( { field: { $size: 2 } } );
```

This query returns all documents in `collection` where `field` is an array with 2 elements. For example, the query returns `{ field: [ red, green ] }` and `{ field: [ apple, lime ] }` but not `{ field: fruit }` or `{ field: [ orange, lemon, grapefruit ] }`. To match fields with only one element within an array use :query:`$size` with a value of 1, as follows:

```javascript
db.collection.find( { field: { $size: 1 } } );
```

:query:`$size` does not accept ranges of values. To select documents based on fields with different numbers of elements, create a counter field that you increment when you add elements to a field.

Queries cannot use indexes for the :query:`$size` portion of a query, although the other portions of a query can use indexes if applicable.

## Syntax

A `$size` expression has the following syntax:

```javascript
{
   <field>: {
      $size: <number>
   }
}
```

## Additional Examples

.. include:: /includes/arrays-additional-examples.rst

> **Seealso:** :method:`db.collection.find()`
