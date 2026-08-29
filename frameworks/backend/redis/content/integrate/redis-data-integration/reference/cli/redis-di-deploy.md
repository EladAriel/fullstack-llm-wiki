---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-deploy.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.188044Z"
---
---
Title: redis-di deploy
linkTitle: redis-di deploy
description: Deploys a pipeline with the specified configuration
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
- /integrate/redis-data-integration/ingest/reference/cli/redis-di-deploy/
---

Deploys a pipeline, creating it or updating it from the configuration in the `--dir` directory. The
API validates the configuration and rejects an invalid one. By default, the command starts the
pipeline after deploying and waits for it to reach the expected state. `set` is an alias for this
command.

## Usage

```
redis-di deploy [pipeline] [flags]
```

The pipeline name is an optional argument that defaults to `default`.

## Options

| Option              | Description                                                                          |
| :------------------ | :----------------------------------------------------------------------------------- |
| `--dir`             | Directory containing the pipeline configuration (default `.`).                       |
| `--dry-run`         | Validate the configuration without deploying.                                        |
| `--validate-tables` | Validate the configuration against the source and target databases (default `true`). |
| `--validate-cdc`    | Validate the source database CDC configuration.                                      |
| `--start`           | Start the pipeline after deploying (default `true`).                                 |
| `--wait`            | Wait for the pipeline to reach the expected state (default `true`).                  |
| `--timeout`         | Maximum time to wait for the pipeline to reach the expected state (default `2m`).    |

This command also accepts the
[global options]({{< relref "/integrate/redis-data-integration/reference/cli/redis-di#global-options" >}}).

## Example

```bash
# Deploy the configuration in the current directory
redis-di deploy

# Validate a configuration folder without deploying it
redis-di deploy --dir /opt/rdi/config --dry-run
```
