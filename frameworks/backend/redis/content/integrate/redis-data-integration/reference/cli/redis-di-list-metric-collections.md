---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-list-metric-collections.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.186824Z"
---
# Redis Di List Metric Collections

---
Title: redis-di list-metric-collections
linkTitle: redis-di list-metric-collections
description: Lists the metric collections of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Lists the metric collections of a pipeline. Metric collections hold the raw component metrics that
the [`describe`]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di-describe" >}})
command summarizes in its Statistics and Performance sections. This command is most useful with
`-o json` or `-o yaml` for scripting and for tools such as `jq`.

## Usage

```
redis-di list-metric-collections [flags]
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
redis-di list-metric-collections
```
