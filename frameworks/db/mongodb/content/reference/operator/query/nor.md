---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/nor.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $nor (query predicate operator)

## Definition

## Examples

### `$nor` Query with Two Expressions

Consider the following query which uses only the :query:`$nor` operator:

```javascript
db.inventory.find( { $nor: [ { price: 1.99 }, { sale: true } ]  } )
```

This query will return all documents that:

- contain the `price` field whose value is not equal to `1.99`
and contain the `sale` field whose value is not equal to `true` **or**

- contain the `price` field whose value is not equal to `1.99`
but do not contain the `sale` field **or**

- do not contain the `price` field but contain the `sale`
field whose value is not equal to `true` **or**

- do not contain the `price` field and do not contain the
`sale` field

### `$nor` and Additional Comparisons

Consider the following query:

```javascript
db.inventory.find( { $nor: [ { price: 1.99 }, { qty: { $lt: 20 } }, { sale: true } ] } )
```

This query will select all documents in the `inventory` collection where:

- the `price` field value does not equal `1.99` **and**
- the `qty` field value is not less than `20` **and**
- the `sale` field value is not equal to `true`
including those documents that do not contain these field(s).

The exception in returning documents that do not contain the field in the :query:`$nor` expression is when the :query:`$nor` operator is used with the :query:`$exists` operator.

### `$nor` and `$exists`

Compare that with the following query which uses the :query:`$nor` operator with the :query:`$exists` operator:

```javascript
db.inventory.find( { $nor: [ { price: 1.99 }, { price: { $exists: false } },
                             { sale: true }, { sale: { $exists: false } } ] } )
```

This query will return all documents that:

- contain the `price` field whose value is not equal to `1.99`
and contain the `sale` field whose value is not equal to `true`

> **Seealso:** - :method:`~db.collection.find()`
- :query:`$or`
- :update:`$set`
- :query:`$exists`
