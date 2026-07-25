---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/rewriteCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# rewriteCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( {
   rewriteCollection: "<database>.<collection>",
   numInitialChunks: <int>,
   zones: <zones>
} )
```

## Command Fields

The command takes the following fields:

## Considerations

.. include:: /includes/fact-reshard-considerations.rst

.. include:: /includes/resharding-oplog-note.rst

### Rewrite Limitations

.. include:: /includes/fact-reshard-limitations.rst

## Access Control

The `rewriteCollection` command requires the :authaction:`rewriteCollection` privilege action on the cluster or on the database and collection you want to rewrite.

This privilege action is also available to users with the following roles:

- :authrole:`enableSharding`
- :authrole:`clusterManager`
## Examples

To rewrite a collection, run the following command:

```javascript
db.adminCommand( {
  rewriteCollection: "sales.orders"
} )
```

## Learn More

- `reshard-to-same-key`
- `resharding-a-collection-back-to-same-key`
- `resharding-for-adding-and-removing-shards-tutorial`
- :dbcommand:`reshardCollection`
- :dbcommand:`moveCollection`
