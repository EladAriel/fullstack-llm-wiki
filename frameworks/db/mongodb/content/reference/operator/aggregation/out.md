---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/out.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# $out (aggregation stage)

## Definition

## Syntax

The `$out` stage has the following syntax:

- `$out` can take a string to specify only the output
collection (i.e. output to a collection in the same database):

```javascript
  { $out: "<output-collection>" } // Output collection is in the same database
```

- `$out` can take a document to specify the output database as well as the
output collection:

```javascript
  { $out: { db: "<output-db>", coll: "<output-collection>" } }
```

- Starting in MongoDB 7.0.3 and 7.1, `$out` can take a document to
output to a `time series collection<manual-timeseries-landing>`:

```javascript
 { $out: 
   { db: "<output-db>", coll: "<output-collection>",
     timeseries: {
       timeField: "<field-name>", 
       metaField: "<field-name>", 
       granularity:  "seconds" || "minutes" || "hours" ,
     } 
   } 
 }

.. important:: Changing Time Series Granularity

   After creating a time series collection, you can modify its
   granularity using the :dbcommand:`collMod` method. However,
   you can only increase the timespan covered by each bucket. You
   cannot decrease it.

.. list-table::
 :header-rows: 1
 :widths: 15 85

 * - Field
   - Description

 * - ``db``
   - ..  _out-db:

     The output database name.

     - For a :ref:`replica set <replica-set>` or a standalone, if the
       output database does not exist, ``$out`` also creates
       the database.

 * - ``coll``
   - ..  _out-collection:

     The output collection name.

 * - ``timeseries``
   - .. _out-timeseries:

     A document that specifies the configuration to use when writing
     to a time series collection. The ``timeField`` is required. All
     other fields are optional.

 * - ``timeField``
   - .. _out-timefield:

     Required when writing to a time series collection. The name of the field
     which contains the date in each time series document. Documents in a
     time series collection must have a valid BSON date as the value for the
     ``timeField``.

 * - ``metaField``
   - .. _out-metafield:

     .. include:: /includes/time-series/fact-meta-field-description.rst

 * - ``granularity``
   - .. _out-granularity:

     .. include:: /includes/time-series/fact-granularity-field-description.rst

 * - ``bucketMaxSpanSeconds``
   - .. _out-bucketmaxspanseconds:

     .. include:: /includes/time-series/fact-bucketmaxspanseconds-field-description.rst

 * - ``bucketRoundingSeconds``
   - .. _out-bucketroundingseconds:

     .. include:: /includes/time-series/fact-bucketroundingseconds-field-description.rst
```

> **Important:** - You cannot specify a sharded collection as the output
  collection. The input collection for a pipeline can be sharded.
  To output to a sharded collection, see :pipeline:`$merge`.
- The `$out` operator cannot write results to a
  `capped collection <manual-capped-collection>`.
- If you modify a collection with a :atlas:`{+fts+}
  </atlas-search>` index, you must first delete and then re-create
  the search index. Consider using :pipeline:`$merge` instead.

### Comparison with `$merge`

MongoDB provides two stages, :pipeline:`$merge` and `$out`, for writing the results of the aggregation pipeline to a collection. The following summarizes the capabilities of the two stages:

## Behaviors

### $out Read Operations Run on Secondary Replica Set Members

Starting in MongoDB 5.0, `$out` can run on replica set secondary nodes if all the nodes in cluster have `featureCompatibilityVersion <view-fcv>` set to `5.0` or higher and the `/core/read-preference` is set to secondary.

Read operations of the `$out` statement occur on the secondary nodes, while the write operations occur only on the primary nodes.

Not all driver versions support targeting of `$out` operations to replica set secondary nodes. Check your :driver:`driver </>` documentation to see when your driver added support for `$out` running on a secondary.

### Create New Collection

The `$out` operation creates a new collection if one does not already exist.

The collection is not visible until the aggregation completes. If the aggregation fails, MongoDB does not create the collection.

### Replace Existing Collection

If the output collection already exists, the `$out` stage atomically replaces it upon completion of the aggregation. Specifically, the `$out` operation:

#. Creates a temp collection. #. Copies the indexes from the existing collection to the temp collection. #. Inserts the documents into the temp collection. #. Calls the :dbcommand:`renameCollection` command with `dropTarget: true` to rename the temp collection to the destination collection.

If specified collection exists and the `$out` operation specifies `timeseries` options, then the following restrictions apply:

#. The existing collection must be a time series collection. #. The existing collection must not be a view. #. The `timeseries` options included in the `$out` stage must exactly match those on the existing collection.

The `$out` operation does not change any indexes that existed on the previous collection. If the aggregation fails, the `$out` operation makes no changes to the pre-existing collection.

Schema Validation Errors ````````````````````````

If your `coll` collection uses `schema validation <schema-validation-overview>` and has `validationAction` set to `error`, inserting an invalid document with `$out` throws an error. The `$out` operation makes no changes to the pre-existing collection and documents returned by the aggregation pipeline are not added to the `coll` collection.

### Index Constraints

The pipeline will fail to complete if the documents produced by the pipeline would violate any unique indexes, including the index on the `_id` field of the original output collection.

If the `$out` operation modifies a collection with a :atlas:`{+fts+} </atlas-search>` index, you must delete and re-create the search index. Consider using :pipeline:`$merge` instead.

### `majority` Read Concern

.. include:: /includes/fact-aggregate-readConcern.rst

### Interaction with `mongodump`

A :binary:`~bin.mongodump` started with :option:`--oplog <mongodump.--oplog>` fails if a client issues an aggregation pipeline that includes `$out` during the dump process. See :option:`mongodump --oplog <mongodump.--oplog>` for more information.

### Restrictions

## Examples
