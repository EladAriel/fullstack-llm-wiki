---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-completion.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
