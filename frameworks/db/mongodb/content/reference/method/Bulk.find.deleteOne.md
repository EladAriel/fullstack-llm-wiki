---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.deleteOne.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
