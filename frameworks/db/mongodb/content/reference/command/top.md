---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/top.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================

# top (database command)

## Definition

For every collection, :dbcommand:`top` returns the amount of `time`, in microseconds, that each `event <event-types>` takes to execute and a `count` of how many times each event has executed. The `time` and `count` metrics reset only after you restart your :binary:`~bin.mongod` instance.

### Redaction

When using `Queryable Encryption <qe-manual-feature-qe>`, the `top` command only returns the collection name.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

Issue the :dbcommand:`top` command against the `admin database`:

```javascript
db.runCommand(
   { 
     top: 1 
   }
)
```

## Event Fields

The :dbcommand:`top` command returns usage statistics for the following event fields:

## Example

The output of the :dbcommand:`top` command resembles the following output:

```javascript
{
  "totals" : {
     note: "all times in microseconds",
     "records.users" : {
                  "total" : {
                          "time" : 305277,
                          "count" : 2825
                  },
                  "readLock" : {
                          "time" : 305264,
                          "count" : 2824
                  },
                  "writeLock" : {
                          "time" : 13,
                          "count" : 1
                  },
                  "queries" : {
                          "time" : 305264,
                          "count" : 2824
                  },
                  "getmore" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "insert" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "update" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "remove" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "commands" : {
                          "time" : 0,
                          "count" : 0
                  }
          }
}
```

## Learn More

- `faq-concurrency-locking`
