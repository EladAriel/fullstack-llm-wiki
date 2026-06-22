---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.listWorkspaceDefaults.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
