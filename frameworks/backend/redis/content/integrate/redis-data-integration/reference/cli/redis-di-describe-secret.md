---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-describe-secret.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: redis-di describe-secret
linkTitle: redis-di describe-secret
description: Describes a secret of a pipeline
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Describes a single secret of a pipeline. The API never returns secret values, so the output shows
only the key and whether it is set, not the stored value.

## Usage

```
redis-di describe-secret <key> [flags]
```

## Options

| Option             | Description                             |
| :----------------- | :-------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`). |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
redis-di describe-secret TARGET_DB_PASSWORD
```
