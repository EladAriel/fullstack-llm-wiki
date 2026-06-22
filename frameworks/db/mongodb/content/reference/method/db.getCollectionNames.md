---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getCollectionNames.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# db.getCollectionNames() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/extracts/listCollections-auth-showCollectionNames.rst

## Behavior

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

## Example

The following returns the names of all collections in the `records` database:

```javascript
use records
db.getCollectionNames()
```

The method returns the names of the collections in an array:

```javascript
[ "employees", "products", "mylogs", "system.indexes" ]
```
