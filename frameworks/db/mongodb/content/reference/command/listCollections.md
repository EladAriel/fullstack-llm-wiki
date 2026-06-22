---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/listCollections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# listCollections (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     listCollections: 1, 
     filter: <document>, 
     nameOnly: <boolean>, 
     authorizedCollections: <boolean>, 
     comment: <any> 
   }
)
```

## Command Fields

The command can take the following optional fields:

## Behavior

### Filter

Use a filter to limit the results of `listCollections`. Specify a `filter` on any of the `fields returned <list-collection-output>` in the `listCollections` result set.

### Locks

`listCollections` lock behavior:

- Earlier than MongoDB 5.0, `listCollections` takes an :term:`intent
shared lock <intent lock>` on each collection in the database when `listCollections` holds an intent shared lock on the database.

- Starting in MongoDB 5.0, `listCollections` doesn't take an intent
shared lock on a collection or database. `listCollections` isn't blocked by operations holding an exclusive write lock on a collection.

To learn about locks, see `faq-concurrency`.

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

## Required Access

.. include:: /includes/extracts/listCollections-auth-required-access.rst

## Output

If you don't require a raw command response, use the :method:`db.getCollectionInfos()` or the :method:`db.getCollectionNames()` helper methods.

## Example

### List All Collections

The `sample_mflix` database contains collections such as `movies`, `theaters`, `users`, and others.

To get a list of collection names, run the `listCollections` command with the `nameOnly` option.

To get more detailed information, remove the `nameOnly` option.

## Learn More

For collection options:

- :method:`db.createCollection()`
- :dbcommand:`create`
For collection information:

- :method:`db.getCollectionInfos()`
- `mongosh built-in commands <mongosh-help>`
