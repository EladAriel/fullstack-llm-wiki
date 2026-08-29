---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-get.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.186645Z"
---
# Redis Di Get

---
Title: redis-di get
linkTitle: redis-di get
description: Gets a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Gets a single pipeline and prints it in the compact `list` table format. Use
[`describe`]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di-describe" >}})
for the full pipeline view with its status and metrics.

## Usage

```
redis-di get [pipeline] [flags]
```

The pipeline name is an optional argument that defaults to `default`.

## Options

| Option           | Description                                          |
| :--------------- | :--------------------------------------------------- |
| `-o`, `--output` | Output format: `table` (default), `json`, or `yaml`. |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di get
redis-di get my-pipeline -o yaml
```
