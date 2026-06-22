---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropUser.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# dropUser (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     dropUser: "<user>",
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

.. include:: /includes/check-before-dropping-useradmin.rst

## Required Access

.. include:: /includes/access-drop-user.rst

## Example

The following sequence of operations in :binary:`~bin.mongosh` removes `reportUser1` from the `products` database:

```javascript
use products
db.runCommand( { 
   dropUser: "reportUser1",
   writeConcern: { w: "majority", wtimeout: 5000 }
} )
```
