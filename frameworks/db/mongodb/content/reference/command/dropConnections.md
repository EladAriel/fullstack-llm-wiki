---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropConnections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# dropConnections (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has following syntax:

```javascript
db.adminCommand(
   { 
     dropConnections: 1, 
     hostAndPort : [ "host1:port1", "host2:port2", ... ],
     comment: <any>
   }
)
```

## Command Fields

The command requires the following field:

## Access Control

If the deployment enforces `authentication/authorization <authentication>`, the :dbcommand:`dropConnections` command requires the :authaction:`dropConnections` action on the `cluster <resource-cluster>` resource.

Create a `user-defined role <user-defined-roles>` in the `admin` database  where the `privilege` array includes the following document:

```javascript
{ "resource" : { "cluster" : true } }, "actions" : [ "dropConnections" ] }
```

- Use :method:`db.createUser()` to create a user on the `admin`
database with the custom role.

or

- Use :method:`db.grantRolesToUser()` to grant the role to an  existing
user on the `admin` database.

For example, the following operation creates a user-defined role on the `admin` database with the privileges to support :dbcommand:`dropConnections`:

```javascript
db.getSiblingDB("admin").createRole(
  {
    "role" : "dropConnectionsRole",
    "privileges" : [
      { 
        "resource" : { "cluster" : true }, 
        "actions" : [ "dropConnections" ] 
      }
    ],
    "roles" : []
  }
)
```

Assign the custom role to a user on the `admin` database:

```javascript
db.getSiblingDB("admin").createUser(
  {
    "user" : "dropConnectionsUser",
    "pwd" : "replaceThisWithASecurePassword",
    "roles" : [ "dropConnectionsRole" ]
  }
)
```

The created user can execute :dbcommand:`dropConnections`.

For more examples of user creation, see `/tutorial/create-users`. For a tutorial on adding privileges to an existing database user, see `modify-existing-user-access`.

## Behavior

:dbcommand:`dropConnections` silently ignores `hostAndPort` elements that do not include both the hostname and port of the remote machine.

## Example

Consider a replica set with a recently removed member at `oldhost.example.com:27017`. Running the following :dbcommand:`dropConnections` command against each active replica set member ensures there are no remaining outgoing connections to `oldhost.example.com:27017`:

```javascript
db.adminCommand( 
  {
    "dropConnections" : 1,
    "hostAndPort" : [
      "oldhost.example.com:27017"
    ] 
  } 
)
```

The command returns output similar to the following:

```javascript
{
 "ok" : 1,
 "$clusterTime" : {
   "clusterTime" : Timestamp(1551375968, 1),
   "signature" : {
     "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
     "keyId" : Long(0)
   }
 },
 "operationTime" : Timestamp(1551375968, 1)
}
```

You can confirm the status of the connection pool for the :binary:`~bin.mongod` or :binary:`~bin.mongos` using the :dbcommand:`connPoolStats` command.
