---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/inc.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# $inc (update operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :update:`$inc` operator has the following form:

```javascript
{ $inc: { <field1>: <amount1>, <field2>: <amount2>, ... } }
```

.. include:: /includes/use-dot-notation.rst

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

The :update:`$inc` operator accepts positive and negative values.

If the field does not exist, :update:`$inc` creates the field and sets the field to the specified value.

Using the :update:`$inc` operator on a field with a null value generates an error.

:update:`$inc` is an atomic operation within a single document.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-inc.rst

## Example

Create the `products` collection:

```javascript
db.products.insertOne(
   {
     _id: 1,
     sku: "abc123",
     quantity: 10,
     metrics: { orders: 2, ratings: 3.5 }
   }
)
```

The following :method:`~db.collection.updateOne()` operation uses the :update:`$inc` operator to:

- increase the `"metrics.orders"` field by 1
- increase the `quantity` field by -2 (which decreases `quantity`)
```javascript
db.products.updateOne(
   { sku: "abc123" },
   { $inc: { quantity: -2, "metrics.orders": 1 } }
)
```

The operation returns the following result:

```javascript
{
  _id: 1,
  sku: 'abc123',
  quantity: 8,
  metrics: { orders: 3, ratings: 3.5 }
}
```

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
