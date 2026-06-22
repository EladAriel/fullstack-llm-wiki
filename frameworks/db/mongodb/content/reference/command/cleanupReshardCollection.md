---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/cleanupReshardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
