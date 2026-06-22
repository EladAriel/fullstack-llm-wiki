---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getLogComponents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# db.getLogComponents() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Output

The :method:`db.getLogComponents()` returns a document with the verbosity settings. For example:

```none
{
   "verbosity" : 0,
   "accessControl" : {
      "verbosity" : -1
   },
   "command" : {
      "verbosity" : -1
   },
   "control" : {
      "verbosity" : -1
   },
   "geo" : {
      "verbosity" : -1
   },
   "index" : {
      "verbosity" : -1
   },
   "network" : {
      "verbosity" : -1
   },
   "query" : {
      "verbosity" : 2
   },
   "replication" : {
      "verbosity" : -1,
      "election" : {
         "verbosity" : -1
      },
      "heartbeats" : {
         "verbosity" : -1
      },
      "initialSync" : {
         "verbosity" : -1
      },
      "rollback" : {
         "verbosity" : -1
      }
   },
   "sharding" : {
      "verbosity" : -1
   },
   "storage" : {
      "verbosity" : 2,
      "recovery" : {
         "verbosity" : -1
      },
      "journal" : {
         "verbosity" : -1
      }
   },
   "write" : {
      "verbosity" : -1
   }
}
```

To modify these settings, you can configure the :setting:`systemLog.verbosity` and `systemLog.component.<name>.verbosity` settings in the `configuration file <configuration-options>` or set the :parameter:`logComponentVerbosity` parameter using the :dbcommand:`setParameter` command or use the :method:`db.setLogLevel()` method. For examples, see `log-messages-configure-verbosity`.
