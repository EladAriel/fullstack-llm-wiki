---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/drop-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============

# Drop an Index

You can remove a specific index from a collection. You may need to drop an index if you see a negative performance impact, want to replace it with a new index, or no longer need the index.

To drop an index, use one of the following shell methods:

## About this Task

You can drop any index except the default index on the `_id field. To drop the id` index, you must drop the entire collection.

If you drop an index that's actively used in production, you may experience performance degradation. Before you drop an index, consider `hiding the index <index-type-hidden>` to evaluate the potential impact of the drop.

## Before You Begin

To drop an index, you need its name. To get all index names for a collection, run the :method:`~db.collection.getIndexes()` method:

```javascript
db.<collection>.getIndexes()
```

## Procedures

After you identify which indexes to drop, use one of the following drop methods for the specified collection:

### Drop a Single Index

To drop a specific index, use the :method:`~db.collection.dropIndex()` method and specify the index name:

```javascript
db.<collection>.dropIndex("<indexName>")
```

### Drop Multiple Indexes

To drop multiple indexes, use the :method:`~db.collection.dropIndexes()` method and specify an array of index names:

```javascript
db.<collection>.dropIndexes( [ "<index1>", "<index2>", "<index3>" ] )
```

### Drop All Indexes Except the `_id` Index

To drop all indexes except the `_id` index, use the :method:`~db.collection.dropIndexes()` method:

```javascript
db.<collection>.dropIndexes()
```

## Results

After you drop an index, the system returns information about the status of the operation.

Example output:

```javascript
... 
{ "nIndexesWas" : 3, "ok" : 1 }
...
```

The value of `nIndexesWas` reflects the number of indexes before removing an index.

To confirm that the index was dropped, run the :method:`db.collection.getIndexes()` method:

```javascript
db.<collection>.getIndexes()
```

The dropped index no longer appears in the `getIndexes()` output.

## Learn More

- To learn more about managing your existing indexes, see `manage-indexes`.
- To learn how to remove an index in |compass|, see :compass:`Manage Indexes in Compass </indexes>`.
