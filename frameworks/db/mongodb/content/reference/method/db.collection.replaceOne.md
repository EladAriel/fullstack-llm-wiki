---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.replaceOne.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# db.collection.replaceOne() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-replaceOne.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

.. versionchanged:: 8.0

The :method:`~db.collection.replaceOne()` method has the following form:

```javascript
db.collection.replaceOne(
   <filter>,
   <replacement>,
   {
      upsert: <boolean>,
      writeConcern: <document>,
      collation: <document>,
      hint: <document|string>,
      sort: <document>
   }
)
```

The :method:`~db.collection.replaceOne()` method takes the following parameters:

## Behavior

:method:`~db.collection.replaceOne()` replaces the first matching document in the collection that matches the `filter`, using the `replacement` document.

### `upsert`

If `upsert: true` and no documents match the `filter`, :method:`db.collection.replaceOne()` creates a new document based on the `replacement` document.

.. versionchanged:: 8.0

For additional :method:`db.collection.replaceOne()` behavior on a sharded collection, see `replaceOne-sharded-collection`.

See `replaceOne-example-replace-with-upsert`.

### Capped Collections

.. include:: /includes/extracts/capped-collection-immutable-document-size-replace.rst

### Time Series Collections

You cannot use the :method:`~db.collection.replaceOne()` method on a `time series collection`.

### Sharded Collections

:method:`db.collection.replaceOne()` attempts to target a single shard, first by using the query filter. If the operation cannot target a single shard by the query filter, it then attempts to target by the replacement document.

In earlier versions, the operation attempts to target using the replacement document.

Shard Key Requirements In Replacement Document ``````````````````````````````````````````````

The replacement document does not need to include the shard key.

.. include:: /includes/shard-key-modification-warning.rst

`upsert` on a Sharded Collection ``````````````````````````````````

Starting in MongoDB 8.0, a :method:`db.collection.replaceOne()` operation that includes `upsert: true` on a sharded collection does **not** need to include the full shard key in the `filter`.

.. include:: /includes/extracts/missing-shard-key-equality-condition-update.rst

Shard Key Modification ``````````````````````

.. include:: /includes/limits-sharding-shardkey-document-immutable.rst

.. include:: /includes/shard-key-modification-warning.rst

To modify the **existing** shard key value with :method:`db.collection.replaceOne()`:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>`.

- You :red:`must` include an equality :ref:`filter
<replace-one-filter>` on the full shard key.

Missing Shard Key `````````````````

Documents in a sharded collection can be `missing the shard key fields <shard-key-missing>`. To use :method:`db.collection.replaceOne()` to set the document's **missing** shard key, you :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not` issue the operation directly on the shard.

In addition, the following requirements also apply:

> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

See also:

- `replaceOne-sharded-upsert`
- `shard-key-missing`
### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Upsert within Transactions ``````````````````````````

.. include:: /includes/extracts/transactions-upsert-availability.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

## Examples

### Replace

The `restaurant` collection contains the  following documents:

```javascript
db.restaurant.insertMany ( [ 
   { _id: 1, name: "Central Perk Cafe", Borough: "Manhattan" },
   { _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
   { _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 0 }
] )
```

The following operation replaces a single document where `name: "Central Perk Cafe"`:

```javascript
try {
   db.restaurant.replaceOne(
      { "name" : "Central Perk Cafe" },
      { "name" : "Central Pork Cafe", "Borough" : "Manhattan" }
   );
} catch (e){
   print(e);
}
```

The operation returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

If no matches were found, the operation instead returns:

```javascript
{ "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
```

Setting `upsert: true` would insert the document if no match was found. See `replaceOne-example-replace-with-upsert`

### Replace with Upsert

The `restaurant` collection contains the following documents:

```javascript
db.restaurant.insertMany( [ 
   { _id: 1, name: "Central Perk Cafe", Borough: "Manhattan",  violations: 3 },
   { _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
   { _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 0 }
] )
```

The following operation attempts to replace the document with `name : "Pizza Rat's Pizzaria"`, with `upsert : true`:

```javascript
try {
   db.restaurant.replaceOne(
      { "name" : "Pizza Rat's Pizzaria" },
      { "_id": 4, "name" : "Pizza Rat's Pizzaria", "Borough" : "Manhattan", "violations" : 8 },
      { upsert: true }
   );
} catch (e){
   print(e);
}
```

