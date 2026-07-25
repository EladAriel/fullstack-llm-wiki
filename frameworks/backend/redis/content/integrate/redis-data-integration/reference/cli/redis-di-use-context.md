---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-use-context.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: redis-di use-context
linkTitle: redis-di use-context
description: Sets a context to be the active one
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Sets a context in the `~/.redis-di` context file to be the active one, so its connection details are
used by subsequent commands. Create or update a context with
[`set-context`]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di-set-context" >}}).

## Usage

```
redis-di use-context <name> [flags]
```

## Options

This command takes only the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di use-context prod
```
