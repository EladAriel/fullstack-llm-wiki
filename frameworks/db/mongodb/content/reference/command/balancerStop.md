---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/balancerStop.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# balancerStop (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     balancerStop: 1, 
     maxTimeMS: <number> 
   }
)
```

### Command Fields

## Example

To stop the balancer thread, connect to a :binary:`~bin.mongos` instance and issue the following command:

```javascript
db.adminCommand( { balancerStop: 1 } )
```

## Learn More

- :method:`sh.stopBalancer()`
- :dbcommand:`balancerStart`
