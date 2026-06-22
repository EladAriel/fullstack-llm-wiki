---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.commitReshardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# sh.commitReshardCollection() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`sh.commitReshardCollection()` method has the following syntax:

```javascript
sh.commitReshardCollection( <namespace> )
```

### Parameter

The :method:`sh.commitReshardCollection()` method takes the following parameter:

## Example

### Commit a Resharding Operation

The following command forces the `resharding operation <sharding-resharding>` on the `sales.orders` to block writes and complete:

```javascript
sh.commitReshardCollection("sales.orders")
```

> **Seealso:** `sharding-resharding`
