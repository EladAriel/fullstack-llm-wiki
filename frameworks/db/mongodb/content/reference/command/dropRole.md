---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropRole.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# dropRole (database command)

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
     dropRole: "<role>",
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

## Behavior

### Authentication

.. include:: /includes/behavior-drop-role.rst

## Required Access

.. include:: /includes/access-drop-role.rst

## Example

The following operations remove the `readPrices` role from the `products` database:

```javascript
use products
db.runCommand(
   {
     dropRole: "readPrices",
     writeConcern: { w: "majority" }
   }
)
```
