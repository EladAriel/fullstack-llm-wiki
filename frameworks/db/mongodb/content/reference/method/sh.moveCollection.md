---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.moveCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# sh.moveCollection() (mongosh method)

## Definition

## Syntax

`sh.moveCollection()` has the following syntax:

```javascript
sh.moveCollection( "<namespace>", "<toShard>" )
```

.. include:: /includes/retrieve-shard-id-note.rst

### Parameters

`sh.moveCollection()` takes the following parameters:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

> **Note:** This command is not available on the Atlas Free and Flex Tier.

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

.. include:: /includes/mc-considerations.rst

## Requirements

.. include:: /includes/mc-reqs.rst

## Examples

This example moves an unsharded collection named `inventory` on the `app` database to the `shard02` shard.

```javascript
sh.moveCollection( "app.inventory", "shard02" )  
```

.. include:: /includes/mc-sh-status.rst

## Learn More

- :dbcommand:`moveCollection`
- `moveable-collections`
