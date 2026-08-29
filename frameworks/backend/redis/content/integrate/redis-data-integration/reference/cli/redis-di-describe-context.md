---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-describe-context.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.191173Z"
---
# Redis Di Describe Context

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
