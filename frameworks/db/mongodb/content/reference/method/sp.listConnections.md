---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.listConnections.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================================

# sp.listConnections() (mongosh method)

## Definition

## Syntax

The :method:`sp.listConnections()` method has the following syntax:

```json
sp.listConnections()
```

## Command Fields

`sp.listConnections()` takes no fields.

## Behavior

`sp.listConnections()` returns documents describing all of the connections in the connection registry of the current stream processing workspace to the shell.

## Access Control

The user running `sp.listConnections()` must have the :atlasrole:`atlasAdmin` role.

## Example

The following example shows an expected response from `sp.listConnections()`:

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-processing-instance>`
