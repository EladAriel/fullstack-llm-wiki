---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setQuerySettings.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# setQuerySettings (database command)

## Definition

.. versionadded:: 8.0

`setQuerySettings` defines query settings used by the :dbcommand:`find`, :dbcommand:`distinct`, and :dbcommand:`aggregate` commands.

You can use query settings to add index hints, define `operation rejection filters <operation-rejection-filters>`, and set other fields for all executions of a given `query shape <query-shapes>` on a cluster. A cluster's query settings persist across restarts.

The `query optimizer` uses query settings as an additional input during query planning. Index hints in query settings restrict the set of indexes available to the planner, but don't guarantee that the planner will use the index. The planner can still select a collection scan as the winning plan for a given query shape hash.

.. include:: /includes/hints-precedence.rst

> **Note:** To remove query settings, use :dbcommand:`removeQuerySettings`. To
see current query settings, use a :pipeline:`$querySettings` stage in
an aggregation pipeline.

### Query Settings and Index Filters

Starting in MongoDB 8.0, `index filters <index-filters>` are deprecated. Use query settings instead.

Query settings have more functionality than index filters. Index filters aren't persistent, and you can't easily create index filters for all cluster nodes.

## Syntax

You can add or update query settings using either of the two syntax specifications shown in this section.

### Set Query Settings by Passing in a Query

In the following syntax, you provide:

- The same fields as a :dbcommand:`find`, :dbcommand:`distinct`, or
:dbcommand:`aggregate` command. See the syntax sections on the pages for those commands for the fields you can include in `setQuerySettings`.

- A `$db` field to specify the database for the query settings.
- A `settings` document with `indexHints` and other fields.
```javascript
db.adminCommand( {
   setQuerySettings: {
      <fields>,  // Provide fields for 
                 // find, distinct, or aggregate command
      $db: <string>  // Provide a database name
   },
   // Provide a settings document with indexHints and other fields
   settings: { 
      indexHints: [ { 
         ns: { db: <string>, coll: <string> },
         allowedIndexes: <array>
      }, ... ],
      queryFramework: <string>,
      reject: <boolean>,
      comment: <BSON type>
   }
} )
```

### Set Query Settings by Passing in a Query Shape Hash

You can provide an existing query shape hash string in `setQuerySettings` and an updated `settings` document with `indexHints` and other fields:

```javascript
db.adminCommand( {
   setQuerySettings: <string>,  // Provide an existing query shape hash string
   // Provide a settings document with indexHints and other fields
   settings: { 
      indexHints: [ { 
         ns: { db: <string>, coll: <string> },
         allowedIndexes: <array>
      }, ... ],
      queryFramework: <string>,
      reject: <boolean>,
      comment: <BSON type>
   }
} )
```

.. include:: /includes/query-shape-hash-string.rst

> **Tip:** In both syntax variations, you can provide an array of `indexHints`
documents. You can omit the array brackets if you provide only one
`indexHints` document.

## Command Fields

The command takes these fields:

## Examples

The following examples create a collection and add query settings for different commands. For all executions of a query shape on the cluster, the examples restrict the query planner to either using the hinted index, or a collection scan.

## Learn More

- `query-plans-query-optimization`
- `indexes`
- :pipeline:`$querySettings`
- :dbcommand:`removeQuerySettings`
- `aggregation-pipeline`
- `query-shapes`
- `Query statistics for query shapes <queryStats-queryShape>`
- `operation-rejection-filters`
