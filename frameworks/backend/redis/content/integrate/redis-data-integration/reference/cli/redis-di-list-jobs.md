---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-list-jobs.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.189258Z"
---
# Redis Di List Jobs

---
Title: redis-di list-jobs
linkTitle: redis-di list-jobs
description: Lists the jobs of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
- /integrate/redis-data-integration/ingest/reference/cli/redis-di-list-jobs/
---

Lists the jobs of a pipeline, one row per job with its source, its transformation and output counts,
and the target connections of its outputs. Use
[`describe-job`]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di-describe-job" >}})
for the full view of a single job.

## Usage

```
redis-di list-jobs [flags]
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
redis-di list-jobs
```
