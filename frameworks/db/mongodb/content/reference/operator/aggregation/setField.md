---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/setField.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $setField  (expression operator)

## Definition

## Syntax

:expression:`$setField` has the following syntax:

```javascript
{ 
  $setField: {
    field: <String>,
    input: <Object>,
    value: <Expression>
  }
}
```

You must provide the following fields:

## Behavior

- If `input` evaluates to `missing`, `undefined`, or `null`,
:expression:`$setField` returns `null` and does not update `input`.

- If `input` evaluates to anything other than an object, `missing`,
`undefined`, or `null`, :expression:`$setField` returns an error.

- If `field` resolves to anything other than a string constant,
:expression:`$setField` returns an error.

- If `field` doesn't exist in `input`, :expression:`$setField`
adds it.

- :expression:`$setField` doesn't implicitly traverse objects or
arrays. For example, :expression:`$setField` evaluates a `field` value of `"a.b.c"` as a top-level field `"a.b.c"` instead of as a nested field, `{ "a": { "b": { "c": } } }`.

- :expression:`$unsetField` is an alias for :expression:`$setField`
with an input value of `$$REMOVE`.  The following expressions are equivalent:

```javascript
  {
     $setField: {
        field: <field name>, 
        input: "$$ROOT",
        value: "$$REMOVE"
     }
  }

  {
     $unsetField: {
        field: <field name>, 
        input: "$$ROOT"
     }
  }
```

.. seealso :

```
:ref:`Considerations for field names <crud-concepts-dot-dollar-considerations>`
```

## Examples

### Add Fields that Contain Periods (`.`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: "sweatshirt", price: 45.99, qty: 300 },
   { _id: 2, item: "winter coat", price: 499.99, qty: 200 },
   { _id: 3, item: "sun dress", price: 199.99, qty: 250 },
   { _id: 4, item: "leather boots", price: 249.99, qty: 300 },
   { _id: 5, item: "bow tie", price: 9.99, qty: 180 }
] )
```

The following operation uses the :pipeline:`$replaceWith` pipeline stage and the :expression:`$setField` operator to add a new field to each document, `"price.usd"`. The value of `"price.usd"` will equal the value of `"price"` in each document. Finally, the operation uses the :pipeline:`$unset` pipeline stage to remove the `"price"` field.

```javascript
db.inventory.aggregate( [ 
   { $replaceWith: {
        $setField: { 
           field: "price.usd",
           input: "$$ROOT", 
           value: "$price" 
   } } },
   { $unset: "price" }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 1, item: 'sweatshirt', qty: 300, 'price.usd': 45.99 },
  { _id: 2, item: 'winter coat', qty: 200, 'price.usd': 499.99 },
  { _id: 3, item: 'sun dress', qty: 250, 'price.usd': 199.99 },
  { _id: 4, item: 'leather boots', qty: 300, 'price.usd': 249.99 },
  { _id: 5, item: 'bow tie', qty: 180, 'price.usd': 9.99 }
]
```

### Add Fields that Start with a Dollar Sign (`$`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: "sweatshirt", price: 45.99, qty: 300 },
   { _id: 2, item: "winter coat", price: 499.99, qty: 200 },
   { _id: 3, item: "sun dress", price: 199.99, qty: 250 },
   { _id: 4, item: "leather boots", price: 249.99, qty: 300 },
   { _id: 5, item: "bow tie", price: 9.99, qty: 180 }
] )
```

The following operation uses the :pipeline:`$replaceWith` pipeline stage and the :expression:`$setField` and :expression:`$literal` operators to add a new field to each document, `"$price"`. The value of `"$price"` will equal the value of `"price"` in each document. Finally, the operation uses the :pipeline:`$unset` pipeline stage to remove the `"price"` field.

```javascript
db.inventory.aggregate( [
   { $replaceWith: {
        $setField: { 
           field: { $literal: "$price" },
           input: "$$ROOT", 
           value: "$price" 
   } } },
   { $unset: "price" }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 1, item: 'sweatshirt', qty: 300, '$price': 45.99 },
  { _id: 2, item: 'winter coat', qty: 200, '$price': 499.99 },
  { _id: 3, item: 'sun dress', qty: 250, '$price': 199.99 },
  { _id: 4, item: 'leather boots', qty: 300, '$price': 249.99 },
  { _id: 5, item: 'bow tie', qty: 180, '$price': 9.99 }
]
```

