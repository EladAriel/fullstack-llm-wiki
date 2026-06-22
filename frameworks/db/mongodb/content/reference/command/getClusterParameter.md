---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getClusterParameter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# getClusterParameter (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     getClusterParameter: <parameter> | [<parameter>, <parameter>] | "'*'"
   }
)
```

## Command Fields

The command takes the following fields:

## Behavior

- You can only run `getClusterParameter` on the `admin` database. If
you run the command on any other database, MongoDB returns an error.

- You can run `getClusterParameter` on any node in a replica set or
sharded cluster.

- When you run `getClusterParameter` on :binary:`~bin.mongod`,
`getClusterParameter` returns cached parameter values.

- When you run `getClusterParameter` on :binary:`~bin.mongos`,
`getClusterParameter` returns the `durable` value of the cluster parameter from the `config server <sharding-config-server>`.

### Access Control

When `authentication <authentication>` is enabled, `getClusterParameter` only works when authenticated as a user with a role that has access to the `getClusterParameter` action.

{+atlas+} users must have the :atlasrole:`atlasAdmin` role.

## Examples

> **Note:** The output of the following examples may vary depending on the specific
configuration of the running MongoDB deployment.

### Retrieve Single Cluster Parameter

The following operation runs `getClusterParameter` on the `admin` database using a value of `hostName` to retrieve the value for a hypothetical cluster parameter named `hostName`:

```javascript
use admin
db.adminCommand( { getClusterParameter : "hostName" } )
```

### Retrieve Multiple Cluster Parameters

The following operation runs `getClusterParameter` on the `admin` database using the values `hostName` and `testParameter` to retrieve the values for hypothetical cluster parameters named `hostName` and `testParameter`:

```javascript
use admin
db.adminCommand( { getClusterParameter: [ "hostName", "testParameter" ] } )
```

### Retrieve All Cluster Parameters

The following operation runs `getClusterParameter` with a value of `'*'` to retrieve the values from all cluster parameters:

```javascript
use admin
db.adminCommand( { getClusterParameter : '*' } )
```

> **Seealso:** :dbcommand:`setClusterParameter` for more about these parameters.
