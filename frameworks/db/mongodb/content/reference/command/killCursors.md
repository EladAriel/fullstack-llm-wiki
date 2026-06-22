---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/killCursors.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# killCursors (database command)

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
     killCursors: <collection>, 
     cursors: [ <cursor id1>, ... ], comment: <any> 
   } 
)
```

## Command Fields

The command takes the following fields:

## Required Access

### Kill Own Cursors

Users can always kill their own cursors regardless of whether they have the :authaction:`killCursors` privilege. Cursors are associated with the users at the time of cursor creation.

### Kill Any Cursor

If a user has the :authaction:`killAnyCursor` privilege, they can kill cursors created by any user.

## `killCursors` and Transactions

.. include:: /includes/extracts/transactions-killop-change.rst

## Example

Consider the following :dbcommand:`find` operation on the `test.restaurants` collection:

```javascript
use test
db.runCommand(
   { find: "restaurants",
     filter: { stars: 5 },
     projection: { name: 1, rating: 1, address: 1 },
     sort: { name: 1 },
     batchSize: 5
   }
)
```

which returns the following:

```javascript
{
   "waitedMS" : Long(0),
   "cursor" : {
      "firstBatch" : [
         {
            "_id" : ObjectId("57506d63f578028074723dfd"),
            "name" : "Cakes and more"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e0b"),
            "name" : "Pies and things"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e1d"),
            "name" : "Ice Cream Parlour"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e65"),
            "name" : "Cream Puffs"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e66"),
            "name" : "Cakes and Rolls"
         }
      ],
      "id" : Long("18314637080"),
      "ns" : "test.restaurants"
   },
   "ok" : 1
}
```

To kill this cursor, use the :dbcommand:`killCursors` command.

```javascript
use test

db.runCommand( { killCursors: "restaurants", cursors: [ Long("18314637080") ] } )
```

:dbcommand:`killCursors` returns the following operation details:

```javascript
{
   "cursorsKilled" : [
      Long("18314637080")
   ],
   "cursorsNotFound" : [ ],
   "cursorsAlive" : [ ],
   "cursorsUnknown" : [ ],
   "ok" : 1
}
```
