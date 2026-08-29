---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-check-type.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.797509Z"
---
.. _manual-timeseries-check-type:

# List Time Series Collections in a Database

**meta:** :description: List all time series collections in a database using the `listCollections` command with a filter for `{ type: "timeseries" }`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

You can output a list of collections in a database and filter the
results by a variety of properties, including collection type. You can
use this functionality to list all time series collections in a
database.

## Procedure

To list all time series collections in a database, use the
:dbcommand:`listCollections` command with a filter for
``{ type: "timeseries" }``:

.. code-block:: javascript

   db.runCommand( {
      listCollections: 1,
      filter: { type: "timeseries" } 
   } )

## Output

For time series collections, the output includes:

- ``type: 'timeseries'``
- ``options: { timeseries: { ... } }``

For example:

.. code-block:: javascript
   :copyable: false
   :emphasize-lines: 8-15

   {
     cursor: {
       id: Long("0"),
       ns: 'test.$cmd.listCollections',
       firstBatch: [
         {
           name: 'weather',
           type: 'timeseries',
           options: {
             timeseries: {
               timeField: 'timestamp',
               metaField: 'metadata',
               granularity: 'hours',
               bucketMaxSpanSeconds: 2592000
             }
           },
           info: { readOnly: false }
         }
       ]
     },
     ok: 1
   }