---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-pgxlogdump.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

## `pg_xlogdump` renamed to `pg_waldump`

pg_xlogdump
pg_waldump

PostgreSQL 9.6 and below provided a command named `pg_xlogdump` pg_xlogdump to read write-ahead-log (WAL) files. This command was renamed to `pg_waldump`, see `pgwaldump` for documentation of `pg_waldump` and see the release notes for PostgreSQL 10 for details on this change.
