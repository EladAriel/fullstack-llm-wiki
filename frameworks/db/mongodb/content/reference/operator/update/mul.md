---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/mul.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# $mul (update operator)

## Definition

## Behavior

.. include:: /includes/extracts/update-operation-empty-operand-expressions-mul.rst

.. include:: /includes/fact-update-operator-processing-order.rst

### Missing Field

If the field does not exist in a document, :update:`$mul` creates the field and sets the value to zero of the same numeric type as the multiplier.

### Atomic

:update:`$mul` is an atomic operation within a single document.

### Mixed Type

Multiplication with values of mixed numeric types (32-bit integer, 64-bit integer, Double, Decimal128) may result in conversion of numeric type. For multiplication with values of mixed numeric types, the following type conversion rules apply:

> **Note:** - If the product of two 32-bit integers exceeds the maximum value
  for a 32-bit integer, the result is a 64-bit integer.
- Integer operations of any type that exceed the maximum value for a
  64-bit integer produce an error.

## Examples

### Multiply the Value of a Field

Create the `products` collection:

```javascript
db.products.insertOne(
   { "_id" : 1, "item" : "Hats", "price" : Decimal128("10.99"), "quantity" : 25 }
)
```

In the following operation, :method:`db.collection.updateOne()` updates the document. The :update:`$mul` operator multiplies the `price` field by `1.25` and the `quantity` field by `2`:

```javascript
db.products.updateOne(
   { _id: 1 },
   { $mul: 
      {
         price: Decimal128( "1.25" ),
         quantity: 2
       }
   }
)
```

In the updated document:

- `price` is the original value, 10.99, multiplied by 1.25
- `quantity` is the original value, 25, multiplied by 2
```javascript
 { _id: 1, item: 'Hats', price: Decimal128("13.7375"), quantity: 50 }
```

### Apply `$mul` Operator to a Non-existing Field

Add the following document to the `products` collection:

```javascript
db.products.insertOne( { _id: 2,  item: "Unknown" } )
```

In the following operation, :method:`db.collection.updateOne()` attempts to apply the :update:`$mul` operator to a field that is not in the document:

```javascript
db.products.updateOne(
   { _id: 2 },
   { $mul: { price: Decimal128("100") } }
)
```

The :method:`db.collection.updateOne()` operation

- inserts the `price` field
- sets  Decimal128("0")
```javascript
{ "_id" : 2, "item" : "Unknown", "price" : Long(0) }
```

The `price` field has the same type, Decimal128, as the multiplier.

### Multiply Mixed Numeric Types

Add the following document to the `products` collection:

```javascript
db.products.insertOne( { _id: 3,  item: "Scarf", price: Decimal128("10") } )
```

In the following operation, :method:`db.collection.updateOne()` uses the :update:`$mul` operator to multiply the value in the `price` field `Decimal128(10) <shell-type-decimal>` by `Int32(5) <shell-type-int>`:

```javascript
db.products.updateOne(
   { _id: 3 },
   { $mul: { price: Int32(5) } }
)
```

The operation results in the following document:

```javascript
{ _id: 3, item: 'Scarf', price: Decimal128("50") }
```

The value in the `price` field is of type `Decimal128 <shell-type-decimal>`. See `Multiplication Type Conversion Rules <multiplication-type-conversion>` for details.

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
