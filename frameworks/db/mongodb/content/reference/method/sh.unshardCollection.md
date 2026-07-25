---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.unshardCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================================

# sh.unshardCollection (mongosh method)

## Definition

## Syntax

`sh.unshardCollection` has the following syntax:

```text
sh.unshardCollection( namespace, shardID )
```

### Parameters

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-atlas-only.rst

## Considerations

.. include:: /includes/uc-considerations.rst

## Requirements

.. include:: /includes/uc-reqs

## Behavior

### Unshard Zones

.. include:: /includes/fact-unshard-zones

## Examples

### Unshard a Collection

This example unshards a collection named `inventory` on the `app` database to the `shard02` shard.

```javascript
sh.unshardCollection( "app.inventory", "shard02" )
```

.. include:: /includes/mc-sh-status.rst

## Learn More

- :dbcommand:`unshardCollection`
- `unshard-collection-task`
