---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-get-metric-collection.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.186277Z"
---
# Redis Di Get Metric Collection

---
Title: redis-di get-metric-collection
linkTitle: redis-di get-metric-collection
description: Gets a metric collection of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Gets a single metric collection of a pipeline, returning its raw metric data. This command is most
useful with `-o json` or `-o yaml` for scripting and for tools such as `jq`. Use
[`list-metric-collections`]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di-list-metric-collections" >}})
to see the available collections.

## Usage

```
redis-di get-metric-collection <name> [flags]
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
redis-di get-metric-collection processor -o json
```
