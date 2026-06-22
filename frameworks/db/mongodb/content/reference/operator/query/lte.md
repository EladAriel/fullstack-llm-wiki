---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/lte.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
