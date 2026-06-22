---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/reference/cli/redis-di.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: redis-di
aliases: null
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description: A command line tool to manage & configure Write-behind
group: di
linkTitle: redis-di
summary:
  Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 10
---

## Usage

```
Usage: redis-di [OPTIONS] COMMAND [ARGS]...
```

## Options

- `version`:

  - Type: BOOL
  - Default: `false`
  - Usage: `--version`

  Show the version and exit.

- `help`:

  - Type: BOOL
  - Default: `false`
  - Usage: `--help`

  Show this message and exit.

## CLI help

```
Usage: redis-di [OPTIONS] COMMAND [ARGS]...

  A command line tool to manage & configure Write-behind

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  add-context           Adds a new context
  configure             Configures the Write-behind Database so it is ready to...
  create                Creates the Write-behind Database instance
  delete                Deletes Write-behind database permanently
  delete-all-contexts   Deletes all contexts
  delete-context        Deletes a context
  deploy                Deploys the Write-behind configurations including target
  describe-job          Describes a transformation engine's job
  dump-support-package  Dumps Write-behind support package
  get-rejected          Returns all the stored rejected entries
  list-contexts         Lists all saved contexts
  list-jobs             Lists transformation engine's jobs
  monitor               Monitors Write-behind by collecting metrics and exporting...
  reset                 Resets the pipeline into initial full sync mode
  scaffold              Generates configuration files for Write-behind and...
  set-context           Sets a context to be the active one
  set-secret            Writes a secret to Redis secret store
  start                 Starts the pipeline
  status                Displays the status of the pipeline end to end
  stop                  Stops the pipeline
  trace                 Starts a trace session for troubleshooting data...
  upgrade               Upgrades Write-behind Engine without losing data or downtime
```
