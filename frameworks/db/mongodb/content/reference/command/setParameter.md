---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setParameter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# setParameter (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

```javascript
db.adminCommand( 
   { 
     setParameter: 1, 
     <parameter>: <value> 
   } 
)
```

For the available parameters, including examples, see `/reference/parameters`.

## Behavior

### Persistence

Commands issued by the admin command :dbcommand:`setParameter` do not survive server restarts. For a persistent option use the :option:`--setParameter <mongod --setParameter>` command line option or the :setting:`setParameter` configuration file setting.

### Stable API

When using `Stable API <stable-api>` V1 with `apiStrict <api-strict-desc>` set to `true`, you cannot use :dbcommand:`setParameter` to modify server parameters.
