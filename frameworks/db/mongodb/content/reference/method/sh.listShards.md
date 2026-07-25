---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.listShards.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# sh.listShards() (mongosh method)

## Definition

`sh.listShards()` returns a list of the configured shards in a sharded cluster. This information matches the `shards` field returned by the :dbcommand:`listShards` database command.

## Syntax

`sh.listShards()` has the following syntax:

```javascript
sh.listShards()
```

## Behavior

The output for `sh.listShards()` returns an array of documents, each describing one shard. Each document may contain the following fields:

.. include:: /includes/list-shards-output.rst

## Example

The following code runs `sh.listShards()` and provides an example output array:
