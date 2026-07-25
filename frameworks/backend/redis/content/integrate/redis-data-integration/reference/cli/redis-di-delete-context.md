---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-delete-context.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: redis-di delete-context
linkTitle: redis-di delete-context
description: Deletes a context
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
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
