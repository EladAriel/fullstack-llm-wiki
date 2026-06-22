---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortRewriteCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# abortRewriteCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
db.adminCommand( {
   abortRewriteCollection: "<database>.<collection>"
} )
```

## Command Fields

The command takes the following field:

## Access Control

The `abortRewriteCollection` command requires the :authaction:`rewriteCollection` privilege action on the cluster or on the database and collection on which you want to stop the rewrite.

This privilege action is also available to users with the following roles:

- :authrole:`enableSharding`
- :authrole:`clusterManager`
## Examples

Consider the following example of a collection rewrite:

```javascript
db.adminCommand( {
  rewriteCollection: "sales.orders"
} )
```

To stop this rewrite, pass the database and collection name to the `abortRewriteCollection` command:

```javascript
db.adminCommand( {
   abortRewriteCollection: "sales.orders"
} )
```

## Learn More

- `sharding-introduction`
- :dbcommand:`rewriteCollection`
- :dbcommand:`reshardCollection`
- :dbcommand:`abortReshardCollection`
