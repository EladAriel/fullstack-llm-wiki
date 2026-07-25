---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.moveRange.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
