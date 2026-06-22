---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/delete.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# delete (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     delete: <collection>, 
     deletes: [
        { 
          q : <query>, 
          limit : <integer>, 
          collation: <document>,
          hint: <document|string>
        },
        ...
     ],
     comment: <any>,
     let: <document>, // Added in MongoDB 5.0
     ordered: <boolean>,
     writeConcern: { <write concern> },
     maxTimeMS: <integer>
  }
)
```

## Command Fields

The command takes the following fields:

Each element of the `deletes` array contains the following fields:

## Behavior

### Sharded Collections

.. include:: /includes/fact-single-modification-in-sharded-collections.rst

### Limits

The total size of all the queries (i.e. the `q` field values) in the `deletes` array must be less than or equal to the :limit:`maximum BSON document size <BSON Document Size>`.

The total number of delete documents in the `deletes` array must be less than or equal to the :limit:`maximum bulk size <Write Command Batch Limit Size>`.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-operations-write-concern.rst

.. include:: /includes/extracts/transactions-usage.rst

## Examples

### Limit the Number of Documents Deleted

The following example deletes from the `orders` collection one document that has the `status` equal to `D` by specifying the `limit` of `1`:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [ { q: { status: "D" }, limit: 1 } ]
   }
)
```

The returned document shows that the command deleted `1` document. See `delete-command-output` for details.

```javascript
{ "ok" : 1, "n" : 1 }
```

> **Note:** .. include:: /includes/fact-single-modification-in-sharded-collections.rst

### Delete All Documents That Match a Condition

The following example deletes from the `orders` collection all documents that have the `status` equal to `D` by specifying the `limit` of `0`:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [ { q: { status: "D" }, limit: 0 } ],
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

The returned document shows that the command found and deleted `13` documents. See `delete-command-output` for details.

```javascript
{ "ok" : 1, "n" : 13 }
```

### Delete All Documents from a Collection

.. include:: /includes/note-drop-faster-than-delete-for-large-collections.rst

Delete all documents in the `orders` collection by specifying an empty query condition and a `limit` of `0`:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [ { q: { }, limit: 0 } ],
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)
```

The returned document shows that the command found and deleted `35` documents in total. See `delete-command-output` for details.

```javascript
{ "ok" : 1, "n" : 35 }
```

### Bulk Delete

The following example performs multiple delete operations on the `orders` collection:

```javascript
db.runCommand(
   {
      delete: "orders",
      deletes: [
         { q: { status: "D" }, limit: 0 },
         { q: { cust_num: 99999, item: "abc123", status: "A" }, limit: 1 }
      ],
      ordered: false,
      writeConcern: { w: 1, j: true }
   }
)
```

The returned document shows that the command found and deleted `21` documents in total for the two delete statements. See `delete-command-output` for details.

```javascript
{ "ok" : 1, "n" : 21 }
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
db.runCommand({
   delete: "myColl",
   deletes: [
     { q: { category: "cafe", status: "a" }, limit: 0, collation: { locale: "fr", strength: 1 } }
   ]
})
```

### Specify `hint` for Delete Operations

In :binary:`~bin.mongosh`, create a `members` collection with the following documents:

```javascript
db.members.insertMany([
   { "_id" : 1, "member" : "abc123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 2, "member" : "xyz123", "status" : "A", "points" : 60,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" },
   { "_id" : 3, "member" : "lmn123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 4, "member" : "pqr123", "status" : "D", "points" : 20,  "misc1" : "Deactivated", "misc2" : null },
   { "_id" : 5, "member" : "ijk123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 6, "member" : "cde123", "status" : "A", "points" : 86,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" }
])
```

Create the following indexes on the collection:

```javascript
db.members.createIndex( { status: 1 } )
db.members.createIndex( { points: 1 } )
```

The following delete operation explicitly hints to use the index `{ status: 1 }`:

```javascript
db.runCommand({
   delete: "members",
   deletes: [
     { q: { "points": { $lte: 20 }, "status": "P" }, limit: 0, hint: { status: 1 } }
   ]
})
```

> **Note:** If you specify an index that does not exist, the operation errors.

To see the index used, run :dbcommand:`explain` on the operation:

```javascript
db.runCommand(
   {
     explain: {
       delete: "members",
       deletes: [ 
         { q: { "points": { $lte: 20 }, "status": "P" }, limit: 0, hint: { status: 1 } }
       ]
     },
     verbosity: "queryPlanner"
   }
)
```

### Use Variables in `let`

.. include:: /includes/let-example-introduction.rst

.. include:: /includes/let-example-delete-flavors.rst

```javascript
db.runCommand( {
   delete: db.cakeFlavors.getName(),
   deletes: [ {
      q: { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
      limit: 1
   } ],
   let : { targetFlavor: "strawberry" }
} )
```

## Output

The returned document contains a subset of the following fields:

The following is an example document returned for a successful :dbcommand:`delete` command:

```javascript
{ ok: 1, n: 1 }
```

The following is an example document returned for a :dbcommand:`delete` command that encountered an error because it specified a non-existent index in the `hint` field:

```javascript
{
  n: 0,
  writeErrors: [
    {
      index: 0,
      code: 2,
      errmsg: 'error processing query: ns=test.products: hat $eq "bowler"\n' +
        'Sort: {}\n' +
        'Proj: {}\n' +
        ' planner returned error :: caused by :: hint provided does not correspond to an existing index'
    }
  ],
  ok: 1
}
```
