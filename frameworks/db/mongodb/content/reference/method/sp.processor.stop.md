---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.stop.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
