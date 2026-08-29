---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/cli/redis-di-dump-support-package.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.187715Z"
---
# Redis Di Dump Support Package

---
Title: redis-di dump-support-package
linkTitle: redis-di dump-support-package
description: Dumps the RDI support package
weight: 10
alwaysopen: false
categories: ["redis-di"]
aliases:
- /integrate/redis-data-integration/ingest/reference/cli/redis-di-dump-support-package/
---

Dumps a comprehensive set of RDI forensics data that you can send to Redis support (see
[Dump support package]({{< relref "/integrate/redis-data-integration/troubleshooting#dump-support-package" >}})).
This is an administration command that is available only on VM installations, where `redis-di`
forwards it to the bundled `rdi-admin` tool.

## Usage

```
redis-di dump-support-package [OPTIONS]
```

## Options

| Option               | Description                                                                              |
| :------------------- | :--------------------------------------------------------------------------------------- |
| `-l`, `--log-level`  | Log level: `TRACE`, `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL` (default `INFO`). |
| `--rdi-namespace`    | RDI Kubernetes namespace (default `rdi`).                                                |
| `--rdi-host`         | Host or IP of the RDI database (required).                                               |
| `--rdi-port`         | Port of the RDI database, `1`–`65535` (required).                                        |
| `--rdi-user`         | RDI database username.                                                                   |
| `--rdi-password`     | RDI database password.                                                                   |
| `--rdi-key`          | Private key file to authenticate with.                                                   |
| `--rdi-cert`         | Client certificate file to authenticate with.                                            |
| `--rdi-cacert`       | CA certificate file to verify with.                                                      |
| `--rdi-key-password` | Password for unlocking an encrypted private key.                                         |
| `--dir`              | Directory where the support file is generated (default `.`).                             |
| `--dump-rejected`    | Dump rejected records.                                                                   |
| `--log-days`         | Number of days to look back for log files (default `2`).                                 |
