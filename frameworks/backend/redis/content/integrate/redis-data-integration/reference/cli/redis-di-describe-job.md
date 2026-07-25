---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-describe-job.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: redis-di describe-job
linkTitle: redis-di describe-job
description: Describes a job of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Describes a single job of a pipeline, printing its source properties followed by tables that
summarize its transformations and outputs.

## Usage

```
redis-di describe-job <name> [flags]
```

## Options

| Option             | Description                             |
| :----------------- | :-------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`). |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di describe-job customers_hash_job
```
