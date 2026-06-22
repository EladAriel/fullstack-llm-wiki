---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropAllRolesFromDatabase.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# dropAllRolesFromDatabase (database command)

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
    dropAllRolesFromDatabase: 1,
    writeConcern: { <write concern> },
    comment: <any>
  }
)
```

## Command Fields

The command has the following fields:

## Required Access

.. include:: /includes/access-drop-role.rst

## Example

The following operations drop all `user-defined <user-defined-roles>` roles from the `products` database:

```javascript
use products
db.runCommand(
   {
     dropAllRolesFromDatabase: 1,
     writeConcern: { w: "majority" }
   }
)
```

The `n` field in the results document reports the number of roles dropped:

```javascript
{ "n" : 4, "ok" : 1 }
```
