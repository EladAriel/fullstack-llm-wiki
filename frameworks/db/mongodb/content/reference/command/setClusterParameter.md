---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setClusterParameter.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# setClusterParameter (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

```javascript
db.adminCommand( 
   { 
     setClusterParameter: { <parameter>: <value> } 
   } 
)
```

For the available cluster parameters, including examples, see `cluster-parameters`.

## Behavior

- You can only run `setClusterParameter` on the `admin` database. If you run
the command on any other database, MongoDB returns an error.

- You can only run `setClusterParameter` on a replica set primary or on a
`sharded cluster`.

- You **cannot** run `setClusterParameter` on a standalone deployment.
- `setClusterParameter` accepts only one parameter at a time.
### Accesss Control

When `authentication <authentication>` is enabled, `setClusterParameter` only works when authenticated as a user with a role that has access to the `setClusterParameter` action.

### Persistence

The parameter modifications made using `setClusterParameter` are persisted on replica sets and sharded clusters. This ensures that parameter modifications made using `setClusterParameter` survive restarts.

### Stable API

When using `Stable API <stable-api>` V1 with `apiStrict <api-strict-desc>` set to `true`, you cannot use :dbcommand:`setClusterParameter` to modify cluster parameters.
