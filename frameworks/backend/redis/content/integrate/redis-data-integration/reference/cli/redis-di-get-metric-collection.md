---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-get-metric-collection.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
