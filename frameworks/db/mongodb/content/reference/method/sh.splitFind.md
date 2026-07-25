---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.splitFind.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================

# sh.splitFind() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Consideration

In most circumstances, you should leave chunk splitting to the automated processes within MongoDB.

To use :method:`sh.splitFind()`, the sharded collection must be populated.

## Example

For the sharded collection `test.foo`, the following example splits, at the median point, a chunk that contains the shard key value `x: 70`.

```javascript
sh.splitFind( "test.foo", { x: 70 } )
```
