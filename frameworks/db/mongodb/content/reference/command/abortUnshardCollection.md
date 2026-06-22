---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortUnshardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
