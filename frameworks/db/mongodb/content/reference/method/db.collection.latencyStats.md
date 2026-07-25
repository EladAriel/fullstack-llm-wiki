---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.latencyStats.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================================

# db.collection.latencyStats() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-alt

## Definition

> **Seealso:** :pipeline:`$collStats`

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Output

:method:`~db.collection.latencyStats()` returns a document containing a field `latencyStats`, containing the following fields:

.. include:: /includes/fact-latencystats-reference.rst

## Examples

You can run :method:`~db.collection.latencyStats()` in :binary:`~bin.mongosh` as follows:

```javascript
db.data.latencyStats( { histograms: true } ).pretty()
```

:method:`~db.collection.latencyStats()` returns a document such as the following:

```javascript
{
  "ns" : "test.data",
  "localTime" : ISODate("2016-11-01T21:56:28.962Z"),
  "latencyStats" : {
    "reads" : {
      "histogram" : [
        {
          "micros" : Long(16),
          "count" : Long(6)
        },
        {
          "micros" : Long(512),
          "count" : Long(1)
        }
      ],
      "latency" : Long(747),
      "ops" : Long(7)
    },
    "writes" : {
      "histogram" : [
        {
          "micros" : Long(64),
          "count" : Long(1)
        },
        {
          "micros" : Long(24576),
          "count" : Long(1)
        }
      ],
      "latency" : Long(26845),
      "ops" : Long(2)
    },
    "commands" : {
      "histogram" : [ ],
      "latency" : Long(0),
      "ops" : Long(0)
    }
  }
}
```
