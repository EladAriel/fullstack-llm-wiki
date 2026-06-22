---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/getField.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $getField (expression operator)

## Definition

## Syntax

:expression:`$getField` has the following syntax:

```javascript
{ 
  $getField: {
    field: <String>,
    input: <Object> 
  }
}
```

:expression:`$getField` has the following shorthand syntax for retrieving field values from :variable:`$$CURRENT <CURRENT>`:

```javascript
{ 
  $getField: <String>
}
```

For this syntax, the argument is equivalent to the value of `field` described above.

## Behavior

- If the `field` that you specify is not present in the `input`
object, or in :variable:`$$CURRENT <CURRENT>` if you don't specify an `input` object, :expression:`$getField` returns `missing`.

- If `input` evaluates to `missing`, `undefined`, or `null`,
:expression:`$getField` returns `null`.

- If `input` evaluates to anything other than an object, `missing`,
`undefined`, or `null`, :expression:`$getField` returns an error.

- :expression:`$getField` doesn't implicitly traverse objects or arrays.
For example, :expression:`$getField` evaluates a `field` value of `a.b.c` as a top-level field `a.b.c` instead of a nested field `{ a: { b: { c: } } }`.

.. seealso :

```
:ref:`Considerations for field names <crud-concepts-dot-dollar-considerations>`
```

## Examples

### Query Fields that Contain Periods (`.`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "sweatshirt", "price.usd": 45.99, qty: 300 },
   { _id: 2, item: "winter coat", "price.usd": 499.99, qty: 200 },
   { _id: 3, item: "sun dress", "price.usd": 199.99, qty: 250 },
   { _id: 4, item: "leather boots", "price.usd": 249.99, qty: 300 },
   { _id: 5, item: "bow tie", "price.usd": 9.99, qty: 180 }
] )
```

The following operation uses the :expression:`$getField` and :expression:`$gt` operators to find which products have a `price.usd` greater than `200`:

```javascript
db.inventory.aggregate( [
  {
    $match: 
      { $expr: 
        { $gt: [ { $getField: "price.usd" }, 200 ] }
      }
   }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 2, item: 'winter coat', qty: 200, 'price.usd': 499.99 },
  { _id: 4, item: 'leather boots', qty: 300, 'price.usd': 249.99 }
]
```

### Query Fields that Start with a Dollar Sign (`$`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: "sweatshirt", "$price": 45.99, qty: 300 },
   { _id: 2, item: "winter coat", "$price": 499.99, qty: 200 },
   { _id: 3, item: "sun dress", "$price": 199.99, qty: 250 },
   { _id: 4, item: "leather boots", "$price": 249.99, qty: 300 },
   { _id: 5, item: "bow tie", "$price": 9.99, qty: 180 }
] )
```

The following operation uses the :expression:`$getField`, :expression:`$gt`, and :expression:`$literal` operators to find which products have a `$price` greater than `200`:

```javascript
db.inventory.aggregate( [
  {
    $match: 
      { $expr: 
        { $gt: [ { $getField: {$literal: "$price" } }, 200 ] }
      }
   }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 2, item: 'winter coat', qty: 200, '$price': 499.99 },
  { _id: 4, item: 'leather boots', qty: 300, '$price': 249.99 }
]
```

### Query a Field in a Sub-document

Create an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "sweatshirt",  "price.usd": 45.99,
     quantity: { "$large": 50, "$medium": 50, "$small": 25 }
   }, 
   { _id: 2, item: "winter coat", "price.usd": 499.99,
     quantity: { "$large": 35, "$medium": 35, "$small": 35 }
   },
   { _id: 3, item: "sun dress", "price.usd": 199.99,
     quantity: { "$large": 45, "$medium": 40, "$small": 5 }
   },
   { _id: 4, item: "leather boots", "price.usd": 249.99,
     quantity: { "$large": 20, "$medium": 30, "$small": 40 }
   },
   { _id: 5, item: "bow tie", "price.usd": 9.99,
     quantity: { "$large": 0, "$medium": 10, "$small": 75 }
   }
] )
```

The following operation returns documents where the number of `$small` items is less than or equal to `20`.

```javascript
db.inventory.aggregate( [
   { $match: 
      { $expr:
         { $lte:
            [
               { $getField: 
                  { field: { $literal: "$small" },
                    input: "$quantity"
                  }
               },
               20
            ]
         }
      }
   }
] )
```

Use these operators to query the collection:

- The :expression:`$lte` operator finds values less than or equal to
20.

- :expression:`$getField` requires explicit `field` and `input`
parameters because the `$small` field is part of a sub-document.

- :expression:`$getField` uses :expression:`$literal` to evaluate
"`$small`", because the field name has a dollar sign (`$`) in it.

Example output:

```javascript
[
  {
    _id: 3,
    item: 'sun dress',
    'price.usd': 199.99,
    quantity: { '$large': 45, '$medium': 40, '$small': 5 }
  }
]
```
