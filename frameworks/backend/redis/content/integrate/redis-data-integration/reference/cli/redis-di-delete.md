---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-delete.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.190825Z"
---
# Redis Di Delete

---
Title: redis-di delete
linkTitle: redis-di delete
description: Deletes a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
- /integrate/redis-data-integration/ingest/reference/cli/redis-di-delete/
---

Deletes a pipeline. Because this is destructive, the command asks for confirmation unless you pass
`--force`.

## Usage

```
redis-di delete [pipeline] [flags]
```

The pipeline name is an optional argument that defaults to `default`.

## Options

| Option      | Description                                                                       |
| :---------- | :-------------------------------------------------------------------------------- |
| `--force`   | Skip the confirmation prompt.                                                     |
| `--wait`    | Wait for the pipeline to reach the expected state (default `true`).               |
| `--timeout` | Maximum time to wait for the pipeline to reach the expected state (default `2m`). |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di delete my-pipeline --force
```
