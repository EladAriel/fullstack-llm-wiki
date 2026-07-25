---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/lt.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# $lt (query predicate operator)

## Definition

## Examples

The following examples use the `inventory` collection. Create the collection:

.. include:: /includes/examples-create-inventory.rst

### Match Document Fields

Select all documents in the `inventory` collection where `quantity` is less than `20`:

```javascript
db.inventory.find( { quantity: { $lt: 20 } } )
```

Example output:

```javascript
{
  _id: ObjectId("61ba634dfe687fce2f04241f"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 }
}
```

### Perform an Update Based on Embedded Document Fields

The following example sets the `price` field based on a :query:`$lt` comparison against a field in an embedded document.

```javascript
db.inventory.updateMany( { "carrier.fee": { $lt: 20 } }, { $set: { price: 9.99 } } )
```

Example output:

```javascript
{
  _id: ObjectId("61ba634dfe687fce2f04241d"),
  item: 'nuts',
  quantity: 30,
  carrier: { name: 'Shipit', fee: 3 },
  price: 9.99
},
{
  _id: ObjectId("61ba634dfe687fce2f04241e"),
  item: 'bolts',
  quantity: 50,
  carrier: { name: 'Shipit', fee: 4 },
  price: 9.99
},
{
  _id: ObjectId("61ba634dfe687fce2f04241f"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 },
  price: 9.99
}
```

This :method:`~db.collection.updateMany()` operation searches for an embedded document, `carrier`, with a subfield named `fee`. It sets `{ price: 9.99 }` in each document where `fee` has a value less than 20.

To set the value of the `price` field in only the first document where `carrier.fee` is less than 20, use :method:`~db.collection.updateOne()`.

> **Seealso:** - :method:`~db.collection.find()`
- :update:`$set`
