---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/filemd5.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
