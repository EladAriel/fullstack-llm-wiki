---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropAllUsersFromDatabase.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# dropAllUsersFromDatabase (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
  {   
    dropAllUsersFromDatabase: 1,
    writeConcern: { <write concern> },
    comment: <any>
  }
)
```

## Command Fields

The command takes the following fields:

## Required Access

.. include:: /includes/access-drop-user.rst

## Example

The following sequence of operations in :binary:`~bin.mongosh` drops every user from the `products` database:

```javascript
use products
db.runCommand( { dropAllUsersFromDatabase: 1, writeConcern: { w: "majority" } } )
```

The `n` field in the results document shows the number of users removed:

```javascript
{ "n" : 12, "ok" : 1 }
```
