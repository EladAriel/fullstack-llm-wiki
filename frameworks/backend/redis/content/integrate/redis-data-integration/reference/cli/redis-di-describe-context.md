---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-describe-context.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: redis-di describe-context
linkTitle: redis-di describe-context
description: Describes a context
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Describes a single context from the `~/.redis-di` context file, showing its API connection details.
See the [CLI reference overview]({{< relref "/integrate/redis-data-integration/reference/cli#contexts" >}})
for more about contexts.

## Usage

```
redis-di describe-context <name> [flags]
```

## Options

This command takes only the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di describe-context prod
```
