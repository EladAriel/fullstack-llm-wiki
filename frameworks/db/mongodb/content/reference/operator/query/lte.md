---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/lte.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================

# $lte (query predicate operator)

## Definition

## Examples

The following examples use the `inventory` collection. Create the collection:

.. include:: /includes/examples-create-inventory.rst

### Match Document Fields

Consider the following example:

```javascript
db.inventory.find( { quantity: { $lte: 20 } } )
```

This query will select all documents in the `inventory` collection where the `quantity` field value is less than or equal to `20`.

Example output:

```javascript
{
  _id: ObjectId("61ba453ffe687fce2f04241c"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 }
}
```

### Perform an Update Based on Embedded Document Fields

The following example sets the `price` field based on a :query:`$lte` comparison against a field in an embedded document.

```javascript
db.inventory.updateMany(
   { "carrier.fee": { $lte: 5 } }, { $set: { price: 9.99 } }
)
```

Example output:

```javascript
{
  _id: ObjectId("61ba453ffe687fce2f04241a"),
  item: 'nuts',
  quantity: 30,
  carrier: { name: 'Shipit', fee: 3 },
  price: 9.99
},
{
  _id: ObjectId("61ba453ffe687fce2f04241b"),
  item: 'bolts',
  quantity: 50,
  carrier: { name: 'Shipit', fee: 4 },
  price: 9.99
},
{
  _id: ObjectId("61ba453ffe687fce2f04241c"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 },
  price: 9.99
}
```

This :method:`~db.collection.updateMany()` operation searches for an embedded document, `carrier`, with a subfield named `fee`. It sets `{ price: 9.99 }` in each document where `fee` has a value less than or equal to 5.

To set the value of the `price` field in only the first document where `carrier.fee` is less than or equal to 5, use :method:`~db.collection.updateOne()`.

> **Seealso:** - :method:`~db.collection.find()`
- :update:`$set`
