---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.addShard.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# sh.addShard() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

### Balancing

.. include:: /includes/fact-adding-shards-changes-cluster-balance.rst

### Hidden Members

.. include:: /includes/important-add-shard-not-compatible-with-hidden-members.rst

### DDL Operations

If you run `sh.addShard` while your cluster executes a DDL operation (operation that modifies a collection such as :dbcommand:`reshardCollection`), `sh.addShard` only executes after the concurrent DDL operation finishes.

## Example

To add a shard, specify the name of the replica set and the hostname of at least one member of the replica set, as a seed. If you specify additional hostnames, all must be members of the same replica set.

The following example adds a replica set named `repl0` and specifies one member of the replica set:

```javascript
sh.addShard("repl0/mongodb3.example.net:27327")
```
