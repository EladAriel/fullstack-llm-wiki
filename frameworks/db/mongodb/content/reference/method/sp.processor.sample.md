---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.sample.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
