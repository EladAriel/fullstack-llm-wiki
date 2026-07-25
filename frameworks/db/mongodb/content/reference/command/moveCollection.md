---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/moveCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# moveCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.txt

.. include:: /includes/fact-environments-onprem-only.rst

## Restrictions

.. include:: /includes/qe-not-supported.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
  { 
    moveCollection: "<database>.<collection>",
    toShard: "<ID of the recipient shard>",
  } 
)
```

.. include:: /includes/retrieve-shard-id-note.rst

## Command Fields

The command takes the following fields:

## Considerations

.. include:: /includes/mc-considerations.rst

## Requirements

.. include:: /includes/mc-reqs.rst

## Example

.. include:: /includes/mc-example-intro.rst

```javascript
db.adminCommand( 
  { 
    moveCollection: "app.inventory",
    toShard: "shard02"
  } 
)
```

.. include:: /includes/mc-sh-status.rst

## Learn More

- :method:`sh.moveCollection`
- `moveable-collections`
