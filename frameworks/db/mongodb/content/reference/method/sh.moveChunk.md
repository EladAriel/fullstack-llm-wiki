---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.moveChunk.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# sh.moveChunk() (mongosh method)

## Definition

> **Seealso:** - :dbcommand:`moveChunk`
- :method:`sh.splitAt()`
- :method:`sh.splitFind()`
- `/sharding`, and :ref:`chunk migration
  <sharding-chunk-migration>`

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Example

Given the `people` collection in the `records` database, the following operation finds the chunk that contains the documents with the `zipcode` field set to `53187` and then moves that chunk to the shard named `shard0019`:

```javascript
sh.moveChunk("records.people", { zipcode: "53187" }, "shard0019")
```
