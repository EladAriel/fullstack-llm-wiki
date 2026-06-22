---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.isConfigShardEnabled.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# sh.isConfigShardEnabled() (mongosh method)

## Definition

The `sh.isConfigShardEnabled()` method returns whether a cluster has a `config shard <config-shard-concept>`. If it does, then `sh.isConfigShardEnabled()` also returns the config shard's host and tag information.

## Syntax

`sh.isConfigShardEnabled()` has the following syntax:

```javascript
sh.isConfigShardEnabled()
```

## Behavior

`sh.isConfigShardEnabled()` returns a document that contains the following fields:

```javascript
{
   enabled: <boolean>,
   host: <string>,
   tags: [<string>]
}
```

## Example

The following example shows how to run `sh.isConfigShardEnabled()`. It shows the output when you run the method on a cluster that has a config shard, but this shard does not have any associated tags:

The following example shows the output if you run `sh.isConfigShardEnabled()` on a cluster that has a config shard with associated tags:

```javascript
{ 
  enabled: true, 
  host: 'shard3/localhost:27017',
  tags: ['tag1', 'tag2'] 
}
```