### Update Fields that Contain Periods (`.`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: 'sweatshirt', qty: 300, 'price.usd': 45.99 },
   { _id: 2, item: 'winter coat', qty: 200, 'price.usd': 499.99 },
   { _id: 3, item: 'sun dress', qty: 250, 'price.usd': 199.99 },
   { _id: 4, item: 'leather boots', qty: 300, 'price.usd': 249.99 },
   { _id: 5, item: 'bow tie', qty: 180, 'price.usd': 9.99 }
] )
```

The following operation uses the :pipeline:`$match` pipeline stage to find a specific document and the :pipeline:`$replaceWith` pipeline stage and the :expression:`$setField` operator to update the `"price.usd"` field in the matching document:

```javascript
db.inventory.aggregate( [ 
   { $match: { _id: 1 } }, 
   { $replaceWith: { 
        $setField: { 
           field: "price.usd", 
           input: "$$ROOT", 
           value: 49.99 
    } } }
] )
```

The operation returns the following results:

```javascript
[ 
  { _id: 1, item: 'sweatshirt', qty: 300, 'price.usd': 49.99 } 
]
```

### Update Fields that Start with a Dollar Sign (`$`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany([ 
   { _id: 1, item: 'sweatshirt', qty: 300, '$price': 45.99 },
   { _id: 2, item: 'winter coat', qty: 200, '$price': 499.99 },
   { _id: 3, item: 'sun dress', qty: 250, '$price': 199.99 },
   { _id: 4, item: 'leather boots', qty: 300, '$price': 249.99 },
   { _id: 5, item: 'bow tie', qty: 180, '$price': 9.99 }
] )
```

The following operation uses the :pipeline:`$match` pipeline stage to find a specific document and the :pipeline:`$replaceWith` pipeline stage and the :expression:`$setField` and :expression:`$literal` operators to update the `"$price"` field in the matching document:

```javascript
db.inventory.aggregate( [ 
   { $match: { _id: 1 } }, 
   { $replaceWith: { 
        $setField: { 
           field: { $literal: "$price" }, 
           input: "$$ROOT", 
           value: 49.99 
   } } }
] )
```

The operation returns the following results:

```javascript
[ 
  { _id: 1, item: 'sweatshirt', qty: 300, '$price': 49.99 } 
]
```

### Remove Fields that Contain Periods (`.`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany([ 
   { _id: 1, item: 'sweatshirt', qty: 300, 'price.usd': 45.99 },
   { _id: 2, item: 'winter coat', qty: 200, 'price.usd': 499.99 },
   { _id: 3, item: 'sun dress', qty: 250, 'price.usd': 199.99 },
   { _id: 4, item: 'leather boots', qty: 300, 'price.usd': 249.99 },
   { _id: 5, item: 'bow tie', qty: 180, 'price.usd': 9.99 }
] )
```

The following operation uses the :pipeline:`$replaceWith` pipeline stage and the :expression:`$setField` operator and :variable:`$$REMOVE <REMOVE>` to remove the `"price.usd"` field from each document:

```javascript
db.inventory.aggregate( [
   { $replaceWith:  {
        $setField: { 
           field: "price.usd",
           input: "$$ROOT", 
           value: "$$REMOVE" 
   } } }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 1, item: 'sweatshirt', qty: 300 },
  { _id: 2, item: 'winter coat', qty: 200 },
  { _id: 3, item: 'sun dress', qty: 250 },
  { _id: 4, item: 'leather boots', qty: 300 },
  { _id: 5, item: 'bow tie', qty: 180 }
]
```

A similar query written using the :expression:`$unsetField` alias returns the same results:

```javascript
db.inventory.aggregate( [
   { $replaceWith:  {
        $unsetField: { 
           field: "price.usd",
           input: "$$ROOT" 
   } } }
] )
```

### Remove Fields that Start with a Dollar Sign (`$`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: 'sweatshirt', qty: 300, '$price': 45.99 },
   { _id: 2, item: 'winter coat', qty: 200, '$price': 499.99 },
   { _id: 3, item: 'sun dress', qty: 250, '$price': 199.99 },
   { _id: 4, item: 'leather boots', qty: 300, '$price': 249.99 },
   { _id: 5, item: 'bow tie', qty: 180, '$price': 9.99 }
] )
```

The following operation uses the :pipeline:`$replaceWith` pipeline stage, the :expression:`$setField` and :expression:`$literal` operators, and :variable:`$$REMOVE <REMOVE>` to remove the `"$price"` field from each document:

```javascript
db.inventory.aggregate( [
   { $replaceWith: {
        $setField: { 
           field: { $literal: "$price" },
           input: "$$ROOT", 
           value: "$$REMOVE" 
   } } }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 1, item: 'sweatshirt', qty: 300 },
  { _id: 2, item: 'winter coat', qty: 200 },
  { _id: 3, item: 'sun dress', qty: 250 },
  { _id: 4, item: 'leather boots', qty: 300 },
  { _id: 5, item: 'bow tie', qty: 180 }
]
```

A similar query written using the :expression:`$unsetField` alias returns the same results:

```javascript
db.inventory.aggregate( [
  { $replaceWith: {
       $unsetField: { 
          field: { $literal: "$price" },
          input: "$$ROOT"
  } } }
] )
```

> **Seealso:** :expression:`$unsetField`
