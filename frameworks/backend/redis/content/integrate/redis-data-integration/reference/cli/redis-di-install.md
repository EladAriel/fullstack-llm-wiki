---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-install.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: redis-di install
linkTitle: redis-di install
description: Installs RDI
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
---

## Usage

```
Usage: redis-di install [OPTIONS]
```

## Options

- `log_level`:
  - Type: Choice(['TRACE', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
  - Default: `warning`
  - Usage: `--log-level
-l`

- `file`:
  - Type: <click.types.Path object>
  - Default: `none`
  - Usage: `-f
--file`

  Path to a YAML configuration file for silent installation

- `online`:
  - Type: BOOL
  - Default: `false`
  - Usage: `--online`

  Run installer in online mode

- `k3s_only`:
  - Type: BOOL
  - Default: `false`
  - Usage: `--k3s-only`

  Install only k3s components

- `https_port`:
  - Type: INT
  - Default: `443`
  - Usage: `--https-port`

  HTTPS port for Traefik

- `installation_dir`:
  - Type: <click.types.Path object>
  - Default: `none`
  - Usage: `--installation-dir`

  Custom installation directory

- `help`:
  - Type: BOOL
  - Default: `false`
  - Usage: `--help`

  Show this message and exit.

## CLI help

```
Usage: redis-di install [OPTIONS]

  Installs RDI

Options:
  -l, --log-level [TRACE|DEBUG|INFO|WARNING|ERROR|CRITICAL]
                                  [default: WARNING]
  -f, --file FILE                 Path to a YAML configuration file for silent
                                  installation
  --installation-dir DIRECTORY    Custom installation directory
  --help                          Show this message and exit.
```
