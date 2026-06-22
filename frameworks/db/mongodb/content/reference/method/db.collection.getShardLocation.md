---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.getShardLocation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
