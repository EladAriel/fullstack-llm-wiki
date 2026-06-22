---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.moveCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
