---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.listStreamProcessors.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================================

# sp.listStreamProcessors() (mongosh method)

## Definition

.. versionadded:: 7.0

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.listStreamProcessors()` method has the following syntax:

```json
sp.listStreamProcessors(
  {
   <filter>
  }
)
```

## Command Fields

`sp.listStreamProcessors()` takes these fields:

## Behavior

`sp.listStreamProcessors()` returns documents describing all of the named stream processors on the current stream processing workspace to `STDOUT`.

## Access Control

The user running `sp.listStreamProcessors()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example shows an expected response from `sp.listStreamProcessors()` when the command is called without any filter:

The following example shows an expected response if you invoke `sp.listStreamProcessors()` filtering for only those stream processors with a `state` of `running`.

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
