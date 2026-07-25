---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/cleanupReshardCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# cleanupReshardCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
  {
    cleanupReshardCollection: "<database>.<collection>"
  }
)
```

## Example

### Clean up a Failed Resharding Operation

The following example cleans up metadata of a failed `resharding operation <sharding-resharding>` on the `sales.orders` collection:

```javascript
db.adminCommand({
  cleanupReshardCollection: "sales.orders"
})
```

> **Seealso:** `sharding-resharding`
