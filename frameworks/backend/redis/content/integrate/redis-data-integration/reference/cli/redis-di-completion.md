---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-completion.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.186459Z"
---
# Redis Di Completion

---
Title: redis-di completion
linkTitle: redis-di completion
description: Generates a shell autocompletion script
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

Generates an autocompletion script for `redis-di` for the specified shell. Supported shells are
`bash`, `zsh`, `fish`, and `powershell`.

## Usage

```
redis-di completion [bash|zsh|fish|powershell]
```

Run `redis-di completion <shell> --help` for the per-shell installation instructions.

## Example

To load completions into the current `bash` session:

```bash
source <(redis-di completion bash)
```
