---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.adminCommand.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# db.adminCommand() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

:method:`db.adminCommand` runs commands against the `admin` database regardless of the database context in which it runs. The following commands are equivalent:

```javascript
db.getSiblingDB("admin").runCommand(<command>)

db.adminCommand(<command>)
```

For a list of available administrative database commands, see `database-commands`.

> **Note:** For a :binary:`~bin.mongod` or :binary:`~bin.mongos` running with
:setting:`~security.authorization`, the authorized user must have
the appropriate privileges to run the database command. See the
reference documentation for the command for more information on
security requirements.

## Response

The method returns a response document that contains the following fields:

.. include:: /includes/fact-runCommand-results.rst

## Examples

### killOp

The following example uses the :method:`db.adminCommand()` method to execute a :dbcommand:`killOp` command to terminate an operation with `opid 724`. :dbcommand:`killOp` is an administrative command and must be run against the `admin` database.

```javascript
db.adminCommand( { "killOp": 1, "op": 724 } )
```

### renameCollection

The following example uses :method:`db.adminCommand()` to execute the :dbcommand:`renameCollection` administrative database command to rename the `orders` collection in the `test` database to `orders-2016`.

```javascript
db.adminCommand(
  {
     renameCollection: "test.orders",
     to: "test.orders-2016"
  }
)
```

### createUser

The following example uses the :method:`db.adminCommand()` method to create a user named `bruce` with the :authrole:`dbOwner` role on the `admin` database.

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
db.adminCommand(
  {
    createUser: "bruce",
    pwd: passwordPrompt(),  // or <cleartext password>
    roles: [
      { role: "dbOwner", db: "admin" }
    ]
  }
)
```
