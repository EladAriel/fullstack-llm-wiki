---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.start.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# sp.processor.start() (mongosh method)

## Definition

.. versionadded:: 7.0

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.processor.start()` method has the following syntax:

```json
sp.processor.start(
  {
    <options>
  }
)
```

## Command Fields

`sp.processor.start()` takes a generic, optional `<options>` document whose fields are passed to the underlying start command. These fields can be:

## Behavior

`sp.processor.start()` starts a named stream processor on the current stream processing workspace. The stream processor must be in a `STOPPED` state. If you invoke `sp.processor.start()` for a stream processor that is not `STOPPED`, `mongosh` will return an error.

## Access Control

The user running `sp.processor.start()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example starts a stream processor named `solarDemo`.

```sh
sp.solarDemo.start()
```

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
