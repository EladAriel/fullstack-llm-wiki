---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/cluster-parameters/defaultMaxTimeMS.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# defaultMaxTimeMS

## Definition

## Access Control

.. include:: /includes/cluster-parameters/access-control.rst

## Syntax

To set `defaultMaxTimeMS` for your deployment, run the following command on the `admin` database:

```javascript
db.adminCommand(
   {
      setClusterParameter: {
         defaultMaxTimeMS: { readOperations: <value> }
      }
   }
)
```

To view the current value for `defaultMaxTimeMS`, run the following command on the `admin` database:

```javascript
db.adminCommand( { getClusterParameter: "defaultMaxTimeMS" } )
```

## Behavior

By default, `defaultMaxTimeMS.readOperations` is 0, meaning no default query timeout is set. If there is no default query timeout, the query runs until it either returns a result or fails.

If a query specifies a :method:`~cursor.maxTimeMS()` option, that value overrides the `defaultMaxTimeMS` value.

### Long-Running Queries

If your deployment needs to run long queries, such as `analytics node <analytics-nodes-overview>` queries, you must specify a timeout for those queries at the operation level using :method:`~cursor.maxTimeMS()`. If you don't specify an operation timeout, those queries use the `defaultMaxTimeMS` timeout, and won't run for the required amount of time.

## Example

The following command sets the default query timeout `5000` milliseconds:

```javascript
db.runCommand( {
   setClusterParameter: {
      defaultMaxTimeMS: { readOperations: 5000 }
   }
} )
```

To check the value of `defaultMaxTimeMS`, run the following command:

### Results

After you set `defaultMaxTimeMS` for your deployment, consider these queries:

```javascript
db.test.find( { name: "Carol" } )

db.test.find( { name: "Carol" } ).maxTimeMS( 8000 )
```

The first query uses the `defaultMaxTimeMS` value of 5,000 milliseconds.

The second query specifies :method:`~cursor.maxTimeMS()`, which overrides the `defaultMaxTimeMS` and causes the query to timeout after 8,000 milliseconds.
