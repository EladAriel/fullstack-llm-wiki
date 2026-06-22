---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/filemd5.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# filemd5 (database command)

> **Important:** This command is deprecated and its use is discouraged as MD5 is no
longer considered cryptographically secure.

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
     filemd5: ObjectId("4f1f10e37671b50e4ecd2776"), 
     root: "fs" 
   }
)
```

MongoDB computes the `filemd5` using all data in the GridFS file object pulled sequentially from each chunk in the `chunks` collection.
