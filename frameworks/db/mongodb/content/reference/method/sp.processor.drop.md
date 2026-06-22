---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.drop.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# sp.processor.drop() (mongosh method)

## Definition

.. versionadded:: 7.0

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.processor.drop()` method has the following syntax:

```json
sp.processor.drop(
  {
    <options>
  }
)
```

## Command Fields

`sp.processor.drop()` takes a generic, optional `<options>` document whose fields are passed to the underlying drop command.

## Behavior

`sp.processor.drop()` deletes the given named stream processor from the current stream processing workspace. If you invoke this command on a currently running stream processor, it stops that processor before deleting it.

## Access Control

The user running `sp.processor.drop()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example stops a stream processor named `solarDemo`

```
sp.solarDemo.drop()
```

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
