---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/mapReduce.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# mapReduce (database command)

> **Note:** .. include:: /includes/fact-use-aggregation-not-map-reduce.rst

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

> **Note:** .. include:: /includes/extracts/4.4-changes-mapreduce-ignore-verbose.rst
.. include:: /includes/extracts/4.2-changes-map-reduce-deprecation.rst

The command has the following syntax:

```javascript
db.runCommand( 
   {
     mapReduce: <string>,
     map: <string or JavaScript>,
     reduce: <string or JavaScript>,
     finalize: <string or JavaScript>,
     out: <output>,
     query: <document>,
     sort: <document>,
     limit: <number>,
     scope: <document>,
     jsMode: <boolean>,
     verbose: <boolean>,
     bypassDocumentValidation: <boolean>,
     collation: <document>,
     maxTimeMS: <integer>,
     writeConcern: <document>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields as arguments:

## Usage

The following is a prototype usage of the :dbcommand:`mapReduce` command:

```javascript
var mapFunction = function() { ... };
var reduceFunction = function(key, values) { ... };

db.runCommand(
               {
                 mapReduce: <input-collection>,
                 map: mapFunction,
                 reduce: reduceFunction,
                 out: { merge: <output-collection> },
                 query: <query>
               }
             )
```

.. include:: /includes/extracts/admonition-js-prevalence-mapReduce.rst

.. include:: /includes/parameters-map-reduce.rst

.. include:: /includes/parameters-map-reduce.rst

.. include:: /includes/parameters-map-reduce.rst

.. include:: /includes/parameters-map-reduce.rst

## Required Access

If your MongoDB deployment enforces authentication, the user executing the :dbcommand:`mapReduce` command must possess the following privilege actions:

Map-reduce with `{out : inline}` output option:

- :authaction:`find`
Map-reduce with the `replace` action when `outputting to a collection <mapreduce-out-mtd>`:

- :authaction:`find`,
- :authaction:`insert`,
- :authaction:`remove`
Map-reduce with the `merge` or `reduce` actions when `outputting to a collection <mapreduce-out-mtd>`:

- :authaction:`find`,
- :authaction:`insert`,
- :authaction:`update`
The :authrole:`readWrite` built-in role provides the necessary permissions to perform map-reduce aggregation.

## Restrictions

The :dbcommand:`mapReduce` command no longer supports `afterClusterTime <afterClusterTime>`. As such, :dbcommand:`mapReduce` cannot be associated with `causally consistent sessions <causal-consistency>`.

## Map-Reduce Examples

In :binary:`~bin.mongosh`, the :method:`db.collection.mapReduce()` method is a wrapper around the :dbcommand:`mapReduce` command. The following examples use the :method:`db.collection.mapReduce()` method:

.. include:: /includes/examples-map-reduce.rst

For more information and examples, see the `Map-Reduce <map-reduce>` page and `Perform Incremental Map-Reduce <incremental-map-reduce>`

## Output

If you set the `out <mapreduce-out-cmd>` parameter to write the results to a collection, the :dbcommand:`mapReduce` command returns a document in the following form:

```javascript
{ "result" : "map_reduce_example", "ok" : 1 }
```

If you set the `out <mapreduce-out-cmd>` parameter to output the results inline, the :dbcommand:`mapReduce` command returns a document in the following form:

```javascript
{
      "results" : [
         {
            "_id" : <key>,
            "value" :<reduced or finalizedValue for key>
         },
         ...
      ],
      "ok" : <int>
}
```

In addition to the aforementioned command specific return fields, the :method:`db.runCommand()` includes additional information:

- for replica sets: `$clusterTime`, and `operationTime`.
- for sharded clusters: `operationTime` and `$clusterTime`.
See `db.runCommand Response <command-response>` for details on these fields.

## Additional Information

- `/tutorial/troubleshoot-map-function`
- `/tutorial/troubleshoot-reduce-function`
- :method:`db.collection.mapReduce()`
- `aggregation`
