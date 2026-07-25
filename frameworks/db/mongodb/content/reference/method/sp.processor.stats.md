---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.stats.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================================

# sp.processor.stats() (mongosh method)

## Definition

.. versionadded:: 7.0

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.processor.stats()` method has the following syntax:

```json
sp.processor.stats( { options: { scale: <int>, verbose: <boolean> } } )
```

## Command Fields

`sp.processor.stats()` takes these fields:

## Behavior

`sp.processor.stats()` returns a document containing statistics about the specified stream processor to `STDOUT`. These statistics include but are not limited to:

- The number of messages ingested and processed
- The total size of all input and output
- The amount of memory used to store processor state
You can only invoke `sp.processor.stats()` on a currently running stream processor. If you try to invoke this command on a stopped stream processor, `mongosh` will return an error.

## Access Control

The user running `sp.processor.stats()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example shows an expected response from calling `sp.solarDemo.stats()` to get the statistics of a stream processor called `solarDemo`:

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
