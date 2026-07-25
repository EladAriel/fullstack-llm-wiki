---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/mergeAllChunksOnShard-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

This example assumes that history is empty for all chunks and all chunks are non-jumbo. Since both conditions are true, all contiguous intervals on the same shard are `mergeable <mergeability>`.

## Setup

These chunks belong to a collection named `coll` with shard key `x`. There are nine chunks in total.

## Steps

## Result

After these commands have completed, the contiguous chunks have been merged. There are four total chunks instead of the original nine.
