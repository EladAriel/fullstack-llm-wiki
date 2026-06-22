---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.getOperations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# Bulk.getOperations() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

The following initializes a :method:`Bulk()` operations builder on the `items` collection, adds a series of write operations, executes the operations, and then calls :method:`~Bulk.getOperations()` on the `bulk` builder object:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();

for (var i = 1; i <= 1500; i++) {
    bulk.insert( { x: i } );
}

bulk.execute();
bulk.getOperations();
```

The :method:`~Bulk.getOperations()` method returns an array with the operations executed. The output shows that MongoDB divided the operations into 2 groups, one with 1000 operations and one with 500. For information on how MongoDB groups the list of bulk write operations, see `Bulk.execute() Behavior <bulk-execute-behavior>`

Although the method returns all 1500 operations in the returned array, this page omits some of the results for brevity.

```javascript
[
   {
      "originalZeroIndex" : 0,
      "batchType" : 1,
      "operations" : [
         { "_id" : ObjectId("53a8959f1990ca24d01c6165"), "x" : 1 },

         ... // Content omitted for brevity

         { "_id" : ObjectId("53a8959f1990ca24d01c654c"), "x" : 1000 }
      ]
   },
   {
      "originalZeroIndex" : 1000,
      "batchType" : 1,
      "operations" : [
         { "_id" : ObjectId("53a8959f1990ca24d01c654d"), "x" : 1001 },

         ... // Content omitted for brevity

         { "_id" : ObjectId("53a8959f1990ca24d01c6740"), "x" : 1500 }
      ]
   }
]
```

## Returned Fields

The array contains documents with the following fields:

> **Seealso:** - :method:`Bulk()`
- :method:`Bulk.execute()`
