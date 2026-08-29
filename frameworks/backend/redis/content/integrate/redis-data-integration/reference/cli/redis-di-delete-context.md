---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-delete-context.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.190096Z"
---
# Redis Di Delete Context

---
Title: redis-di delete-context
linkTitle: redis-di delete-context
description: Deletes a context
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
- /integrate/redis-data-integration/ingest/reference/cli/redis-di-delete-context/
---

Deletes a context from the `~/.redis-di` context file. Because this is destructive, the command asks
for confirmation unless you pass `--force`.

## Usage

```
redis-di delete-context <name> [flags]
```

## Options

| Option    | Description                   |
| :-------- | :---------------------------- |
| `--force` | Skip the confirmation prompt. |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di delete-context dev --force
```
