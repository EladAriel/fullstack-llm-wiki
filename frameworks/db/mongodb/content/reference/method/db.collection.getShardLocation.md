---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.getShardLocation.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================================

# db.collection.getShardLocation() (mongosh method)

## Definition

## Output

The `getShardLocation()` method returns a document with the following fields:

If you run the method on an unsharded deployment:

- The `shards` array is empty.
- The `sharded` field is `false`.
## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
db.<collection>.getShardLocation()
```

## Examples

### Sharded Collection

The following example shows the shards that contain the data in the `sample_mflix.movies` collection:

### Unsharded Collection on a Sharded Cluster

If you run the command on a sharded cluster but the collection is not sharded, the `sharded` field is `false` and the `shards` array only contains the `config` shard:

### Unsharded Deployment

If you run the command on an unsharded deployment, the `sharded` field is `false` and the `shards` array is empty:
