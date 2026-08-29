---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-use-context.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.191497Z"
---
# Redis Di Use Context

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
