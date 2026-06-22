---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.getSearchIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# db.collection.getSearchIndexes() (mongosh method)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/getSearchIndexes-description.rst

.. include:: /includes/fact-mongosh-shell-method.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

## Syntax

Command syntax:

```javascript
db.<collection>.getSearchIndexes(<indexName>)
```

## Command Fields

`getSearchIndexes()` takes this field:

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

## Examples

These examples demonstrate how to:

- `getSearchIndexes-return-all`
- `getSearchIndexes-return-one`
### Return All Search Indexes

The following example returns all {+fts+} indexes on the `movies` collection. The `movies` collection contains two search indexes: `default` and `synonym_mappings`.

```javascript
db.movies.getSearchIndexes()
```

Sample output:

.. include:: /includes/atlas-search-commands/command-output/examples/multi-doc-example-output.rst

### Return a Single Search Index

The following example returns the `synonym_mappings` index on the `movies` collection:

```javascript
db.movies.getSearchIndexes("synonym_mappings")
```

Sample output:

.. include:: /includes/atlas-search-commands/command-output/examples/single-doc-synonyms-example-output.rst
