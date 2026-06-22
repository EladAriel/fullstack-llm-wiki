---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.dropSearchIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================

# db.collection.dropSearchIndex() (mongosh method)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst

.. include:: /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

## Syntax

Command syntax:

```javascript
db.<collection>.dropSearchIndex(<name>)
```

## Command Fields

`dropSearchIndex()` takes the following field:

## Behavior

.. include:: /includes/atlas-search-commands/behavior/delete-behavior.rst

## Access Control

If your deployment enforces access control, the user running the `dropSearchIndex()` method must have the :authaction:`dropSearchIndex` privilege action on the database:

```javascript
{ resource: { database : true }, actions: [ "dropSearchIndex" ] }
```

The built-in :authrole:`dbAdmin` and :authrole:`readWrite` roles provide the `dropSearchIndex` privilege. The following example grants the `readWrite` role on the `qa` database:

```javascript
db.grantRolesToUser(
   "<user>",
   [ { role: "readWrite", db: "qa" } ]
)
```

## Example

The following example deletes a search index named `searchIndex01` on the `movies` collection:

```javascript
db.movies.dropSearchIndex("searchIndex01")
```
