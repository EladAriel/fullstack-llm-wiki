---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-list-contexts.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.188434Z"
---
# Redis Di List Contexts

---
Title: redis-di list-contexts
linkTitle: redis-di list-contexts
description: Lists all contexts
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
- /integrate/redis-data-integration/ingest/reference/cli/redis-di-list-contexts/
---

Lists all contexts from the `~/.redis-di` context file and indicates which one is active. See the
[CLI reference overview]({{< relref "/integrate/redis-data-integration/reference/cli#contexts" >}})
for more about contexts.

## Usage

```
redis-di list-contexts [flags]
```

## Options

This command takes only the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di list-contexts
```
