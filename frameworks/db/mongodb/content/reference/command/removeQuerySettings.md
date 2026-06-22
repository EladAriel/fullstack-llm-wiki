---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/removeQuerySettings.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# removeQuerySettings (database command)

## Definition

.. versionadded:: 8.0

Deletes query settings previously added with :dbcommand:`setQuerySettings`.

To delete query settings, you must provide either a `query shape <query-shapes>` hash string or a query shape to `removeQuerySettings`.

To find a hash string or query shape, you can use a :pipeline:`$querySettings` stage in an aggregation pipeline. The hash string is named `queryShapeHash` in the `$querySettings` output.

If you provide a query shape to `removeQuerySettings`, include the fields for the existing query settings shape to delete. The field values don't have to match. For example, if you have existing query settings for `find x=1` and provide `find x=100` to `removeQuerySettings`, `removeQuerySettings` deletes the query settings for `find x=1`.

For more information about query shapes, see `query-shapes`.

## Syntax

You can delete query settings using either of the following syntax specifications.

### Provide a Query Shape Hash String

In the following syntax, you provide a query shape hash string in `removeQuerySettings`:

```javascript
db.adminCommand( {
   removeQuerySettings: <string>  // Provide an existing query shape hash string
} )
```

### Provide a Query Shape

In the following syntax, you provide:

- The same fields as a :dbcommand:`find`, :dbcommand:`distinct`, or
:dbcommand:`aggregate` command. See the syntax sections on the pages for those commands for the fields you can include in `removeQuerySettings`.

- A `$db` field that specifies the database name associated with the
original command.

```javascript
db.adminCommand( {
   removeQuerySettings: {
      <fields>,  // Provide fields for 
                 // find, distinct, or aggregate command
      $db: <string>  // Provide a database name
   }
} )
```

## Command Fields

The command takes this field:

## Examples

The following examples create a collection, add query settings, and delete the settings:

## Learn More

- `query-plans-query-optimization`
- :dbcommand:`setQuerySettings`
- :pipeline:`$querySettings`
- `query-shapes`
- `Query statistics for query shapes <queryStats-queryShape>`
- `operation-rejection-filters`
