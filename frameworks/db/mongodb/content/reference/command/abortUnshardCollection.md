---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortUnshardCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================================

# abortUnshardCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.txt

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
db.adminCommand( { 
   abortUnshardCollection: "<database>.<collection>" 
} )
```

## Command Fields

## Examples

.. include:: /includes/auc-example-intro.rst

```javascript
db.adminCommand( { 
   abortUnshardCollection: "sales.us_accounts" 
} )
```

## Learn More

- :method:`sh.abortUnshardCollection`
- `stop-unshard-collection-task`
