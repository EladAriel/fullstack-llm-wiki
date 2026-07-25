---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pgtestfsync.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

pg_test_fsync

`pg_test_fsync`
1
Application

pg_test_fsync
determine fastest `wal_sync_method` for PostgreSQL

`pg_test_fsync`
`option`

## Description

`pg_test_fsync` is intended to give you a reasonable idea of what the fastest `guc-wal-sync-method` is on your specific system, as well as supplying diagnostic information in the event of an identified I/O problem. However, differences shown by `pg_test_fsync` might not make any significant difference in real database throughput, especially since many database servers are not speed-limited by their write-ahead logs. `pg_test_fsync` reports average file sync operation time in microseconds for each `wal_sync_method`, which can also be used to inform efforts to optimize the value of `guc-commit-delay`.

## Options

`pg_test_fsync` accepts the following command-line options: - Specifies the file name to write test data in. This file should be in the same file system that the `pg_wal` directory is or will be placed in. (`pg_wal` contains the WAL files.) The default is `pg_test_fsync.out` in the current directory. - Specifies the number of seconds for each test. The more time per test, the greater the test's accuracy, but the longer it takes to run. The default is 5 seconds, which allows the program to complete in under 2 minutes. - Print the `pg_test_fsync` version and exit. - Show help about `pg_test_fsync` command line arguments, and exit.

## Environment

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

## See Also
