---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/reference/cli/redis-di-scaffold.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: redis-di scaffold
aliases: null
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description:
  Generates configuration files for Write-behind and Debezium (when ingesting data
  to Redis)
group: di
linkTitle: redis-di scaffold
summary:
  Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 10
---

## Usage

```
Usage: redis-di scaffold [OPTIONS]
```

## Options

- `loglevel`:

  - Type: Choice(['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'])
  - Default: `info`
  - Usage: `--loglevel
-log-level`

- `db_type` (REQUIRED):

  - Type: Choice([<DbType.MYSQL: 'mysql'>, <DbType.ORACLE: 'oracle'>, <DbType.POSTGRESQL: 'postgresql'>, <DbType.REDIS: 'redis'>, <DbType.SQLSERVER: 'sqlserver'>])
  - Default: `none`
  - Usage: `--db-type`

  DB type

- `strategy`:

  - Type: Choice([<Strategy.INGEST: 'ingest'>, <Strategy.WRITE_BEHIND: 'write_behind'>])
  - Default: `ingest`
  - Usage: `--strategy`

  Strategy

  Output to directory or stdout

- `directory`:

  - Type: STRING
  - Default: `none`
  - Usage: `--dir`

  Directory containing Write-behind configuration

- `preview`:

  - Type: Choice(['debezium/application.properties', 'config.yaml'])
  - Default: `none`
  - Usage: `--preview`

  Print the content of specified config file to CLI output

- `help`:

  - Type: BOOL
  - Default: `false`
  - Usage: `--help`

  Show this message and exit.

## CLI help

```
Usage: redis-di scaffold [OPTIONS]

  Generates configuration files for Write-behind and Debezium (when ingesting data to
  Redis)

Options:
  -log-level, --loglevel [DEBUG|INFO|WARN|ERROR|CRITICAL]
                                  [default: INFO]
  --db-type [mysql|oracle|postgresql|redis|sqlserver]
                                  DB type  [required]
  --strategy [ingest|write_behind]
                                  Strategy  [default: ingest]
  Output formats: [mutually_exclusive, required]
                                  Output to directory or stdout
    --dir TEXT                    Directory containing Write-behind configuration
    --preview [debezium/application.properties|config.yaml]
                                  Print the content of specified config file
                                  to CLI output
  --help                          Show this message and exit.
```
