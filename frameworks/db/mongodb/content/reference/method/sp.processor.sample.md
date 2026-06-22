---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.sample.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# sp.processor.sample() (mongosh method)

## Definition

.. versionadded:: 7.0

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.processor.sample()` method has the following syntax:

```json
sp.processor.sample()
```

## Command Fields

`sp.processor.sample()` takes no fields.

## Behavior

`sp.processor.sample()` returns arrays of sampled results from the named, currently running stream processor to `STDOUT`. This command runs continuously until you cancel it using `CTRL-C`, or until the returned samples cumulatively reach `40 MB`.

## Access Control

The user running `sp.processor.sample()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example shows an expected response from calling `sp.solarDemo.sample()` to sample from a stream processor called `solarDemo`:

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
