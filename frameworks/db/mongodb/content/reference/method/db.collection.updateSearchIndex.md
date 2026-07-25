---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.updateSearchIndex.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================================

# db.collection.updateSearchIndex() (mongosh method)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst

.. include:: /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

## Syntax

Command syntax:

```javascript
db.<collection>.updateSearchIndex(
   <name>,
   {
      <definition>
   }
)
```

## Command Fields

`updateSearchIndex()` takes these fields:

### Search Index Definition Syntax

.. include:: /includes/atlas-search-commands/search-index-definition-fields.rst

### Vector Search Index Definition Syntax

.. include:: /includes/atlas-search-commands/vector-search-index-definition-fields.rst

## Behavior

.. include:: /includes/atlas-search-commands/behavior/update-behavior.rst

## Access Control

.. include:: /includes/atlas-search-commands/access-control/update-access-control.rst

## Example

The following example creates a new {+fts+} index and then updates that index.

#. Create a search index named `searchIndex01` on the `movies` collection:

```javascript
   db.movies.createSearchIndex(
      "searchIndex01",
      {
         mappings: { dynamic: true },
         storedSource: {
            exclude: [ "imdb.rating" ]
         }
      }
   )
```

#. Update the `searchIndex01` index:

```javascript
   db.movies.updateSearchIndex(
      "searchIndex01",
      {
         mappings: { dynamic: true },
         storedSource: {
            exclude: [ "movies" ]
         }
      }
   )
```
