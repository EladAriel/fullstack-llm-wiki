---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.splitAt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# sh.splitAt() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Consideration

In most circumstances, you should leave chunk splitting to the automated processes within MongoDB. However, when initially deploying a `sharded cluster`, it may be beneficial to `pre-split <pre-splitting>` manually an empty collection using methods such as :method:`sh.splitAt()`.

## Behavior

:method:`sh.splitAt()` splits the original chunk into two chunks. One chunk has a shard key range that starts with the original lower bound (inclusive) and ends at the specified shard key value (exclusive). The other chunk has a shard key range that starts with the specified shard key value (inclusive) as the lower bound and ends at the original upper bound (exclusive).

To split a chunk at its median point instead, see :method:`sh.splitFind()`.

## Example

For the sharded collection `test.foo`, the following example splits a chunk at the shard key value `x: 70`.

```javascript
sh.splitAt( "test.foo", { x: 70 } )
```
