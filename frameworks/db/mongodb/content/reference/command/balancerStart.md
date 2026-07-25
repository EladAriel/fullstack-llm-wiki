---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/balancerStart.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# balancerStart (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

You can only issue the :dbcommand:`balancerStart` against the `admin` database on a :binary:`~bin.mongos` instance.

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     balancerStart: 1, 
     maxTimeMS: <number> 
   } 
)
```

### Command Fields

## Example

To start the balancer thread, connect to a :binary:`~bin.mongos` instance and issue the following command:

```javascript
db.adminCommand( { balancerStart: 1 } )
```

> **Seealso:** - :method:`sh.startBalancer()`
- :dbcommand:`balancerStart`
