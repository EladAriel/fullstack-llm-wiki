---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/unshardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# unshardCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only

.. include:: /includes/fact-environments-atlas-only

> **Note:** This task is not available on the {+atlas+} Free or Flex Tiers.

## Restrictions

.. include:: /includes/qe-not-supported.rst

## Syntax

```javascript
db.adminCommand( {
   unshardCollection: "<database>.<collection>",
   toShard: "<shard-id>"
} )
```

## Command Fields

## Considerations

.. include:: /includes/uc-considerations

## Requirements

.. include:: /includes/uc-reqs

## Behavior

### Unshard Zones

.. include:: /includes/fact-unshard-zones

## Examples

### Unshard a Collection

The following example unshards the `sales.eu_accounts` collection:

```javascript
db.adminCommand( {
    unshardCollection: "sales.eu_accounts"
} )
```

### Unshard to a Specific Shard

The following example unshards the `sales.us_accounts` collections and places the collection data on `shard1`:

```javascript
db.adminCommand( {
    unshardCollection: "sales.eu_accounts",
    toShard: "shard1"
} )
```

## Learn More

- :method:`sh.unshardCollection`
- `unshard-collection-task`