Since `upsert : true` the document is inserted based on the `replacement` document. The operation returns:

```javascript
{
   "acknowledged" : true,
   "matchedCount" : 0,
   "modifiedCount" : 0,
   "upsertedId" : 4
}
```

The collection now contains the following documents:

```javascript
{ _id: 1, name: "Central Perk Cafe", Borough: "Manhattan", violations: 3 },
{ _id: 2, name: "Rock A Feller Bar and Grill", Borough: "Queens", violations: 2 },
{ _id: 3, name: "Empire State Pub", Borough: "Brooklyn", violations: 0 },
{ _id: 4, name: "Pizza Rat's Pizzaria", Borough: "Manhattan", violations: 8 }
```

### Replace with Write Concern

Given a three member replica set, the following operation specifies a `w` of `majority` and `wtimeout` of `100`:

```javascript
try {
   db.restaurant.replaceOne(
       { "name" : "Pizza Rat's Pizzaria" },
       { "name" : "Pizza Rat's Pub", "Borough" : "Manhattan", "violations" : 3 },
       { w: "majority", wtimeout: 100 }
   );
} catch (e) {
   print(e);
}
```

If the acknowledgment takes longer than the `wtimeout` limit, the following exception is thrown:

```javascript
WriteConcernError({
   "code" : 64,
   "errmsg" : "waiting for replication timed out",
   "errInfo" : {
     "wtimeout" : true,
     "writeConcern" : {
       "w" : "majority",
       "wtimeout" : 100,
       "provenance" : "getLastErrorDefaults"
     }
   }
})
```

The following table explains the possible values of `errInfo.writeConcern.provenance`:

.. include:: /includes/fact-wc-provenance-table.rst

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

A collection `myColl` has the following documents:

```javascript
db.myColl.insertMany( [ 
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
] )
```

The following operation includes the `collation <collation>` option:

```javascript
db.myColl.replaceOne(
   { category: "cafe", status: "a" },
   { category: "cafÉ", status: "Replaced" },
   { collation: { locale: "fr", strength: 1 } }

);
```

### Specify `hint` for `replaceOne`

Create a sample `members` collection with the following documents:

```javascript
db.members.insertMany( [
   { _id: 1, member: "abc123", status: "P", points:  0,  misc1: null, misc2: null },
   { _id: 2, member: "xyz123", status: "A", points: 60,  misc1: "reminder: ping me at 100pts", misc2: "Some random comment" },
   { _id: 3, member: "lmn123", status: "P", points:  0,  misc1: null, misc2: null },
   { _id: 4, member: "pqr123", status: "D", points: 20,  misc1: "Deactivated", misc2: null },
   { _id: 5, member: "ijk123", status: "P", points:  0,  misc1: null, misc2: null },
   { _id: 6, member: "cde123", status: "A", points: 86,  misc1: "reminder: ping me at 100pts", misc2: "Some random comment" }
] )
```

Create the following indexes on the collection:

```javascript
db.members.createIndex( { status: 1 } )
db.members.createIndex( { points: 1 } )
```

The following update operation explicitly hints to use the index `{ status: 1 }`:

> **Note:** If you specify an index that does not exist, the operation errors.

```javascript
db.members.replaceOne(
   { "points": { $lte: 20 }, "status": "P" }, 
   { "misc1": "using index on status", status: "P", member: "replacement", points: "20"},
   { hint: { status: 1 } }
)
```

The operation returns the following:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

To view the indexes used, you can use the :pipeline:`$indexStats` pipeline:

```javascript
db.members.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } } ] )
```

### Replace One Document and Use a Sort

.. include:: /includes/restaurants-update-sort-example.rst

```javascript
db.restaurantsSort.replaceOne(
   // Find restaurants with a rating of 4
   { rating: 4 },

   // Replace the found restaurant with Clean Eats
   { name: "Clean Eats", rating: 4, violations: 2 },

   // Sort restaurants found by the most violations with a descending sort
   { sort: { violations: -1 } }
)
```

.. include:: /includes/restaurants-update-sort-example-description-and-output.rst
