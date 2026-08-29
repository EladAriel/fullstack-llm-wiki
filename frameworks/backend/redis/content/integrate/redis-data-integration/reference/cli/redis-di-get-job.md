---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-get-job.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.188753Z"
---
# Redis Di Get Job

---
Title: redis-di get-job
linkTitle: redis-di get-job
description: Gets a job of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Gets a single job of a pipeline and prints it in the compact `list-jobs` table format. Use
[`describe-job`]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di-describe-job" >}})
for the full job view with its transformations and outputs.

## Usage

```
redis-di get-job <name> [flags]
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
redis-di get-job customers_hash_job
```
