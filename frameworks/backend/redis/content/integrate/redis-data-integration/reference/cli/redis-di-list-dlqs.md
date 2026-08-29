---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-list-dlqs.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.188593Z"
---
# Redis Di List Dlqs

---
Title: redis-di list-dlqs
linkTitle: redis-di list-dlqs
description: Lists the dead-letter queues of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Lists the dead-letter queues (DLQs) of a pipeline with their record counts. A DLQ holds the records
that RDI rejected. Use
[`list-dlq-records`]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di-list-dlq-records" >}})
to read the records of a single queue.

## Usage

```
redis-di list-dlqs [flags]
```

## Options

| Option             | Description                                          |
| :----------------- | :--------------------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`).              |
| `-o`, `--output`   | Output format: `table` (default), `json`, or `yaml`. |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di list-dlqs
```
