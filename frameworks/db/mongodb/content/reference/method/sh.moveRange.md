---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.moveRange.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# sh.moveRange() (mongosh method)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```none
sh.moveRange(namespace, toShard, min, max)
```

The `sh.moveRange()` method takes the following parameters:

## Example

The following example uses a collection with:

- Shard key `postal`, representing a postal code.
- A range with the boundaries `70007` and `70124`.
To move the postal range to `shard02`, run the following method:
