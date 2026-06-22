---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getCmdLineOpts.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# getCmdLineOpts (database command)

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
     getCmdLineOpts: 1  
   } 
)
```

## Output

This command returns a document with two fields, `argv` and `parsed`. The `argv` field contains an array with each item from the command string used to invoke :binary:`~bin.mongod` or :binary:`~bin.mongos`. The document in the `parsed` field includes all runtime options, including those parsed from the command line and those specified in the configuration file, if specified.

Consider the following example output of :dbcommand:`getCmdLineOpts`:

```javascript
{
   "argv" : [
      "/usr/bin/mongod",
      "--config",
      "/etc/mongod.conf"
   ],
   "parsed" : {
      "config" : "/etc/mongod.conf",
      "net" : {
         "bindIp" : "127.0.0.1",
         "port" : 27017
      },
      "processManagement" : {
         "fork" : true
      },
      "storage" : {
         "dbPath" : "/data/db"
      },
      "systemLog" : {
         "destination" : "file",
         "logAppend" : true,
         "path" : "/var/log/mongodb/mongod.log"
      }
   },
   "ok" : 1
}
```
