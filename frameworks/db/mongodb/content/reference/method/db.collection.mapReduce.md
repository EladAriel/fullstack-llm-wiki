---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.mapReduce.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# db.collection.mapReduce() (mongosh method)

> **Note:** .. include:: /includes/fact-use-aggregation-not-map-reduce.rst

.. include:: /includes/fact-mongosh-shell-method-alt

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

> **Note:** .. include:: /includes/extracts/4.4-changes-mapreduce-ignore-verbose.rst
.. include:: /includes/extracts/4.2-changes-map-reduce-deprecation.rst

:method:`db.collection.mapReduce()` has the following syntax:

```javascript
db.collection.mapReduce(
                         <map>,
                         <reduce>,
                         {
                           out: <collection>,
                           query: <document>,
                           sort: <document>,
                           limit: <number>,
                           finalize: <function>,
                           scope: <document>,
                           jsMode: <boolean>,
                           verbose: <boolean>,
                           bypassDocumentValidation: <boolean>
                         }
                       )
```

### Parameters

:method:`db.collection.mapReduce()` takes the following parameters:

## Fields

The following table describes additional arguments that :method:`db.collection.mapReduce()` can accept.

> **Note:** .. include:: /includes/fact-group-map-reduce-where-limitations-in-24.rst

.. include:: /includes/parameters-map-reduce.rst

.. include:: /includes/parameters-map-reduce.rst

.. include:: /includes/parameters-map-reduce.rst

.. include:: /includes/parameters-map-reduce.rst

.. include:: /includes/examples-map-reduce.rst

## Output

The output of the :method:`db.collection.mapReduce()` method is identical to that of the :dbcommand:`mapReduce` command. See the `Output <mapReduce-output>` section of the :dbcommand:`mapReduce` command for information on the :method:`db.collection.mapReduce()` output.

## Restrictions

:method:`db.collection.mapReduce()` no longer supports `afterClusterTime <afterClusterTime>`. As such, :method:`db.collection.mapReduce()` cannot be associatd with `causally consistent sessions <causal-consistency>`.

## Additional Information

- `troubleshoot-map-function`
- `troubleshoot-reduce-function`
- :dbcommand:`mapReduce` command
- `aggregation`
- `Map-Reduce <map-reduce>`
- `incremental-map-reduce`
