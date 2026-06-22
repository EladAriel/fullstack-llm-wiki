---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.remove.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# db.collection.remove() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-deprecated.rst

## Definition

## Syntax

`db.collection.remove()` can have one of two syntaxes. `remove()` can take a query document and an optional `justOne` boolean:

```javascript
db.collection.remove(
    <query>,
    <justOne>
)
```

Or the method can take a query document and an optional remove options document:

.. versionchanged:: 5.0

```javascript
db.collection.remove(
    <query>,
    {
      justOne: <boolean>,
      writeConcern: <document>,
      collation: <document>,
      let: <document> // Added in MongoDB 5.0
    }
)
```

`db.collection.remove()` takes the following parameters:

## Behavior

### Write Concern

`remove()` uses the :dbcommand:`delete` command, which uses the default `write concern </reference/write-concern>`. To specify a different write concern, include the write concern in the options parameter.

### Query Considerations

By default, `remove()` removes all documents that match the `query` expression. Specify the `justOne` option to limit the operation to removing a single document. To delete a single document sorted by a specified order, use the `findAndModify() <findAndModify-wrapper-sorted-remove>` method.

When removing multiple documents, the remove operation may interleave with other read or write operations to the collection.

### Time Series Collections

You cannot use `remove()` on a `time series collection`.

### Sharded Collections

.. include:: /includes/fact-single-modification-in-sharded-collections.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-operations-write-concern.rst

.. include:: /includes/extracts/transactions-usage.rst

## Examples

The following are examples of the `remove()` method.

### Remove All Documents from a Collection

To remove all documents in a collection, call the `remove()` method with an empty query document `{}`. The following operation deletes all documents from the `bios collection </reference/bios-example-collection>`:

```javascript
db.bios.remove( { } )
```

This operation is not equivalent to the :method:`~db.collection.drop()` method.

To remove all documents from a collection, it may be more efficient to use the :method:`~db.collection.drop()` method to drop the entire collection, including the indexes, and then recreate the collection and rebuild the indexes.

### Remove All Documents that Match a Condition

To remove the documents that match a deletion criteria, call the `remove()` method with the `<query>` parameter:

The following operation removes all the documents from the collection `products` where `qty` is greater than `20`:

```javascript
db.products.remove( { qty: { $gt: 20 } } )
```

### Override Default Write Concern

The following operation to a replica set removes all the documents from the collection `products` where `qty` is greater than `20` and specifies a `write concern <write-concern>` of `w: 2` with a `wtimeout` of 5000 milliseconds. This operation either returns after the write propagates to both the primary and one secondary, or times out after 5 seconds.

```javascript
db.products.remove(
    { qty: { $gt: 20 } },
    { writeConcern: { w: "majority", wtimeout: 5000 } }
)
```

### Remove a Single Document that Matches a Condition

To remove the first document that match a deletion criteria, call the `remove()` method with the `query` criteria and the `justOne` parameter set to `true` or `1`.

The following operation removes the first document from the collection `products` where `qty` is greater than `20`:

```javascript
db.products.remove( { qty: { $gt: 20 } }, true )
```

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

A collection `myColl` has the following documents:

```javascript
{ _id: 1, category: "café", status: "A" }
{ _id: 2, category: "cafe", status: "a" }
{ _id: 3, category: "cafE", status: "a" }
```

The following operation includes the `collation <collation>` option:

```javascript
db.myColl.remove( 
   { category: "cafe", status: "A" }, 
   { collation: { locale: "fr", strength: 1 } }
)
```

### Use Variables in `let`

.. include:: /includes/let-example-introduction.rst

.. include:: /includes/let-example-delete-flavors.rst

```javascript
db.cakeFlavors.remove(
   { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   { let : { targetFlavor: "strawberry" } }
)
```

## WriteResult

### Successful Results

`remove()` returns a :method:`WriteResult` object that contains the status of the operation. Upon success, the :method:`WriteResult` object contains information on the number of documents removed:

```javascript
WriteResult({ "nRemoved" : 4 })
```

> **Seealso:** `WriteResult.nRemoved`

### Write Concern Errors

If `remove()` encounters write concern errors, the results include the `WriteResult.writeConcernError` field:

```javascript
WriteResult({
  "nRemoved" : 7,
  "writeConcernError" : {
    "code" : 64,
    "codeName" : "WriteConcernTimeout",
    "errmsg" : "waiting for replication timed out",
    "errInfo" : {
      "wtimeout" : true,
      "writeConcern" : { 
        "w" : "majority",
        "wtimeout" : 1,
        "provenance" : "getLastErrorDefaults"
      }
    }
  }
})
```

> **Seealso:** - `WriteResult.writeConcernError`

### Errors Unrelated to Write Concern

If `remove()` encounters a non-write concern error, the results include `WriteResult.writeError` field:

```javascript
WriteResult({
   "nRemoved" : 0,
   "writeError" : {
      "code" : 2,
      "errmsg" : "unknown top level operator: $invalidFieldName"
   }
})
```
