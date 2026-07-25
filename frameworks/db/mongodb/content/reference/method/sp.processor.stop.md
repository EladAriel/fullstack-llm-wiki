---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.stop.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# sp.processor.stop() (mongosh method)

## Definition

.. versionadded:: 7.0

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.processor.stop()` method has the following syntax:

```json
sp.processor.stop(
  {
    <options>
  }
)
```

## Command Fields

`sp.processor.stop()` takes a generic, optional `<options>` document whose fields are passed to the underlying stop command.

## Behavior

`sp.processor.stop()` stops a named stream processor on the current stream processing workspace. The stream processor must be in a `running` state. If you invoke `sp.processor.stop()` for a stream processor that is not `running`, `mongosh` will return an error.

## Access Control

The user running `sp.processor.stop()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example stops a stream processor named `solarDemo`.

```
sp.solarDemo.stop()
```

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
