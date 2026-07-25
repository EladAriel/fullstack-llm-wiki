---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.listWorkspaceDefaults.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# sp.listWorkspaceDefaults() (mongosh method)

## Definition

## Compatibility

.. include:: /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax

The :method:`sp.listWorkspaceDefaults()` method has the following syntax:

```javascript
sp.listWorkspaceDefaults()
```

## Return Value

`sp.listWorkspaceDefaults()` returns a document containing the following fields:

## Behavior

`sp.listWorkspaceDefaults()` returns a single document describing the default and maximum tier configuration for the current stream processing workspace to `STDOUT`.

## Access Control

Running `sp.listWorkspaceDefaults()` requires the :atlasrole:`atlasAdmin` role.

## Example

The following example shows an expected response from `sp.listWorkspaceDefaults()`:

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`
- :method:`sp.listStreamProcessors()`
- :method:`sp.createStreamProcessor()`
