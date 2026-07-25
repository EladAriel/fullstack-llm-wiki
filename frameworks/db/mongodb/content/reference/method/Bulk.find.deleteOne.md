---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.deleteOne.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# Bulk.find.deleteOne() (mongosh method)

## Definition

## Syntax

The command has the following syntax:

```javascript
Bulk.find( <filter document> ).deleteOne()
```

For details on the `find()` method see: :method:`Bulk.find()`

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

Create the `music` collection:

```javascript
db.music.insertMany( [
   { artist: "DOA", genre: "punk" },
   { artist: "Rick Astley", genre: "pop" },
   { artist: "Black Flag", genre: "punk" },
   { artist: "Justin Bieber", genre: "pop" }
] )
```

The following example:

- Initializes a :method:`Bulk()` operations builder.
- Searches for the genre `pop`.
- Deletes `Rick Astley`, the first matching pop artist, from the
collection.

```javascript
var bulk = db.music.initializeOrderedBulkOp();
bulk.find( { "genre": "pop" } ).deleteOne();
bulk.execute()
```

To delete all `"pop"` music, use :method:`Bulk.find.delete()` instead.
