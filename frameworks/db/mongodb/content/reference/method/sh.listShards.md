---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.listShards.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
