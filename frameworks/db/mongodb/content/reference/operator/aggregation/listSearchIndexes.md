---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/listSearchIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# $listSearchIndexes (aggregation stage)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/getSearchIndexes-description.rst

## Syntax

Command syntax:

```javascript
db.<collection>.aggregate(
   [
      {
         $listSearchIndexes:
            {
               id: <indexId>,
               name: <indexName>
            }
      }
   ]
)
```

## Command Fields

`$listSearchIndexes` takes either of the following fields:

You cannot specify both `id` and `name`. If you omit both the `id` and `name` fields, `$listSearchIndexes` returns information about all {+fts+} indexes on the collection.

## Access Control

.. include:: /includes/atlas-search-commands/access-control/list-access-control.rst

## Output

.. include:: /includes/atlas-search-commands/command-output/listSearchIndex-output.rst

### Index Status Details

.. include:: /includes/atlas-search-commands/command-output/search-index-details.rst

### Synonym Mapping Details

.. include:: /includes/atlas-search-commands/command-output/search-index-synonym-details.rst

### {+fts+} Index Statuses

.. include:: /includes/atlas-search-commands/command-output/search-index-statuses.rst

### Errors

.. versionchanged:: 7.1

## Examples

## Learn More

To use a `mongosh` method to view {+fts+} indexes, see :method:`db.collection.getSearchIndexes()`.

To create {+fts+} indexes, see:

- The :method:`db.collection.createSearchIndex()` `mongosh` method
- The :dbcommand:`createSearchIndexes` database command
