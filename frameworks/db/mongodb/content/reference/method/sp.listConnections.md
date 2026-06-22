---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.listConnections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
