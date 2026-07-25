---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.map.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# cursor.map() (mongosh method)

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

:method:`cursor.map()` returns a `Cursor` object. Note that `.map()` only converts the type, it does not create a new cursor. You can convert the `Cursor` object to an `Array` with `.toArray()`.

## Examples

These examples refer to the products collection:

```javascript
db.products.insertMany([ 
   { _id: 1, name: 'widget', price: 10.89 },
   { _id: 2, name: 'thing', price: 11.24 },
   { _id: 3, name: 'moppet', price: 8 },
   { _id: 4, name: 'cosa', price: 24.19 }
])
```

### Return a Value From a Collection

Get the product names.

```javascript
db.products.find().map( function(p) { return p.name; } ) ;
```

### Return Results as an `Array`

Calculate a discounted sale price and return the results as an array.

```javascript
var salePrices = db.products.find().map( function(p) { return p.price * .9 } ).toArray() ;
```

Confirm that the output is an `Array`

```javascript
salePrices.constructor.name
```

> **Seealso:** :method:`cursor.forEach()` for similar functionality.
