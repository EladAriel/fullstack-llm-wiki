---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-delete-secret.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: redis-di delete-secret
linkTitle: redis-di delete-secret
description: Deletes a secret of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Deletes a secret of a pipeline. Because this is destructive, the command asks for confirmation unless
you pass `--force`.

## Usage

```
redis-di delete-secret <key> [flags]
```

## Options

| Option             | Description                                                                       |
| :----------------- | :-------------------------------------------------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`).                                           |
| `--force`          | Skip the confirmation prompt.                                                     |
| `--wait`           | Wait for the pipeline to reach the expected state (default `true`).               |
| `--timeout`        | Maximum time to wait for the pipeline to reach the expected state (default `2m`). |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di delete-secret SOURCE_DB_CACERT --force
```
